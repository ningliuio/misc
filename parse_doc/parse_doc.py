"""
Parse MS Word .doc files, and search for keywords,
and then move to specific folders conditionally.

Developed for cleanning up the recovered files.
"""


import os
import subprocess as sp


def doc_to_text(filename,  source_path, coding='utf-8'):
    source_path = os.path.abspath(source_path)
    fullfilename = os.path.join(source_path, filename)
    if filename[-4:] == ".doc" or ".DOC":
        try:
            doctext = sp.check_output(["antiword", fullfilename])
            return doctext.decode(coding)
        except sp.CalledProcessError:
            err_file_path = os.path.abspath(source_path + '//damaged_files')
            if not os.path.isdir(err_file_path):
                os.mkdir(err_file_path)
            os.rename(fullfilename,
                      os.path.abspath(err_file_path + '//' + filename))
            return ''
        except UnicodeDecodeError:
            err_file_path = os.path.abspath(source_path + '//unicode_err_files')
            if not os.path.isdir(err_file_path):
                os.mkdir(err_file_path)
            os.rename(fullfilename,
                      os.path.abspath(err_file_path + '//' + filename))
            return ''


def pickout_doc(source_path, type_str, key_str):
    source_path = os.path.abspath(source_path)
    files_all = [f for f in os.listdir(source_path)
                 if os.path.isfile(os.path.join(source_path, f))]
    files_doc = [f for f in files_all
                 if (os.path.splitext(f)[1].lower() == type_str.lower())]
    files_out = [f for f in files_doc
                 if doc_to_text(f, source_path).find(key_str) != -1]

    # move filtered files to subfolder
    if files_out:
        target_path = os.path.abspath(source_path + '//' + key_str)
        if not os.path.isdir(target_path):
            os.mkdir(target_path)
        for f in files_out:
            os.rename(os.path.join(source_path, f), os.path.join(target_path, f))
    
    
