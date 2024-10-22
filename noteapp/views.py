from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Note, Folder, NoteContent, NoteImage, NotePDF

def listone(request):
    try:
        unit = Note.objects.get(nName="第一篇筆記")
    except Note.DoesNotExist:
        unit = None
        errormessage = '(讀取錯誤)!'
    return render(request, "listone.html", locals())

def listall(request):
    folder_id = request.GET.get('folder')
    if folder_id:
        notes = Note.objects.filter(folder_id=folder_id).order_by('id')
    else:
        notes = Note.objects.all().order_by('id')

    folders = Folder.objects.all()  # 獲取所有文件夾以供篩選
    return render(request, 'listall.html', {'notes': notes, 'folders': folders})

def insert(request):
    if request.method == 'POST':
        # 檢查筆記名稱的唯一性
        if Note.objects.filter(nName=request.POST.get('name')).exists():
            error_message = '此筆記名稱已存在，請選擇其他名稱。'
            folders = Folder.objects.all()
            return render(request, 'insert.html', {'folders': folders, 'error_message': error_message})

        # 創建基本筆記
        note = Note.objects.create(
            nName=request.POST.get('name'),
            nDate=request.POST.get('date'),
            folder_id=request.POST.get('folder')
        )

        # 處理多段內容
        contents = request.POST.getlist('description[]')
        for idx, content in enumerate(contents):
            NoteContent.objects.create(
                note=note,
                content=content,
                order=idx
            )

        # 處理多張圖片
        images = request.FILES.getlist('image[]')
        for idx, image in enumerate(images):
            NoteImage.objects.create(
                note=note,
                image=image,
                order=idx
            )

        # 處理多個PDF
        pdfs = request.FILES.getlist('pdf[]')
        for idx, pdf in enumerate(pdfs):
            NotePDF.objects.create(
                note=note,
                pdf=pdf,
                order=idx
            )

        return redirect('listall')

    folders = Folder.objects.all()
    return render(request, 'insert.html', {'folders': folders})

def modify(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    folders = Folder.objects.all()  # 獲取所有的資料夾

    # 獲取當前筆記的內容、圖片和 PDF
    contents = note.contents.all()  # 假設 Note 與 NoteContent 有一對多關聯
    images = note.images.all()  # 假設 Note 與 NoteImage 有一對多關聯
    pdfs = note.pdfs.all()  # 假設 Note 與 NotePDF 有一對多關聯

    if request.method == 'POST':
        note.nName = request.POST['name']
        note.nDate = request.POST['date']
        note.folder_id = request.POST['folder']  # 更新文件夾
        note.save()  # 儲存變更

        # 更新內容
        contents = request.POST.getlist('description[]')
        for idx, content in enumerate(contents):
            if idx < len(note.contents.all()):
                note.contents.all()[idx].content = content
                note.contents.all()[idx].save()
            else:
                NoteContent.objects.create(note=note, content=content, order=idx)

        # 更新圖片
        if 'image' in request.FILES:
            images = request.FILES.getlist('image[]')
            for idx, image in enumerate(images):
                NoteImage.objects.create(note=note, image=image, order=idx)

        # 更新 PDF
        if 'pdf' in request.FILES:
            pdfs = request.FILES.getlist('pdf[]')
            for idx, pdf in enumerate(pdfs):
                NotePDF.objects.create(note=note, pdf=pdf, order=idx)

        return redirect('view_note', note_id=note.id)  # 修改後跳轉到查看頁面

    return render(request, 'modify.html', {
        'note': note,
        'folders': folders,
        'contents': contents,  # 傳遞內容
        'images': images,  # 傳遞圖片
        'pdfs': pdfs,  # 傳遞 PDF
    })

def delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('listall')

def delete_image(request, image_id):
    image = get_object_or_404(NoteImage, id=image_id)
    image.delete()
    return JsonResponse({'status': 'success'})

def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(NotePDF, id=pdf_id)
    pdf.delete()
    return JsonResponse({'status': 'success'})

def view_all(request):
    folder_id = request.GET.get('folder')
    if folder_id:
        notes = Note.objects.filter(folder_id=folder_id).order_by('id')
    else:
        notes = Note.objects.all().order_by('id')
        
    folders = Folder.objects.all()  # 獲取所有文件夾以供篩選
    return render(request, 'view_all.html', {'notes': notes, 'folders': folders})

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    contents = note.contents.all()
    images = note.images.all()
    pdfs = note.pdfs.all()

    context = {
        'note': note,
        'contents': contents,
        'images': images,
        'pdfs': pdfs,
    }
    
    return render(request, 'view_note.html', context)
