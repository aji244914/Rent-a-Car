from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method=="POST":
        a=request.POST.get("num1")
        b=request.POST.get("num2")
        c= int(a)+ int(b)
        return render(request,'Basics/Add.html',{'result':c})
    else:
        return render(request,'Basics/Add.html')


def Largest(request):
    if request.method == "POST":
        # Get form data
        a = int(request.POST.get("larg1"))
        b = int(request.POST.get("larg2"))

        # Compare the two values to find the largest
        if a < b:
            c = b
        else:
            c = a

        # Render the result in the template
        return render(request, 'Basics/Largest.html', {'result': c})
    
    # For GET requests, just render an empty form
    return render(request, 'Basics/Largest.html')



def ranklist(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        department = request.POST.get("department")
        mark1 = int(request.POST.get("mark1"))
        mark2 = int(request.POST.get("mark2"))
        mark3 = int(request.POST.get("mark3"))

        # Calculate total, average, and grade
        total = mark1 + mark2 + mark3
        average = total / 3
        percentage = (total / 300) * 100
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"

        # Prepare data to pass to the template
        result = {
            "name": name,
            "gender": gender,
            "department": department,
            "mark1": mark1,
            "mark2": mark2,
            "mark3": mark3,
            "total": total,
            "average": average,
            "grade": grade,
            'percentage': percentage,
        }

        # Return the result in the template
        return render(request, 'Basics/Ranklist.html', {'result': result})

    # Render an empty form for GET requests
    return render(request, 'Basics/Ranklist.html')


def armstrong(request):
    result = None  # Default result value
    
    if request.method == "POST":
        # Get form data
        arm1 = request.POST.get("arm1")

        # Check if arm1 is a valid number
        if arm1.isdigit():
            number = int(arm1)  # Convert to an integer
            num_str = str(number)  # Convert the number to a string to get the digits
            num_digits = len(num_str)  # Get the number of digits
            sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  # Sum of digits raised to the power of the number of digits
            
            # Check if the number is an Armstrong number
            if sum_of_powers == number:
                result = f"{number} is an Armstrong number."
            else:
                result = f"{number} is not an Armstrong number."
        else:
            result = "Please enter a valid number."

    # Render the form and pass the result to the template
    return render(request, 'Basics/Armstrong.html', {'result': result})

    

