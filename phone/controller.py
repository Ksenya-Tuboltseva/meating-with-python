import view
import manager

def start():
    while True:
        choise = view.menu()
        if choise == 1:
            manager.open_file()
        elif choise == 2:
            manager.save_file()
        elif choise == 3:
            pb = manager.get()
            view.show_contact(pb)
        elif choise == 4:
            new = view.new_contact_input()
            manager.add(new)
        elif choise == 5:
            pb = manager.get()
            view.show_contact(pb)
            ind = view.input_id()
            contact = view.new_contact_input()
            manager.change_contact(ind, contact)
        elif choise == 6:
            find = view.find_contact()
            result = manager.find(find)
            view.input_id(result)
        elif choise == 7:
            pb = manager.get()
            view.show_contact(pb)
            ind = view.input_id()
            manager.delete_contact(ind)
        elif choise == 8:
            print("Работа закончена")
            break