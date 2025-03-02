from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Document
from .forms import DocumentForm

@login_required
@permission_required('bookshelf.can_edit_document', raise_exception=True)
def edit_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_detail', doc_id=document.id)
    else:
        form = DocumentForm(instance=document)

    return render(request, 'edit_document.html', {'form': form})

@login_required
@permission_required('bookshelf.can_create_document', raise_exception=True)
def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect('document_detail', doc_id=document.id)
    else:
        form = DocumentForm()

    return render(request, 'create_document.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete_document', raise_exception=True)
def delete_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')

    return render(request, 'confirm_delete.html', {'document': document})
  
# Create your views here.
