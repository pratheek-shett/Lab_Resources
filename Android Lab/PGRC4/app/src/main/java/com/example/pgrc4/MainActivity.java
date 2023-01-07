package com.example.pgrc4;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class MainActivity extends AppCompatActivity {
    Button threadBtn1,threadBtn2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        threadBtn1 = findViewById(R.id.thread_1);
        threadBtn2 = findViewById(R.id.thread_2);

        threadBtn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                createThread(threadBtn1);
            }
        });
        threadBtn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                createThread(threadBtn2);
            }
        });
    }
    public void createThread(Button threadBtn1) {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0;i<=10;i++) {
                    try {
                        int temp = i;
                        threadBtn1.post(new Runnable() {
                            @Override
                            public void run() {
                                threadBtn1.setText(String.valueOf(temp));
                            }
                        });
                        Thread.sleep(1000);
                    }catch(InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
        t1.start();
    }
}