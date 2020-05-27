package com.saffron.saffronbank;

import android.os.AsyncTask;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class ConHandle extends AsyncTask {

    private String result = "nimic";

    @Override
    protected String doInBackground(Object[] objects) {
        URL requ = null;
        String urlstr = (String)objects[0];
        try {
            requ = new URL(urlstr);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        HttpURLConnection urlConnection = null;
        try {
            urlConnection = (HttpURLConnection) requ.openConnection();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());

            BufferedReader r = new BufferedReader(new InputStreamReader(in));
            StringBuilder total = new StringBuilder();
            for (String line; (line = r.readLine()) != null; ) {
                total.append(line).append('\n');
            }
            result = total.toString();

//            Utils.showText(getApplicationContext(), total.toString());
//                    JsonReader reader = new JsonReader(new InputStreamReader(in, "UTF-8"));
//
//                    String result = reader.toString();
//                    Utils.showText(getApplicationContext(), result);

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            urlConnection.disconnect();
        }
        return "nimic";
    }

    public String getResult() {
        return result;
    }
}

