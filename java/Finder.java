import java.awt.Point;
import java.util.ArrayList;

public class Finder {

    static ArrayList<Point> getPossibleNextPositions(String[] mazearr, Point currentPosition){
        ArrayList<Point> possibleNextPositions = new ArrayList<Point>();
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
        ArrayList<Point> openPoints = new ArrayList<Point>();
        openPoints.add(new Point(0,0));
        ArrayList<Point> closedPoints = new ArrayList<Point>();

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
                 "....W.";

        System.out.println(a + "\n" + Finder.pathFinder(a) + "\n");
        System.out.println(b + "\n" + Finder.pathFinder(b) + "\n");
        System.out.println(c + "\n" + Finder.pathFinder(c) + "\n");
        System.out.println(d + "\n" + Finder.pathFinder(d) + "\n");
    }
}