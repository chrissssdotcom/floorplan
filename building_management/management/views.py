from django.shortcuts import render, get_object_or_404, redirect
from .models import Building, Floor, Location, Person
from .forms import BuildingForm, FloorForm, LocationForm, PersonForm

def home(request):
    buildings = Building.objects.all()
    floors = Floor.objects.all()
    locations = Location.objects.all()
    people = Person.objects.all()
    context = {
        'buildings': buildings,
        'floors': floors,
        'locations': locations,
        'people': people,
    }
    return render(request, 'management/home.html', context)

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'management/building_list.html', {'buildings': buildings})

def building_create(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('building_list')
    else:
        form = BuildingForm()
    return render(request, 'management/building_form.html', {'form': form})

def floor_list(request):
    floors = Floor.objects.all()
    return render(request, 'management/floor_list.html', {'floors': floors})

def floor_create(request):
    if request.method == "POST":
        form = FloorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('floor_list')
    else:
        form = FloorForm()
    return render(request, 'management/floor_form.html', {'form': form})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'management/location_list.html', {'locations': locations})

def location_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request, 'management/location_form.html', {'form': form})

def person_list(request):
    people = Person.objects.all()
    return render(request, 'management/person_list.html', {'people': people})

def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'management/person_form.html', {'form': form})

def plot_locations(request, floor_id):
    floor = get_object_or_404(Floor, id=floor_id)
    locations = floor.locations.all()
    return render(request, 'management/plot_locations.html', {'floor': floor, 'locations': locations})

def update_location_coordinates(request, location_id):
    if request.method == 'POST':
        location = get_object_or_404(Location, id=location_id)
        location.x_coordinate = request.POST.get('x')
        location.y_coordinate = request.POST.get('y')
        location.save()
        return redirect('plot_locations', floor_id=location.floor.id)