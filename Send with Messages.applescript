property appleID : "yourAppleID"
property path_to_python : "/usr/bin/python"
property path_to_qs_messages : "/Users/[username]/path/to/qs_messages.py"
property abs_path_to_messages_phonebook : "/Users/[username]/path/to/messages_phonebook.txt"

(*
See post at: http://n8henrie.com/2013/04/send-imessage-messages-with-quicksilver
Version 2 of the script at: http://n8henrie.com/2013/06/send-imessages-with-quicksilver-v2/

Send an iMessage to a buddy with Quicksilver. 
 
Install by placing in ~/Library/Application Support/Quicksilver/Actions and restarting Quicksilver
First pane: type text to send.
Second pane: choose this action. 
Third pane: pick buddy (iMessage number, iMessage email address, or their name if you've put it with their number into messages_phonebook.txt)
 *)

using terms from application "Quicksilver"
  on get direct types
		return {"NSStringPboardType"}
	end get direct types
	
	on get indirect types
		return {"qs.contact.phone", "qs.contact.email"}
	end get indirect types
	
	on process text firstPane with thirdPane
		
		if appleID is "yourAppleID" then
			display dialog "You need to open the \"Send with Messages\" Action script and set your Apple ID. Exiting."
			return
		else
			
			-- If the python part is set up...					
			try
				set the_command to path_to_python & " " & path_to_qs_messages & " " & quoted form of thirdPane & " " & quoted form of abs_path_to_messages_phonebook
				set thirdPane to do shell script the_command
			end try
			
			try
				tell application "Messages"
					
					tell (first service whose (service type is iMessage and name is ("E:" & appleID)))
						log in
						
						send firstPane to buddy thirdPane
						
					end tell
					
				end tell
				
			on error a number b
				activate
				display dialog a with title "error with your QS action script"
			end try
		end if
	end process text
	
	on get argument count
		return 2
	end get argument count
	
end using terms from