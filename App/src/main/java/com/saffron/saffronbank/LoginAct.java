package com.saffron.saffronbank;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

public class LoginAct extends AppCompatActivity {

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);//will hide the title
        ActionBar bar = getSupportActionBar();
        try{  bar.hide();} catch (Exception e){}

        setContentView(R.layout.first_run);
        Button loginButton = findViewById(R.id.loginButton);
        Button regBtn = findViewById(R.id.reg_btn);

        regBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(LoginAct.this, RegisterAct.class);
                startActivity(intent);
            }
        });

        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String url = getResources().getString(R.string.url);
                TextView email_tv = findViewById(R.id.log_email);
                String email = email_tv.getText().toString();
                TextView pass_tv = findViewById(R.id.log_pass);
                String pass = pass_tv.getText().toString();

                Uri uri = new Uri.Builder()
                        .scheme("https")
                        .authority(url)
                        .path("login")
                        .appendQueryParameter("email", email)
                        .appendQueryParameter("pword", pass)
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
                    }
                    if (sv_res.equals("good")){
                        SharedPreferences.Editor editor = getSharedPreferences("appdata", MODE_PRIVATE).edit();
                        editor.putString("use_email", email);
                        editor.putString("use_pass", pass);
                        editor.putBoolean("islogged", true);

                        String token = resultJson.getString("token");
                        editor.putString("token", token);
                        editor.commit();
                        Utils.showText(getApplicationContext(), "Logged in with succes");
                        Intent intent = new Intent(LoginAct.this, MenuActivity.class);
                        startActivity(intent);

                    }

                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        });
    }
}
