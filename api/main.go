package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
	"time"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

// db, err := sql.Open("mysql", "username:password@tcp(127.0.0.1:3306)/moonstock_api")

func main() {
	// create new logger
	l := log.New(os.Stdout, "moonstock-api", log.LstdFlags)

	// create router with Gorilla
	sm := mux.NewRouter()

	// TODO: SETUP SUBROUTER ENDPOINTS HERE

	// start server with our serve mux
	s := &http.Server{
		Addr:         ":9090",
		Handler:      sm,
		IdleTimeout:  120 * time.Second,
		ReadTimeout:  1 * time.Second,
		WriteTimeout: 1 * time.Second,
	}

	// go routine to run the server and catch error and won't block
	go func() {
		err := s.ListenAndServe()
		if err != nil {
			l.Fatal(err)
		}
	}()

	// signal channel
	sigChan := make(chan os.Signal)

	// listen for interrupt and kill signals
	signal.Notify(sigChan, os.Interrupt)
	signal.Notify(sigChan, os.Kill)

	sig := <-sigChan
	l.Println("Received terminate, graceful shutdown", sig)

	// graceful shutdown to finish work before cutting off after 30 seconds
	tc, _ := context.WithTimeout(context.Background(), 30*time.Second)
	s.Shutdown(tc)

}
