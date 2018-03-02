import javax.swing.text.html.HTMLDocument;
import java.io.*;
import java.util.*;

public class Testing {
    public static int cordinateX = 0;
    public static int cordinateY = 0;
    public static Hashtable result;
    public static int vehicleCount = 0;
    public static int step, steps;

    public static void main(String[] args){
        result = new Hashtable<String,ArrayList<Integer>>();
        //Readers and Writers
        BufferedReader reader = null;
        BufferedWriter writer = null;
        int ride = 0;
        //int rideCount = 0;
        int r, c, vehicle, rides, bonus;
        int x1, x2, y1, y2, start, finish;
        try {
            reader = new BufferedReader(new FileReader(new File("c:/users/mahome/desktop/a_example.in")));
            writer = new BufferedWriter(new FileWriter(new File("testouput.txt"),
                    false));

            //Computational logic goes here.
            StringTokenizer token = new StringTokenizer(reader.readLine()," ");
            r = Integer.parseInt(token.nextToken());
            c = Integer.parseInt(token.nextToken());
            vehicle = Integer.parseInt(token.nextToken());
            rides = Integer.parseInt(token.nextToken());
            bonus = Integer.parseInt(token.nextToken());
            steps = Integer.parseInt(token.nextToken());

            //Loop process through the rides
            while(ride < rides){
                token = new StringTokenizer(reader.readLine(), " ");
                x1 = Integer.parseInt(token.nextToken());
                y1 = Integer.parseInt(token.nextToken());
                x2 = Integer.parseInt(token.nextToken());
                y2 = Integer.parseInt(token.nextToken());
                start = Integer.parseInt(token.nextToken());
                finish = Integer.parseInt(token.nextToken());

                rider(x1,y1,x2,y2,start,finish,ride);
                if(vehicleCount < vehicle -1){
                    vehicleCount++;
                }else{
                    vehicleCount = 0;
                }
                ride++;
                //maintain vehicle count


            }


            //outputting
            Enumeration<ArrayList> values = result.elements();
            while(values.hasMoreElements()){
                ArrayList<Integer> vehicleRider = values.nextElement();
                writer.write(String.valueOf(vehicleRider.size()));
                writer.write(" ");
                Iterator<Integer> it = vehicleRider.iterator();
                String rd = "";
                while(it.hasNext()){
                    rd += it.next().toString()+" ";
                }
                System.out.println(result.toString());
                writer.write(rd.trim());
                writer.newLine();

            }





            //Close the object after reading
            reader.close();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //The rider route
    public static void rider(int x1, int y1, int x2, int y2, int start, int stop, int rider){
        Testing.cordinateX = 0;
        Testing.cordinateY = 0;
        Testing.step = 0;
        ArrayList<Integer> ridee = new ArrayList<>();
        ridee.add(rider);
        if(result.containsKey("vehicle"+vehicleCount)){
            ridee = (ArrayList<Integer>) result.get("vehicle"+vehicleCount);
            ridee.add(rider);
            result.remove("vehicle"+vehicleCount);
            result.put("vehicle"+vehicleCount,ridee);
        }else {
            result.put("vehicle" + vehicleCount, ridee);
        }
        movex(x2,y2);

    }

    //Row walker
    public static void movex(int finishX, int finishY){
        if(Testing.step >= steps){
            return;
        }
        if(Testing.cordinateX <= finishX){
            Testing.cordinateX++;
            Testing.step++;
            movex(finishX, finishY);


        }else if(Testing.cordinateY <= finishY){
            movey(finishX,finishY);
        }
    }

    //column walker
    public static void movey(int finishX, int finishY){
        if(Testing.step >= steps){
           return;
        }
        if(Testing.cordinateY <= finishY){
            Testing.cordinateY++;
            Testing.step++;
            movey(finishX, finishY);
        }else if(Testing.cordinateY <= finishX){
            movex(finishX,finishY);
        }
    }
}
