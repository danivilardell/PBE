package com.example.coursemanager;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONException;

public class MainActivity extends AppCompatActivity {
    EditText host;
    EditText username;
    EditText password;
    Button loginbtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.host = (EditText) findViewById(R.id.host);
        this.username = (EditText) findViewById(R.id.username);
        this.password = (EditText) findViewById(R.id.password);
        this.loginbtn= (Button) findViewById(R.id.loginbtn);

        loginbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                validateUser();
            }
        });
    }

    private void validateUser(){
        DataRequest dataRequest=new DataRequest(MainActivity.this, this.host.getText().toString());
        dataRequest.response("http://"+ this.host.getText().toString()+":8000/index.php/?userId=%27"+this.password.getText().toString()+"%27", new DataRequest.VolleyResponseListener() {

            @Override
            public void onError(String message) {
                Toast.makeText(MainActivity.this, "ERROR", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onResponse(JSONArray jsonObjectsArray) throws JSONException {
                Intent intent=new Intent(MainActivity.this,PrincipalActivity.class);
                intent.putExtra("host", host.getText().toString());
                intent.putExtra("username", username.getText().toString());
                intent.putExtra("password", password.getText().toString());
                startActivity(intent);
                finish();
            }
        });
    }

}