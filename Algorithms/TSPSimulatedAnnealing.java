import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class TSPSimulatedAnnealing {

    static class Point {
        double x;
        double y;

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static double distance(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    }

    public static double calculateTotalDistance(Point[] coordinates, int[] path) {
        double totalDistance = 0;
        for (int i = 0; i < path.length - 1; i++) {
            totalDistance += distance(coordinates[path[i]], coordinates[path[i + 1]]);
        }
        totalDistance += distance(coordinates[path[path.length - 1]], coordinates[path[0]]);
        return totalDistance;
    }

    public static int[] simulatedAnnealingTSP(Point[] coordinates, double initialTemperature, double coolingRate) {
        Random random = new Random();
        int n = coordinates.length;
        int[] currentPath = new int[n];
        for (int i = 0; i < n; i++) {
            currentPath[i] = i;
        }
        int[] bestPath = Arrays.copyOf(currentPath, n);
        double currentEnergy = calculateTotalDistance(coordinates, currentPath);
        double bestEnergy = currentEnergy;

        double temperature = initialTemperature;

        ArrayList<Double> energies = new ArrayList<>(); 

        while (temperature > 1) {
            int randomIndex1 = random.nextInt(n);
            int randomIndex2 = random.nextInt(n);

            int[] newPath = Arrays.copyOf(currentPath, n);
            int temp = newPath[randomIndex1];
            newPath[randomIndex1] = newPath[randomIndex2];
            newPath[randomIndex2] = temp;

            double newEnergy = calculateTotalDistance(coordinates, newPath);

            if (newEnergy < currentEnergy) {
                currentPath = Arrays.copyOf(newPath, n);
                currentEnergy = newEnergy;
                if (newEnergy < bestEnergy) {
                    bestPath = Arrays.copyOf(currentPath, n);
                    bestEnergy = newEnergy;
                }
            } else {
                double acceptanceProbability = Math.exp((currentEnergy - newEnergy) / temperature);
                if (random.nextDouble() < acceptanceProbability) {
                    currentPath = Arrays.copyOf(newPath, n);
                    currentEnergy = newEnergy;
                }
            }

            energies.add(currentEnergy); 

            temperature *= 1 - coolingRate;
        }

        double sum = 0;
        double minEnergy = Double.MAX_VALUE;
        for (double energy : energies) {
            sum += energy;
            if (energy < minEnergy) {
                minEnergy = energy;
            }
        }
        double averageEnergy = sum / energies.size(); 

        System.out.println("Average TSP Cost: " + averageEnergy);
        System.out.println("Best TSP Cost: " + bestEnergy);
        return bestPath;
    }

    public static Point[] readCoordinatesFromFile(String filePath) throws FileNotFoundException {
        ArrayList<Point> coordinates = new ArrayList<>();
        Scanner scanner = new Scanner(new File(filePath));
        scanner.nextLine(); 
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split(" ");
            double x = Double.parseDouble(line[0]);
            double y = Double.parseDouble(line[1]);
            coordinates.add(new Point(x, y));
        }
        scanner.close();
        return coordinates.toArray(new Point[0]);
    }

    public static void main(String[] args) throws FileNotFoundException {
        String filePath = "PATH 3";
        Point[] coordinates = readCoordinatesFromFile(filePath);

        long startTime = System.currentTimeMillis();
        int[] tspPath = simulatedAnnealingTSP(coordinates, 10000, 0.003);
        long endTime = System.currentTimeMillis();
        double elapsedTime = (endTime - startTime) / 1000.0; 

        System.out.print("TSP Path: ");
        for (int i : tspPath) {
            System.out.print(i + " ");
        }
        System.out.println("\nElapsed Time: " + elapsedTime + " seconds");
    }
}
