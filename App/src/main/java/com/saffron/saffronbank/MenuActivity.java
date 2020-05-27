package com.saffron.saffronbank;

import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Window;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

public class MenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);//will hide the title
        ActionBar bar = getSupportActionBar();
        try{  bar.hide();} catch (Exception e){}

        setContentView(R.layout.activity_menu);
        SharedPreferences prefs = getSharedPreferences("appdata", MODE_PRIVATE);

        TextView utxt = findViewById(R.id.txt_mail);
        String email = prefs.getString("use_email", "error");

        TextView btxt = findViewById(R.id.txt_ballance);

        utxt.setText(email);
        int bal = balance();
        btxt.setText(String.valueOf(bal));

    }

    public int balance(){
        SharedPreferences prefs = getSharedPreferences("appdata", MODE_PRIVATE);
        SharedPreferences.Editor editor = getSharedPreferences("appdata", MODE_PRIVATE).edit();

        String url = getResources().getString(R.string.url);
        String token = prefs.getString("token", "None");

        if (token.equals("None"))
            return -1;


        Uri uri = new Uri.Builder()
                .scheme("https")
                .authority(url)
                .path("balance")
                .appendQueryParameter("token", token)
                .build();


        String[] arr = new String[2];
        arr[0] = uri.toString();
        ConHandle ch = new ConHandle();

        ch.execute(arr);

        String result = ch.getResult();
        while (result == "nimic")
            result = ch.getResult();



        try {
            JSONObject resultJson = new JSONObject(result);
            String sv_res = resultJson.getString("result");

            if (sv_res.equals("bad")){
                String error_text = resultJson.getString("error_text");
                Utils.showText(getApplicationContext(), error_text);
                return  -1;
            }

            if (sv_res.equals("good")){

                int balance = resultJson.getInt("balance");
                return balance;

            }

        } catch (JSONException e) {
            e.printStackTrace();
        }

        return 10;
    }
}
