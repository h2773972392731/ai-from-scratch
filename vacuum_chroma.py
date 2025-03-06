from chromadb.utils.vacuum import vacuum

db_path = "E:\\PycharmProjects\\python_project_vs\\data_base\\vector_db\\chroma"
vacuum(path=db_path)
print("Vacuum completed!")