from django.shortcuts import render, redirect
from .models import Container
from .forms import ContainerForm


def container_list(request):
    containers = Container.objects.all()
    return render(request, "containers/container_list.html", {"containers": containers})


def container_create(request):
    if request.method == "POST":
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("container_list")
    else:
        form = ContainerForm()
    return render(request, "containers/container_form.html", {"form": form})


def container_update(request, pk):
    container = Container.objects.get(pk=pk)
    if request.method == "POST":
        form = ContainerForm(request.POST, instance=container)
        if form.is_valid():
            form.save()
            return redirect("container_list")
    else:
        form = ContainerForm(instance=container)
    return render(request, "containers/container_form.html", {"form": form})


def container_delete(request, pk):
    container = Container.objects.get(pk=pk)
    if request.method == "POST":
        container.delete()
        return redirect("container_list")
    return render(
        request, "containers/container_confirm_delete.html", {"container": container}
    )
