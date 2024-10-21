from django.shortcuts import render, redirect
from .models import Movement
from .forms import MovementForm


def movement_list(request):
    movements = Movement.objects.all()
    return render(request, "movements/movement_list.html", {"movements": movements})


def movement_create(request):
    if request.method == "POST":
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movement_list")
    else:
        form = MovementForm()
    return render(request, "movements/movement_form.html", {"form": form})


def movement_update(request, pk):
    movement = Movement.objects.get(pk=pk)
    if request.method == "POST":
        form = MovementForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            return redirect("movement_list")
    else:
        form = MovementForm(instance=movement)
    return render(request, "movements/movement_form.html", {"form": form})


def movement_delete(request, pk):
    movement = Movement.objects.get(pk=pk)
    if request.method == "POST":
        movement.delete()
        return redirect("movement_list")
    return render(
        request, "movements/movement_confirm_delete.html", {"movement": movement}
    )
