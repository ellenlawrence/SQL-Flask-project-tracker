"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    rows = hackbright.get_grades_by_github(github)

    # return f"{github} is the GitHub account for {first} {last}"

    return render_template("student_info.html", 
                            first=first,
                            last=last, 
                            github=github,
                            rows=rows
                            )


@app.route("/student-add")
def display_add_form():
    """Show form for adding a student."""
    return render_template("student_add.html")


@app.route("/add-student", methods=['POST'])
def student_add():
    """Add a student"""
    first = request.form.get('firs<br>t_name')
    last = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)
    
    return render_template("add_success.html", 
                            first=first,
                            last=last, 
                            )


@app.route("/project-search")
def get_project_search():
    """Show form for searching for a student."""

    return render_template("project_search.html") #to make


@app.route("/project")
def get_projects():
    """Show information for projects."""
    project = request.args.get('project')

    title, description, max_grade = hackbright.get_project_by_title(project)

    # return f"{github} is the GitHub account for {first} {last}"

    return render_template("project_info.html", 
                            title=title,
                            desc=description, 
                            max_grade=max_grade,)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
