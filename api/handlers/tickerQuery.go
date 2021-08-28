package handlers

import (
	"database/sql"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
	// "github.com/wchen777/moonstock-api/data"
)

type APILogger struct {
	l *log.Logger
}

// instantiate instance of this handler
func NewStockLogger(l *log.Logger) *APILogger {
	return &APILogger{l}
}

func tickerDataMostRecent(rw http.ResponseWriter, r *http.Request) {

	// query database
	db, err := sql.Open("mysql", "username:password@tcp(127.0.0.1:3306)/moonstock_api")

	if err != nil {
		panic(err)
	}

	defer db.Close()

	// perform a db.Query
	queryResults, err := db.Query("SELECT * FROM stocks WHERE (date_time = (SELECT MAX(date_time) FROM stocks));")

	// if there is an error inserting, handle it
	if err != nil {
		panic(err.Error())
	}

	// convert data to json

	// send json over

}
