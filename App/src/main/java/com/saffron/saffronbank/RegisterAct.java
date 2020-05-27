package com.saffron.saffronbank;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;



public class RegisterAct extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);//will hide the title

        ActionBar bar = getSupportActionBar();
        try{
            bar.hide();
        } catch (Exception e)
        {
        }
        setContentView(R.layout.activity_register);

        Button regBtn = findViewById(R.id.reg_btn);
        Button logBtn = findViewById(R.id.btn_log);


        regBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String url = getResources().getString(R.string.url);
                TextView email_tv = findViewById(R.id.reg_email);
                String email = email_tv.getText().toString();
                TextView pass_tv = findViewById(R.id.reg_pass);
                String pass = pass_tv.getText().toString();

                Uri uri = new Uri.Builder()
                        .scheme("https")
                        .authority(url)
                        .path("register")
                        .appendQueryParameter("email", email)
                        .appendQueryParameter("pword", pass)
                        .build();

                String[] arr = new String[10];
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
                        Utils.showText(getApplicationContext(), "Registered with succes");
                    }

                } catch (JSONException e) {
                    e.printStackTrace();
                }


            }

        });

        logBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(RegisterAct.this, LoginAct.class);
                startActivity(intent);
            }
        });
    }
}
