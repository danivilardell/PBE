package com.example.coursemanager;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TableLayout;
import android.widget.TextView;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class PrincipalActivity extends AppCompatActivity {

    private String username;
    private String password;
    private String host;
    Button botologout;
    Button botosend;
    EditText buscador;
    TableLayout taula;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal);

        this.username = getIntent().getStringExtra("username");
        this.password = getIntent().getStringExtra("password");
        this.host = getIntent().getStringExtra("host");
        this.botologout = findViewById(R.id.botologout);
        this.botosend = findViewById(R.id.botosend);
        this.buscador = findViewById(R.id.buscador);
        this.taula = findViewById(R.id.taula);

        botologout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(intent);
            }
        });
        botosend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                datostaula();
            }
        });
    }

    private void datostaula() {
        String buscadorStr = this.buscador.getText().toString();
        String url;
        url="http://"+ this.host + ":8000/"+ buscadorStr + ".php/?userId=%27" + this.password + "%27";
        //EXEMPLE: url = "http://192.168.56.1:8000/marks.php/?userId=%27A2304D2%27";

        DataRequest dataRequest = new DataRequest(PrincipalActivity.this, url);
        dataRequest.response(url, new DataRequest.VolleyResponseListener() {
            @Override
            public void onResponse(JSONArray jsonObjectsArray) throws JSONException {
                creartaula(jsonObjectsArray,buscadorStr);
            }
            @Override
            public void onError(String message) {
                Toast.makeText(PrincipalActivity.this, "ERROR URL", Toast.LENGTH_SHORT).show();
            }
        });
    }
    protected void creartaula(JSONArray jsonArray, String idtaula) {
        try {
            View layout = null;

            switch (idtaula) {
                case "marks":
                    layout = LayoutInflater.from(this).inflate(R.layout.marksrow, null, false);
                    TextView as = layout.findViewById(R.id.assig);
                    TextView n = layout.findViewById(R.id.nom);
                    TextView notes = layout.findViewById(R.id.notes);

                    as.setTextColor(getResources().getColor(R.color.white));
                    n.setTextColor(getResources().getColor(R.color.white));
                    notes.setTextColor(getResources().getColor(R.color.white));
                    layout.setBackgroundColor(getResources().getColor(R.color.black));

                    as.setText("Subject");
                    n.setText("Name");
                    notes.setText("Mark");
                    taula.addView(layout);

                    for (int i = 0; i < jsonArray.length(); i++) {

                        JSONObject jsonObject = jsonArray.getJSONObject(i);
                        layout = LayoutInflater.from(this).inflate(R.layout.marksrow, null, false);
                        TextView as2 = layout.findViewById(R.id.assig);
                        TextView n2 = layout.findViewById(R.id.nom);
                        TextView notes2 = layout.findViewById(R.id.notes);
                        if (i % 2 == 0) {
                            layout.setBackgroundColor(getResources().getColor(R.color.clar));
                        } else {
                            layout.setBackgroundColor(getResources().getColor(R.color.fosc));
                        }
                        as2.setText(jsonObject.getString("subject"));
                        n2.setText(jsonObject.getString("name"));
                        notes2.setText(jsonObject.getString("mark"));
                        taula.addView(layout);
                    }
                    break;

                case "tasks":
                    layout = LayoutInflater.from(this).inflate(R.layout.tasksrow, null, false);
                    TextView data = layout.findViewById(R.id.data);
                    TextView assig = layout.findViewById(R.id.assig);
                    TextView nom = layout.findViewById(R.id.nom);

                    data.setTextColor(getResources().getColor(R.color.white));
                    assig.setTextColor(getResources().getColor(R.color.white));
                    nom.setTextColor(getResources().getColor(R.color.white));
                    layout.setBackgroundColor(getResources().getColor(R.color.black));

                    data.setText("Data");
                    assig.setText("Subject");
                    nom.setText("Name");
                    taula.addView(layout);

                    for (int i = 0; i < jsonArray.length(); i++) {
                        Log.e("arriba","aqui");
                        JSONObject jsonObject = jsonArray.getJSONObject(i);
                        layout = LayoutInflater.from(this).inflate(R.layout.tasksrow, null, false);
                        TextView data2 = layout.findViewById(R.id.data);
                        TextView assig2 = layout.findViewById(R.id.assig);
                        TextView nom2 = layout.findViewById(R.id.nom);
                        if (i % 2 == 0) {
                            layout.setBackgroundColor(getResources().getColor(R.color.clar));
                        } else {
                            layout.setBackgroundColor(getResources().getColor(R.color.fosc));
                        }

                        data2.setText(jsonObject.getString("Date"));
                        assig2.setText(jsonObject.getString("Subject"));
                        nom2.setText(jsonObject.getString("Name"));

                        taula.addView(layout);
                    }
                    break;

                case "timetable":
                    layout = LayoutInflater.from(this).inflate(R.layout.timetablerow, null, false);
                    TextView dia = layout.findViewById(R.id.dia);
                    TextView hora = layout.findViewById(R.id.hora);
                    TextView assig2 = layout.findViewById(R.id.assig);
                    TextView clas = layout.findViewById(R.id.classe);

                    dia.setTextColor(getResources().getColor(R.color.white));
                    hora.setTextColor(getResources().getColor(R.color.white));
                    assig2.setTextColor(getResources().getColor(R.color.white));
                    clas.setTextColor(getResources().getColor(R.color.white));
                    layout.setBackgroundColor(getResources().getColor(R.color.black));

                    dia.setText("Day");
                    hora.setText("Hour");
                    assig2.setText("Subject");
                    clas.setText("Room");
                    taula.addView(layout);

                    for (int i = 0; i < jsonArray.length(); i++) {

                        JSONObject jsonObject = jsonArray.getJSONObject(i);
                        layout = LayoutInflater.from(this).inflate(R.layout.timetablerow, null, false);
                        TextView dia2 = layout.findViewById(R.id.dia);
                        TextView hora2 = layout.findViewById(R.id.hora);
                        TextView assig3 = layout.findViewById(R.id.assig);
                        TextView clase2 = layout.findViewById(R.id.classe);
                        if (i % 2 == 0) {
                            layout.setBackgroundColor(getResources().getColor(R.color.clar));
                        } else {
                            layout.setBackgroundColor(getResources().getColor(R.color.fosc));
                        }
                        dia2.setText(jsonObject.getString("Day"));
                        hora2.setText(jsonObject.getString("Hour"));
                        assig3.setText(jsonObject.getString("Subject"));
                        clase2.setText(jsonObject.getString("Room"));

                        taula.addView(layout);
                    }
                    break;

            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}