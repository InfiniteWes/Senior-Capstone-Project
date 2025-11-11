from functions import inputFile

if __name__ == '__main__':
    running = True
    file = None
    fileName = None

    print("-----------------------------------------")
    print("YapGPT - TCP Anomaly Detection System")
    print("-----------------------------------------")
    if fileName is None:
        print("[1] Upload Network Log File")
    else:
        print(f"[1] Upload Network Log File - {fileName}")
    print("[2] Run TCP Handshake Analysis")
    print("[3] View Detected Anomalies")
    print("[4] Export Results")
    print("[5] Exit")
    print("-----------------------------------------")  

    while(running):
        choice = input("Enter your choice (M to see menu): ").lower().strip()

        if choice == "m":
            print("-----------------------------------------")
            print("YapGPT - TCP Anomaly Detection System")
            print("-----------------------------------------")
            if fileName is None:
                print("[1] Upload Network Log File")
            else:
                print(f"[1] Upload Network Log File - {fileName}")
            print("[2] Run TCP Handshake Analysis")
            print("[3] View Detected Anomalies")
            print("[4] Export Results")
            print("[5] Exit")
            print("-----------------------------------------")
            continue

        
        if choice == '1':
            file, fileName = inputFile(file, fileName)
        elif choice == '2':
            print("Analysing................................................................")
        elif choice == '3':
            print("Displaying Results")
        elif choice == '4':
            print("Exporting Results")
        elif choice == '5':
            print("Exiting program.")
            running = False
        else:
            print("Invalid input.")


    