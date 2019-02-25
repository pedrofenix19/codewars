import java.awt.Point;
import java.util.ArrayList;

public class Finder {

    static ArrayList<Point> getPossibleNextPositions(String[] mazearr, Point currentPosition){
        ArrayList<Point> possibleNextPositions = new ArrayList<Point>(4);
        int n = mazearr.length;

        //if can move down
        if(currentPosition.x < n - 1 && mazearr[currentPosition.x + 1].charAt(currentPosition.y) != 'W'){
            possibleNextPositions.add(new Point(currentPosition.x + 1, currentPosition.y));
        }

        //if can move right
        if(currentPosition.y < n - 1 && mazearr[currentPosition.x].charAt(currentPosition.y + 1) != 'W'){
            possibleNextPositions.add(new Point(currentPosition.x, currentPosition.y + 1));
        }

        //if can move left
        if(currentPosition.y > 0 && mazearr[currentPosition.x].charAt(currentPosition.y - 1) != 'W'){
            possibleNextPositions.add(new Point(currentPosition.x, currentPosition.y - 1));
        }

        //if can move up
        if(currentPosition.x > 0 && mazearr[currentPosition.x - 1].charAt(currentPosition.y) != 'W'){
            possibleNextPositions.add(new Point(currentPosition.x - 1, currentPosition.y));
        }

        return possibleNextPositions;
    }

    
    static boolean pathFinder(String maze) {
        String[] mazearr = maze.split("\n");
        int n = mazearr.length;
        if(mazearr[n-1].endsWith("W")) return false;
        ArrayList<Point> openPoints = new ArrayList<Point>(n * n);
        openPoints.add(new Point(0,0));
        ArrayList<Point> closedPoints = new ArrayList<Point>(n * n);

        while (openPoints.size() > 0) {
            Point currentPoint = openPoints.remove(0);
            ArrayList<Point> possibleNextPoints = getPossibleNextPositions(mazearr, currentPoint);

            for (Point p : possibleNextPoints) {
                if(p.x == n -1 && p.y == n - 1) return true;
            }

            for (Point p : possibleNextPoints) {
                if(!closedPoints.contains(p)) openPoints.add(p);
            }
            closedPoints.add(currentPoint);
        }
        return false;
    }

    public static void main(String[] args){
        String a = ".W.\n"+
                 ".W.\n"+
                 "...",
               
             b = ".W.\n"+
                 ".W.\n"+
                 "W..",
               
             c = "......\n"+
                 "......\n"+
                 "......\n"+
                 "......\n"+
                 "......\n"+
                 "......",
               
             d = "......\n"+
                 "......\n"+
                 "......\n"+
                 "......\n"+
                 ".....W\n"+
                 "....W.",

            e =  ".W....\n"+
                 ".W.WW.\n"+
                 ".W.W..\n"+
                 ".W.W.W\n"+
                 ".W.W..\n"+
                 "...W..",

            f =  ".W....\n"+
                 ".W.WW.\n"+
                 ".W.W..\n"+
                 ".W.W.W\n"+
                 ".W.W..\n"+
                 "...W.W",

            g = "..W...W.W \n"+
            "..WW..WWW \n"+
            ".....W... \n"+
            ".W..W.... \n"+
            "W....WWWW \n"+
            ".......W. \n"+
            "..W...... \n"+
            "WW.WW..WW \n"+
            ".....W...",


            h = ".W...W...W...\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                ".W.W.W.W.W.W.\n" +
                "...W...W...W.",

            i = ".W...W...W...\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                ".W.W.W.W.W.W.\n"+
                "...W...W...W.",
            
            j = ".............\n"+
                "WWWWWWWWWWWW.\n"+
                ".............\n"+
                ".WWWWWWWWWWWW\n"+
                ".............\n"+
                "WWWWWWWWWWWW.\n"+
                "......W......\n"+
                ".WWWWWWWWWWWW\n"+
                ".............\n"+
                "WWWWWWWWWWWW.\n"+
                ".............\n"+
                ".WWWWWWWWWWWW\n"+
                ".............";

        long startTime = System.currentTimeMillis();

        System.out.println(Finder.pathFinder(a));
        System.out.println(Finder.pathFinder(b));
        System.out.println(Finder.pathFinder(c));
        System.out.println(Finder.pathFinder(d));
        System.out.println(Finder.pathFinder(e));
        System.out.println(Finder.pathFinder(f));
        System.out.println(Finder.pathFinder(g));
        System.out.println(Finder.pathFinder(h));
        System.out.println(Finder.pathFinder(i));
        System.out.println(Finder.pathFinder(j));

        long endTime = System.currentTimeMillis();

        System.out.println("Execution time is " + (endTime - startTime) / 1000d + " seconds");

    }
}