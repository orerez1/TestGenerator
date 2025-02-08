package org.testGenerator;

import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import com.intellij.openapi.ui.Messages;
import com.intellij.openapi.vfs.VirtualFile;
import org.jetbrains.annotations.NotNull;
import org.junit.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.File;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import static com.intellij.openapi.actionSystem.CommonDataKeys.VIRTUAL_FILE;

public class GenerateTestsClass extends AnAction {

    public String getBasicScriptPathBasedOnOS() {
        // todo: make better paths
        String osName = System.getProperty("os.name").toLowerCase();
        String basePath;
        if (osName.contains("win")) {
            basePath = "C:\\Program Files";
        } else if (osName.contains("mac")) {
            basePath = "/Users";
        } else if (osName.contains("nix") || osName.contains("nux") || osName.contains("aix")) {
            basePath = "/home";
        } else {
            basePath = "";
            System.out.println("Operating system not recognized.");
        }

        return basePath;
    }

    public String getPathSeparatorBasedOnOS() {
        return System.getProperty("os.name").toLowerCase().contains("win") ? "\\":"/";
    }

    public String getScriptPath() {
        String scriptProject = "TestGenerator";
        String scriptFile = "main.py";
        String separator = getPathSeparatorBasedOnOS();

        return getBasicScriptPathBasedOnOS() + separator + scriptProject + separator + scriptFile;
    }
    @Override
    public void actionPerformed(@NotNull AnActionEvent e) {
        VirtualFile file = e.getData(VIRTUAL_FILE);

        if (file == null) {
            return;
        }

        try {
            String scriptPath = getScriptPath();

            // Create a process builder to run the Python script
            ProcessBuilder processBuilder = new ProcessBuilder("python", scriptPath, file.getCanonicalPath());
            processBuilder.redirectErrorStream(true);

            // Start the process
            Process process = processBuilder.start();


            // Read and store the output for easier testing and maintenance
            List<String> outputLines = new ArrayList<>();
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    outputLines.add(line);
                    System.out.println("Python output: " + line);
                }
            }


            // Wait for the process to complete
            int exitCode = process.waitFor();
            System.out.println("Exit code: " + exitCode);

            // Print all collected output
            System.out.println("\nComplete output:");
            outputLines.forEach(System.out::println);
            if (exitCode != 0) {
                Messages.showErrorDialog("Python script exited with code: " + exitCode, "Error");
                return;
            }

            Messages.showInfoMessage("Tests successfully generated", "Action Results");

        } catch (IOException | InterruptedException ex) {
            Messages.showErrorDialog("An error occurred while running the Python script: " + ex.getMessage(), "Error");
        }

    }

    @Test
    public void test() {
        String fileName = "C:/Users/orkin/IdeaProjects/Testing/src/Exampleton.java";
        System.out.println(fileName);

        try {
            // Get the project root directory
            String projectRoot = new File("").getAbsolutePath();

            String scriptPath = getScriptPath();

            // Create a process builder to run the Python script
            ProcessBuilder processBuilder = new ProcessBuilder("python ", scriptPath, fileName);
            processBuilder.redirectErrorStream(true);

            // Start the process
            Process process = processBuilder.start();

            // Read and store the output
            List<String> outputLines = new ArrayList<>();
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    outputLines.add(line);
                    System.out.println("Python output: " + line);
                }
            }

            int exitCode = process.waitFor();
            System.out.println("Exit code: " + exitCode);

            // Print all collected output
            System.out.println("\nComplete output:");
            outputLines.forEach(System.out::println);
        } catch (Exception e) {
            System.out.println("fail");
        }
    }
}
