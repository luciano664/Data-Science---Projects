/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package retscannerxml;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

/**
 *
 * @author qlucisa
 */
public class SaveFile {

    public SaveFile() {
    }
    
    

    public void saveFile(String fileName, String text) {
        try {
            BufferedWriter outPutFile = new BufferedWriter(new FileWriter(fileName, false));
            outPutFile.write(text);
            outPutFile.flush();
            outPutFile.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

}
