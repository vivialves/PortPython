def count_smileys(arr):
    # The function returns the total of smiling faces.
    smiles = [[caracter for caracter in arr]for arr in arr]
    faces_2 = [list_faces for list_faces in smiles if len(list_faces) == 2]
    faces_3 = [list_faces for list_faces in smiles if len(list_faces) == 3]
    faces = []
    for i in range(0, len(faces_2)):
        if faces_2[i][0] == ':' or faces_2[i][0] == ';':
            if faces_2[i][1] == ')' or faces_2[i][1] == 'D':
                faces.append(faces_2[i])
    for i in range(0, len(faces_3)):
        if faces_3[i][0] == ':' or faces_3[i][0] == ';':
            if faces_3[i][1] == '-' or faces_3[i][1] == '~':
                if faces_3[i][2] == ')' or faces_3[i][2] == 'D':
                    faces.append(faces_3[i])

    return faces


print(count_smileys(['D;', ':~)', '.~D', ':)', ';-)', ':<D', ';~)', '**']))

