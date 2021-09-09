'''
    Author: Kai-Yu L. Yu
    Purpose: This is the main file needed to run the StudyHelp program. 
    Date: August 31, 2021
'''
import os
import sys
import FileIO

# Class to handle and enter a program mode based on command line arguments
class UserInterface:    
    def __init__(self):
        self.data = FileIO.FileIO()
        self.loaded_serialized = 0
            
    def display_usage(self):
        os.system("clear")
        print("\033[95mSTUDYHELP USAGE INFORMATION\033[0m\n"
              "> To enter interactive mode, add -i in the command line when running the program.\n"
              "\t\x1B[3m[StudyHelp.py -i]\x1B[23m\n"
              "> To enter report mode, add -r and the filenames of the data files to be loaded when running the program.\n"
              "\t\x1B[3m[StudyHelp.py -r <student_file> <unit_file> <network_file>]\x1B[23m")
    
    def interactive_mode(self):
        os.system("clear")
        self.print_divider()
        print( "\033[95mSTUDYHELP INTERACTIVE MODE\033[0m\n" 
                "(1)  Load data\n" 
                "(2)  Student Details\n" 
                "(3)  Unit Details\n" 
                "(4)  Student Tutor Information\n" 
                "(5)  Unit Tutor Information\n" 
                "(6)  Statistics\n" 
                "(7)  Save data\n" 
                "(8)  Exit")
        
        option = input("Enter menu option number: ")
        if option == "1":
            self.load_data()
        elif option == "2":
            self.find_student()
        elif option == "3":
            self.find_unit()
        elif option == "4":
            self.get_student_network()
        elif option == "5":
            self.get_unit_network()
        elif option == "6":
            self.show_statistics()
        elif option == "7":
            self.save_data()
        elif option == "8":
            sys.exit("\033[92mProgram closed.\033[0m")
        else:
            print("\033[91mInvalid menu option entered. Please try again.\033[0m")   
        
        self.back_to_menu() 
    
    def report_mode(self):
        os.system("clear")
        self.print_divider()
        print("\033[95mSTUDYHELP REPORT MODE\033[0m")
        self.load_data()
        self.show_statistics()

    def load_data(self):
        # Provide load data options in interactive mode
        if sys.argv[1] == "-i":
            print("\n[a] Student data\n"
                  "[b] Unit data\n"
                  "[c] Network data\n"
                  "[d] Serialised data")

            load_option = input("Select data to be loaded: ").upper()
            if load_option == "A":
                if self.data.student_hash.count != 0:
                    print("\033[93mStudent file already loaded!\033[0m")
                else:
                    student_file = input("Enter filename containing STUDENT data: ") 
                    self.data.read_file(student_file, load_option)
                    print("\033[92mSuccessfully loaded student data.\033[0m")
            elif load_option == "B":
                if self.data.unit_hash.count != 0:
                    print("\033[93mUnit file already loaded!\033[0m")
                else:
                    unit_file = input("Enter filename containing UNIT data: ") 
                    self.data.read_file(unit_file, load_option)
                    print("\033[92mSuccessfully loaded unit data.\033[0m")
            elif load_option == "C":
                if not self.data.network_graph._vertices.is_empty():
                    print("\033[93mNetwork file already loaded!\033[0m")
                else:
                    network_file = input("Enter filename containing NETWORK data: ") 
                    self.data.read_file(network_file, load_option)
                    print("\033[92mSuccessfully loaded network data.\033[0m")
            elif load_option == "D":
                self.data.load_serialized()
            else:
                print("\033[91mInvalid input. Please try again.\033[0m")
                self.load_data()
            
        # Load three data files from command line in report mode
        elif sys.argv[1] == "-r":
            self.data.read_file(sys.argv[2], "A")
            print("\033[92mSuccessfully loaded student data.\033[0m")
            
            self.data.read_file(sys.argv[3], "B")
            print("\033[92mSuccessfully loaded unit data.\033[0m")
            
            self.data.read_file(sys.argv[4], "C")
            print("\033[92mSuccessfully loaded network data.\033[0m")
        
    def find_student(self):
        student = input("Enter student ID or name: ")
        if student.isdigit():   # If student ID is entered
            details = self.data.student_hash.get_key(student)
        else:                   # If student name is entered
            details = self.data.student_hash.get_value(student)
            
        print("\n\033[4mStudent Details\033[0m\n" + details)
    
    def find_unit(self):
        unit = input("Enter unit code: ")
        print("\n\033[4mCourse Unit Details\033[0m\n" + self.data.unit_hash.get_key(unit))
    
    def get_student_network(self):
        student = input("Enter student ID: ")
        print("\nTutoring Network of " + student + "\n\n" + self.data.network_graph.network_BFS(student))
        self.data.network_graph._BFS_count = 0          #### COUNT EDIT FOR BFS LINES
        
    def get_unit_network(self):
        unit = input("Enter unit code: ")
        unit_name = self.data.unit_hash.get_key(unit, False)
        print("\nStudents tutored in " + unit_name + " (" + unit + ")\n" + 
              self.data.network_graph.students_in_unit(unit_name) + "\nTutors\n" +
              self.data.network_graph.tutors_in_unit(unit_name))
    
    # Some calculations are discussed in the Project Report
    def show_statistics(self):
        self.print_divider()
        self.data.network_graph.network_DFS()
        print("\033[93mStudyHelp Network Statistics\033[0m" + "\n"
              "Total Number of Students enrolled in the University: " + str(self.data.student_hash.count) + "\n"
              "Total Number of Units offered by the University: " + str(self.data.unit_hash.count) + "\n"
              "Number of Participants in the Network: " + str(self.data.network_graph.network_count()) + "\n"
              "Number of Students who are not Tutors: " + str(self.data.network_graph.student_only_count()) + "\n"
              "Number of Tutors: " + str(self.data.network_graph.tutor_count()) + "\n"
              "Number of Units: " + str(self.data._unit_count) + "\n"
              "Average Number of Tutors per Unit: " + str(round(self.data.network_graph.tutor_count() / self.data._unit_count)) + "\n"
              "Tutor (can be both tutor and student) to Student (only) Ratio: " + str(self.data.network_graph.tutor_count()) + " : " + str(self.data.network_graph.student_only_count()) + "\n"
              "Number of Cycles: " + str(self.data.network_graph._DFS_count))
    
    def save_data(self):
        self.data.serialize_data()
    
    def back_to_menu(self):
        choice = input("Go back to interactive menu [y\\n]? ").upper()
        if choice == "Y":
            self.interactive_mode()
        elif choice == "N":
            raise Exception("\033[91mUser exited the program.\033[0m")
        else:
            print("\033[91mInvalid action. Please try again\033[0m")
            self.back_to_menu()
        
    # Print for better sectioned terminal output
    def print_divider(self):
        print("------------------------------------------------------------------")  
        
# Driver code for StudyHelp program
if __name__ == '__main__':
    study_help = UserInterface()
    if len(sys.argv) == 1:
        study_help.display_usage()
    elif sys.argv[1] == "-i":
        study_help.interactive_mode()
    elif sys.argv[1] == "-r":
        if len(sys.argv) == 5:
            study_help.report_mode()
        else:
            raise Exception("\033[91mInvalid number of arguments for report mode. Please try again.\033[0m")
    else:
        raise Exception("\033[91mInvalid command line arguments for StudyHelp program.\033[0m")