package subsitution_cipher;

public class CeaserCipher{

    public static char positionLetter(char letter, int position){
        if((int)letter + position > 122){
            int excess = ((int)letter + position) - 122;
            int new_letter = 96 + excess;
            return (char)new_letter;
        }
        else{
            int ascii = (int)letter + position;
            return (char)ascii;
        }
    }

    public static int randomPosition(){
        return (int) (Math.random() * (26-1) + 1);
    }

    public static String buildCipher(String str, int position_move){
        String cipher = "";
        for(int i = 0; i < str.length(); i++){
            cipher += positionLetter(str.charAt(i), position_move);
        }
        System.out.println(position_move);
        return cipher;
    }
    public static void main(String[] args){
        System.out.println(buildCipher("Luke", randomPosition()));
    }
}