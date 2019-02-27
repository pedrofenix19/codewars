import java.awt.Point;
import java.util.LinkedList;

public class Finder {

    static LinkedList<Point> getPossibleNextPositions(String[] mazearr, Point currentPosition){
        LinkedList<Point> possibleNextPositions = new LinkedList<Point>();
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
        LinkedList<Point> openPoints = new LinkedList<Point>();
        openPoints.add(new Point(0,0));
        LinkedList<Point> closedPoints = new LinkedList<Point>();

        while (openPoints.size() > 0) {
            Point currentPoint = openPoints.remove(0);
            LinkedList<Point> possibleNextPoints = getPossibleNextPositions(mazearr, currentPoint);

            for (Point p : possibleNextPoints) {
                if(p.x == n -1 && p.y == n - 1) return true;
            }

            for (Point p : possibleNextPoints) {
                if(!closedPoints.contains(p) && !openPoints.contains(p)) openPoints.add(p);
            }
            closedPoints.add(currentPoint);
        }
        return false;
    }

    public static void main(String[] args){
        Point p1 = new Point(1,2);
        Point p2 = new Point(2,1);
        System.out.println(p1 > p2);
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

        long startTime = System.nanoTime();

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

        long endTime = System.nanoTime();

        System.out.println("Execution time is " + (endTime - startTime) / 1000d + " seconds");

    }
}