def save_output(file_path):
    print('Saving output')
    df.to_csv(file_path, index = False)