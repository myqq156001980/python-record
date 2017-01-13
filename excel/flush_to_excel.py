from xlsxwriter.workbook import Workbook
import os

def flush_to_excel(excel_path, headers, contents):
    """
    flush_to_excel(excel_path, headers, contents)
    excel_path: type->string
    headers: type->list,
    content: type->list[list]
    """
    output_dir, excel_name = os.path.split(excel_path)
    # 检测目标文件夹是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 创建excel文件和sheet
    ef = Workbook(excel_path)
    sheet = ef.add_worksheet("sheet1")

   # 写入headers
    for index, t in enumerate(headers):
        sheet.write(0, index, t)
    # 写入内容
    for row_index, l in enumerate(contents):
        for column_index, o in enumerate(l):
            sheet.write(row_index + 1, column_index, o)

    ef.close()
