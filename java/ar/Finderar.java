import java.util.ArrayList;

public class Finderar {

    static ArrayList<int[]> getPossibleNextPositions(String[] mazearr, int[] currentPosition){
        ArrayList<int[]> possibleNextPositions = new ArrayList<int[]>(4);
        int n = mazearr.length;

        //if can move down
        if(currentPosition[0] < n - 1 && mazearr[currentPosition[0] + 1].charAt(currentPosition[1]) != 'W'){
            possibleNextPositions.add(new int[]{currentPosition[0] + 1, currentPosition[1]});
        }

        //if can move right
        if(currentPosition[1] < n - 1 && mazearr[currentPosition[0]].charAt(currentPosition[1] + 1) != 'W'){
            possibleNextPositions.add(new int[]{currentPosition[0], currentPosition[1] + 1});
        }

        //if can move left
        if(currentPosition[1] > 0 && mazearr[currentPosition[0]].charAt(currentPosition[1] - 1) != 'W'){
            possibleNextPositions.add(new int[]{currentPosition[0], currentPosition[1] - 1});
        }

        //if can move up
        if(currentPosition[0] > 0 && mazearr[currentPosition[0] - 1].charAt(currentPosition[1]) != 'W'){
            possibleNextPositions.add(new int[]{currentPosition[0] - 1, currentPosition[1]});
        }

        return possibleNextPositions;
    }

    static boolean pointIsInArray(ArrayList<int[]> list, int[] point){
        for(int[] p: list){
            if(p[0] == point[0] && p[1] == point[1]) return true;
        }
        return false;
    }

    
    static boolean pathFinder(String maze) {
        String[] mazearr = maze.split("\n");
        int n = mazearr.length;
        if(n == 1) return true;
        ArrayList<int[]> openPoints = new ArrayList<int[]>(n * n);
        openPoints.add(new int[]{0,0});
        ArrayList<int[]> closedPoints = new ArrayList<int[]>(n * n);

        while (openPoints.size() > 0) {
            int[] currentPoint = openPoints.remove(0);
            ArrayList<int[]> possibleNextPoints = getPossibleNextPositions(mazearr, currentPoint);

            for (int[] p : possibleNextPoints) {
                if(p[0] == n -1 && p[1] == n - 1) return true;
            }

            for (int[] p : possibleNextPoints) {
                if(!pointIsInArray(closedPoints,p) && !pointIsInArray(closedPoints,p)) openPoints.add(p);
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

        System.out.println(Finderar.pathFinder(a));
        System.out.println(Finderar.pathFinder(b));
        System.out.println(Finderar.pathFinder(c));
        System.out.println(Finderar.pathFinder(d));
        System.out.println(Finderar.pathFinder(e));
        System.out.println(Finderar.pathFinder(f));
        System.out.println(Finderar.pathFinder(g));
        System.out.println(Finderar.pathFinder(h));
        System.out.println(Finderar.pathFinder(i));
        System.out.println(Finderar.pathFinder(j));

        long endTime = System.currentTimeMillis();

        System.out.println("Execution time is " + (endTime - startTime) + " seconds");

    }
}