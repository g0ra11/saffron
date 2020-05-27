package com.saffron.saffronbank;

import android.app.Activity;
import android.app.KeyguardManager;
import android.content.Intent;
import android.content.SharedPreferences;
import android.hardware.fingerprint.FingerprintManager;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;
import android.hardware.fingerprint.FingerprintManager;
import android.Manifest;
import android.os.Build;
import android.os.Bundle;
import android.security.keystore.KeyGenParameterSpec;
import android.security.keystore.KeyPermanentlyInvalidatedException;
import android.security.keystore.KeyProperties;
import android.support.v7.app.AppCompatActivity;
import android.support.v4.app.ActivityCompat;
import android.widget.TextView;
import java.io.IOException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.UnrecoverableKeyException;
import java.security.cert.CertificateException;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        requestWindowFeature(Window.FEATURE_NO_TITLE);//will hide the title
        ActionBar bar = getSupportActionBar();
        try{
            bar.hide();
        } catch (Exception e)
        {
        }

        super.onCreate(savedInstanceState);
        SharedPreferences.Editor editor = getSharedPreferences("appdata", MODE_PRIVATE).edit();
        SharedPreferences prefs = getSharedPreferences("appdata", MODE_PRIVATE);

        boolean firstr = prefs.getBoolean("first_run", true);

        if (firstr){
            editor.putBoolean("first_run", false);
            editor.apply();
            Intent intent = new Intent(MainActivity.this, TermsAct.class);
            startActivity(intent);
            return;
        }

        boolean islogged = prefs.getBoolean("islogged", false);
        if (!islogged){
            Intent intent = new Intent(MainActivity.this, LoginAct.class);
            startActivity(intent);
            return;
        }
        else{
            Intent intent = new Intent(MainActivity.this, FingerAct.class);
            startActivity(intent);
        }
    }

}
