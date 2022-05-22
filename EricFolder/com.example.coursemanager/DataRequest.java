package com.example.coursemanager;

import android.content.Context;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;

public class DataRequest {
    private Context context;
    private String url;

    public DataRequest(Context context, String url) {
        this.context = context;
        this.url = url;
    }

    public interface VolleyResponseListener {
        void onError(String message);

        void onResponse(JSONArray jsonObjectsArray) throws JSONException;

    }

    public void response(String url, VolleyResponseListener volleyResponseListener) {
        RequestQueue queue = Volley.newRequestQueue(context);

        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        try {
                            volleyResponseListener.onResponse(response);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        volleyResponseListener.onError(error.toString());
                    }
                }
        );
        queue.add(jsonArrayRequest);
    }

}
