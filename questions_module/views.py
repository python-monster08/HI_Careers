import os
from django.http import HttpResponse
from docx import Document
from docx.oxml import OxmlElement
from django.utils.html import strip_tags
from .models import Question

def remove_borders_from_cell(cell):
    """
    Remove all borders of a cell by setting the border elements to None.
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for border in ['top', 'left', 'bottom', 'right']:
        borderEl = OxmlElement(f'w:{border}')
        borderEl.set(border, 'nil')
        tcBorders.append(borderEl)
    tcPr.append(tcBorders)

def clean_text(text):
    """
    Replace newline characters with a single space and strip HTML tags.
    """
    return strip_tags(text.replace('\n', ' '))

def generate_questions_word_document(request):
    base_dir = r'F:/Kamlesh Lovewanshi/Office Work/genereted_word_files'
    os.makedirs(base_dir, exist_ok=True)

    document = Document()
    # document.add_heading('Questions', level=0)

    for question in Question.objects.all():
        # Start a new table for each question
        table = document.add_table(rows=0, cols=3)
        table.style = 'Table Grid'
        
        # Clean and add the question text
        question_text = clean_text(str(question.question))
        question_row = table.add_row().cells
        question_row[0].text = 'Question'
        question_text_cell = question_row[1]
        question_text_cell.text = question_text
        question_text_cell.merge(question_row[2])  # Merge cells for question text

        # Add the question type
        type_row = table.add_row().cells
        type_row[0].text = 'Type'
        type_cell = type_row[1]
        type_cell.text = clean_text(str(question.question_type))
        type_cell.merge(type_row[2])  # Merge cells for type

        # Add options with correctness
        correct_option = question.correct_answer_option.lower()
        for option_label in ['a', 'b', 'c', 'd']:
            option_row = table.add_row().cells
            option_row[0].text = 'Option'
            option_text = getattr(question, f"option_{option_label}", '')
            option_row[1].text = clean_text(option_text)
            option_row[2].text = 'correct' if option_label == correct_option else 'incorrect'

        # Add the solution
        solution_row = table.add_row().cells
        solution_row[0].text = 'Solution'
        solution_text_cell = solution_row[1]
        correct_option_text = getattr(question, f"option_{correct_option}")
        solution_text_cell.text = clean_text(str(correct_option_text))
        solution_text_cell.merge(solution_row[2])  # Merge cells for solution

        # Add marks and negative marks
        marks_row = table.add_row().cells
        marks_row[0].text = 'Marks'
        marks_row[1].text = str(question.marks)
        marks_row[2].text = str(question.negative_marks if question.negative_marks else '')  # Negative marks

        # Add a paragraph for spacing between tables
        document.add_paragraph()

    file_path = os.path.join(base_dir, 'questions.docx')
    try:
        document.save(file_path)
        return_message = f"File saved at {file_path}"
    except Exception as e:
        return_message = f"An error occurred: {e}"

    return HttpResponse(return_message, content_type='text/plain')




# import os
# from django.http import HttpResponse
# from docx import Document
# from docx.oxml import OxmlElement
# from django.utils.html import strip_tags
# from .models import Question

# def remove_borders_from_cell(cell):
#     """
#     Remove all borders of a cell by setting the border elements to None.
#     """
#     # Access the cell's XML element
#     tc = cell._tc
#     # Access the cell properties and remove borders
#     tcPr = tc.get_or_add_tcPr()
#     borders = OxmlElement('w:tcBorders')
#     for border in ('top', 'left', 'bottom', 'right'):
#         border_el = OxmlElement(f'w:{border}')
#         border_el.set(f'{border}', 'nil')
#         borders.append(border_el)
#     tcPr.append(borders)

# def generate_questions_word_document(request):
#     base_dir = r'F:/Kamlesh Lovewanshi/Office Work/genereted_word_files'
#     os.makedirs(base_dir, exist_ok=True)

#     document = Document()
#     document.add_heading('Question', level=0)

#     for question in Question.objects.all():
#         table = document.add_table(rows=1, cols=3)  # Change to 3 columns to accommodate negative marks
#         table.style = 'Table Grid'

#         # Add question text in a merged cell across the first row
#         question_cell = table.cell(0, 0)
#         question_cell.text = 'Question'
#         merged_question_cell = question_cell.merge(table.cell(0, 2))
#         merged_question_cell.text = strip_tags(str(question.question))

#         # row_cells = table.add_row().cells
#         # row_cells[0].text = 'Question'
#         # row_cells[1].text = strip_tags(str(question.question))

#         # Additional rows for Type, Options, Correct Answer, Solution, Marks, and Negative Marks
#         row_cells = table.add_row().cells
#         row_cells[0].text = 'Type'
#         row_cells[1].text = str(question.question_type)

#         if hasattr(question, 'option_a'):
#             options = [
#                 ('A', question.option_a),
#                 ('B', question.option_b),
#                 ('C', question.option_c),
#                 ('D', question.option_d)
#             ]

#             for label, option in options:
#                 row_cells = table.add_row().cells
#                 row_cells[0].text = f'Option'
#                 row_cells[1].text = option

