package handlers

import (
	// "database/sql"
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

	// convert data to json

	// send json over

}
