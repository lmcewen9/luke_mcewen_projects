package subsitution_cipher;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class SubsitutionCipher {
    
    private static final Map<Character, Character> encryptMap = new HashMap<>();
    private static final Map<Character, Character> decryptMap = new HashMap<>();
    private static  Random random = new Random();

    static{
        for (int i = 32; i < 126; i++){
            int randomNum = random.nextInt(95) + 32;
            boolean done = false;
            while(!(done)){
                if (!(decryptMap.containsKey(((char)randomNum)))){
                    encryptMap.put((char)i, (char)randomNum);
                    decryptMap.put((char)randomNum, (char)i);
                    done = true;
                }
                else
                    randomNum = random.nextInt(95) + 32;
            }
        }
    }

    public String encrpyt(String plainText){
        String s = "";
        for (int i = 0; i < plainText.length(); i++)
            s += encryptMap.get(plainText.charAt(i));
        return s;
    }

    public String decrypt(String encryptedText){
        String s = "";
        for (int i = 0; i < encryptedText.length(); i++)
            s += decryptMap.get(encryptedText.charAt(i));
        return s;
    }

    public static void main(String[] args) {
        SubsitutionCipher cipher = new SubsitutionCipher();
        Scanner scanner = new Scanner(System.in);
        boolean done = false;
        while (!(done)){
            System.out.print("What is the text you would like to encrypt?: ");
            String plainText = scanner.nextLine();
            String encryptedText = cipher.encrpyt(plainText.strip());
            System.out.println("Here is your encrypted text: " + encryptedText);
            System.out.print("Would you like to decrypt it? y/n/exit: ");
            String yesornoDecrypt = scanner.nextLine();
            switch(yesornoDecrypt.strip().toLowerCase()){
                case "y":
                    System.out.println(cipher.decrypt(encryptedText));
                case "n":
                    break;
                case "exit":
                    done = true;
                    scanner.close();
                    break;
                default:
                    System.out.println("Not a valid command");
            }
        }

    }
}