#         row_cells = table.add_row().cells
#         row_cells[0].text = 'Solution'
#         correct_option = getattr(question, f"option_{question.correct_answer_option.lower()}")
#         row_cells[1].text = f'{correct_option}'

#         # row_cells = table.add_row().cells
#         # row_cells[0].text = 'Solution'
#         # row_cells[1].text = strip_tags(str(question.correct_answer_description))

#        # Insert the marks in a separate row with three cells
#         marks_row = table.add_row().cells
#         marks_row[0].text = 'Marks'
#         marks_row[1].text = str(question.marks)

#         # Add negative marks if available
#         if hasattr(question, 'negative_marks') and question.negative_marks is not None:
#             marks_row[2].text = str(question.negative_marks)
#         else:
#             # If there are no negative marks, we keep the cell empty or you could merge the cells
#             # marks_row[1].merge(marks_row[2]) # Optional: merge if you want only 2 cells displayed
#             pass  # Or simply do nothing to leave the cell blank

#         # Add a blank row at the end of each question for spacing
#         blank_row = table.add_row()
#         for cell in blank_row.cells:
#             remove_borders_from_cell(cell)

#     file_name = 'questions.docx'
#     file_path = os.path.join(base_dir, file_name)

#     try:
#         document.save(file_path)
#         return_message = f"File saved at {file_path}"
#     except Exception as e:
#         return_message = f"An error occurred: {e}"

#     return HttpResponse(return_message, content_type='text/plain')
# import os
# from django.http import HttpResponse
# from docx import Document
# from docx.shared import Pt
# from docx.oxml.ns import qn
# from docx.oxml import OxmlElement
# from django.utils.html import strip_tags
# from .models import Question

# def remove_borders_from_cell(cell):
#     """
#     Remove all borders of a cell by setting the border elements to None.
#     """
#     tc = cell._tc
#     tcPr = tc.get_or_add_tcPr()
#     tcBorders = OxmlElement('w:tcBorders')
#     for border in ['top', 'left', 'bottom', 'right']:
#         borderEl = OxmlElement(f'w:{border}')
#         borderEl.set(qn(f'w:{border}'), 'nil')
#         tcBorders.append(borderEl)
#     tcPr.append(tcBorders)

# def generate_questions_word_document(request):
#     base_dir = 'F:/Kamlesh Lovewanshi/Office Work/genereted_word_files'
#     os.makedirs(base_dir, exist_ok=True)

#     document = Document()
#     document.add_heading('Questions', level=0)

#     for question in Question.objects.all():
#         table = document.add_table(rows=1, cols=2)
#         table.style = 'Table Grid'

#         # Insert the question
#         question_text = strip_tags(str(question.question))
#         question_cell = table.cell(0, 0)
#         merged_question_cell = question_cell.merge(table.cell(0, 1))
#         merged_question_cell.text = question_text

#         # Insert the question type
#         row_cells = table.add_row().cells
#         row_cells[0].text = 'Type'
#         row_cells[1].text = 'multiple_choice'  # or whatever the type is

#         # Insert the options
#         correct_option = getattr(question, f"option_{question.correct_answer_option.lower()}", None)
#         for option_label in ['a', 'b', 'c', 'd']:
#             option_text = getattr(question, f"option_{option_label}", '')
#             is_correct = 'correct' if option_text == correct_option else 'incorrect'
#             row_cells = table.add_row().cells
#             row_cells[0].text = f'Option {option_label.upper()}'
#             row_cells[1].text = f'{strip_tags(str(option_text))} ({is_correct})'

#         # Insert the correct answer
#         row_cells = table.add_row().cells
#         row_cells[0].text = 'Correct Answer'
#         row_cells[1].text = strip_tags(str(correct_option))

#         # Insert the solution if it exists (assumed to be stored in 'correct_answer_description')
#         if hasattr(question, 'correct_answer_description'):
#             row_cells = table.add_row().cells
#             row_cells[0].text = 'Solution'
#             row_cells[1].text = strip_tags(str(question.correct_answer_description))

#         # Insert the marks in separate cells
#         row_cells = table.add_row().cells
#         row_cells[0].text = 'Marks'
#         row_cells[1].text = str(question.marks)
        
#         # Create a new cell for negative marks
#         # If the table has predefined styles that include borders, we may need to manually adjust them
#         if question.negative_marks is not None:
#             row_cells = table.add_row().cells
#             remove_borders_from_cell(row_cells[0])  # Remove border from label cell (which we'll leave blank)
#             row_cells[1].text = 'Negative Marks'
#             neg_marks_cell = table.cell(table.rows[-2].cells[1]._index[1], 1)  # Get the newly created cell
#             neg_marks_cell.text = str(question.negative_marks)
#             # Set the negative marks cell to span two columns
#             neg_marks_cell.merge(table.cell(table.rows[-2].cells[1]._index[1], 2))

#         # Remove borders from the last cell for spacing
#         remove_borders_from_cell(table.add_row().cells[0])

#     # Save the document
#     file_name = 'questions.docx'
#     file_path = os.path.join(base_dir, file_name)
#     document.save(file_path)
    
#     return HttpResponse(f"File saved at {file_path}", content_type='text/plain')





    
def index(request):
    return HttpResponse("This is our home page!")