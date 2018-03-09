/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package retscannerxml;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

/**
 *
 * @author qlucisa
 */
public class RetScannerXML {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try {
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            //Informamos qual arquivo xml vamos ler
            Document doc = db.parse(new InputSource(args[0]));
            //Criamos um objeto Element que vai receber as informacoes de doc
            Element raiz = doc.getDocumentElement();
            NodeList ruList = raiz.getElementsByTagName("ru");
            Element ruElement;
            Element portElement;
            Element aldElement;
            String text = "RU;PortId;unique_id\n";
            //Fazemos um for nas tags Telefone e adicionamos os dados
            //  em um objeto Telefone e depois na colecao
            for (int i = 0; i < ruList.getLength(); i++) {
                ruElement = (Element) ruList.item(i);
                NodeList portList = ruElement.getElementsByTagName("port");

                for (int j = 0; j < portList.getLength(); j++) {
                    portElement = (Element) portList.item(j);
                    NodeList aldList = portElement.getElementsByTagName("ald");
                    if (aldList.getLength() > 0) {
                        for (int k = 0; k < aldList.getLength(); k++) {
                            aldElement = (Element) aldList.item(k);
                            if (aldElement!=null){
                                text += ruElement.getAttribute("ldn")+";";
                                text += portElement.getAttribute("id")+";";
                                text += aldElement.getAttribute("unique_id")+"\n";
                            }
                        }
                    }
                }

            }
            System.out.println(text);
            SaveFile save = new SaveFile();
            save.saveFile(args[1], text);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}
