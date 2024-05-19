from flask import Flask, request, jsonify
from supabase import create_client, Client

app = Flask(__name__)

url= ("https://guvwgjkzbgagntxyaweb.supabase.co")
key= ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd1dndnamt6YmdhZ250eHlhd2ViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTAzMDg3MDEsImV4cCI6MjAyNTg4NDcwMX0.PWy9_rvRQsMlvQ7BdTn2JqFAuUcNC-ZamIa2DasavT4")
supabase = create_client(url, key)

@app.route("/create", methods=["POST"])
def create_record():
    data = request.get_json()
    supabase.table("Dummy").insert(data).execute()
    return jsonify({"message": "Record created successfully"})

@app.route("/read", methods=["GET"])
def read_records():
    data = supabase.table("Dummy").select("*").execute()
    return(data.data)

@app.route("/update", methods=["PUT"])
def update_record():
    data = request.get_json()
    supabase.table("Dummy").update(data).eq("id", data["id"]).execute()
    return jsonify({"message": "Record updated successfully"})

@app.route("/delete", methods=["DELETE"])
def delete_record():
    data = request.get_json()
    supabase.table("Dummy").delete().eq("id", data["id"]).execute()
    return jsonify({"message": "Record deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)