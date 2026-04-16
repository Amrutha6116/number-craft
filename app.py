from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None

    if request.method == 'POST':
        try:
            numbers = request.form['numbers']
            operation = request.form['operation']

            # Convert input string → list of numbers
            nums = list(map(float, numbers.split()))

            if len(nums) < 2:
                error = "Please enter at least 2 numbers"

            else:
                if operation == 'add':
                    result = sum(nums)

                elif operation == 'sub':
                    result = nums[0]
                    for n in nums[1:]:
                        result -= n

                elif operation == 'mul':
                    result = 1
                    for n in nums:
                        result *= n

                elif operation == 'div':
                    result = nums[0]
                    for n in nums[1:]:
                        if n == 0:
                            raise ZeroDivisionError
                        result /= n

                elif operation == 'mod':
                    result = nums[0]
                    for n in nums[1:]:
                        if n == 0:
                            raise ZeroDivisionError
                        result %= n

        except ZeroDivisionError:
            error = "Cannot divide by zero"
        except:
            error = "Invalid input"

    return render_template("index.html", result=result, error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))