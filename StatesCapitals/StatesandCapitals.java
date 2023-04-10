package statescapitals;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class StatesandCapitals {
    
    private HashMap<String, String> gameMap;
    private int score;
    private Random random;

    public StatesandCapitals(){
        gameMap = new HashMap<>();
        gameMap.put("New York", "Albany");
        gameMap.put("California", "Sacremento");
        gameMap.put("Arizona", "Phoenix");
        gameMap.put("Florida", "Tallahassee");
        gameMap.put("Indiana", "Indianapolis");
        gameMap.put("Oregon", "Salem");
        gameMap.put("Colorado", "Denver");
        gameMap.put("Wyoming", "Cheyenne");
        gameMap.put("Texas", "Austin");
        gameMap.put("New Jersey", "Trenton");
        gameMap.put("Nevada", "Carson City");
        gameMap.put("Alaska", "Juneau");
        gameMap.put("Tennessee", "Nashville");
        gameMap.put("Delware", "Dover");
        gameMap.put("Massachusetts", "Boston");
        gameMap.put("Iowa", "Des Moines");
        gameMap.put("Montana", "Helena");
        gameMap.put("Illinois", "Springfield");
        gameMap.put("Oklahoma", "Oklahoma City");
        gameMap.put("Louisana", "Baton Rouge");
        gameMap.put("North Dakota", "Bismarck");
        gameMap.put("Arkansas", "Little Rock");
        gameMap.put("New Mexico", "Santa Fe");
        gameMap.put("Utah", "Salt Lake City");
        gameMap.put("North Carolina", "Raleigh");
        gameMap.put("Alabama", "Montgomery");
        gameMap.put("Pennsylvania", "Harrisburg");
        gameMap.put("South Dakota", "Pierre");
        gameMap.put("Kentucky", "Frankfort");
        gameMap.put("Maryland", "Annapolis");
        gameMap.put("Vermont", "Montpelier");
        gameMap.put("Ohio", "Columbus");
        gameMap.put("Kansas", "Topeka");
        gameMap.put("Rhode Island", "Providence");
        gameMap.put("Hawaii", "Honolulu");
        gameMap.put("Virgina", "Richmond");
        gameMap.put("Michigan", "Lansing");
        gameMap.put("Idaho", "Boise");
        gameMap.put("Missouri", "Jefferson City");
        gameMap.put("Connecticut", "Hartford");
        gameMap.put("West Virgina", "Charleston");
        gameMap.put("Wisconsin", "Madison");
        gameMap.put("Minnesota", "St Paul");
        gameMap.put("New Hampshire", "Concord");
        gameMap.put("South Carolina", "Columbia");
        gameMap.put("Maine", "Augusta");
        gameMap.put("Nebraska", "Lincoln");
        gameMap.put("Washington", "Olympia");
        gameMap.put("Georgia", "Atlanta");
        gameMap.put("Mississippi", "Jackson");

        score = 0;
        random = new Random();
    }

    public int size(){return gameMap.size();}

    public int getScore(){return score;}

    public String getCapital(String state){return gameMap.get(state);}

    public String getState(List<String> list){
        String state = list.get(random.nextInt(list.size()));
        list.remove(state);
        return state;
    }

    public ArrayList<String> toArray(){
        ArrayList<String> strArr = new ArrayList<>();
        for (String s : gameMap.keySet()){
            strArr.add(s);
        }
        return strArr;
    }

    public boolean check(String check, String state){
        if (check.strip().toLowerCase().equals(getCapital(state).strip().toLowerCase())){
            score++;
            return true;
        }
        return false;
    }

    public static void main(String[] args){
        StatesandCapitals game = new StatesandCapitals();
        ArrayList<String> gameArr = game.toArray();
        Scanner scanner = new Scanner(System.in);
        for(int i = 0; i < game.size(); i++){
            String state = game.getState(gameArr);
            System.out.print("What is the capital of " + state + "?: ");
            String check = scanner.nextLine();
            if (game.check(check, state)){
                System.out.println("Correct! Score=" + game.getScore());
            }
            else{
                System.out.println("Incorrect! It was " + game.getCapital(state));
                System.out.println("You suck at this game. Score=" + game.getScore());
            }
        }
        scanner.close();
    }
}
