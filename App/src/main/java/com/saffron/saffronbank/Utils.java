package com.saffron.saffronbank;
import android.content.Context;
import android.widget.Toast;

public class Utils {

    public static void showText(Context context, String Text)
    {
        Toast.makeText(context, Text, Toast.LENGTH_LONG).show();
    }
}
