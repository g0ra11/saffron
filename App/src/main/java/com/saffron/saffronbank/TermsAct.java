package com.saffron.saffronbank;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.widget.Button;

public class TermsAct extends AppCompatActivity {
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
        setContentView(R.layout.terms);
        Button agreeButton = findViewById(R.id.agreeButton);


        agreeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(TermsAct.this, RegisterAct.class);
                startActivity(intent);
            }
        });
    }
}
