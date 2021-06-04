package data

import (
	"encoding/json"
	"io"
)

// "fmt"

// "time"

// defines structure for a stock with json struct tags
type Stock struct {
	CompanyName   string  `json:"company_name"`
	Ticker        string  `json:"ticker"`
	Price         float32 `json:"price"`
	EPS_forward   float32 `json:"EPS_forward"`
	EPS_trailing  float32 `json:"EPS_trailing"`
	PE_forward    float32 `json:"PE_forward"`
	PE_trailing   float32 `json:"PE_trailing"`
	Change        float32 `json:"change"`
	ChangePercent string  `json:"change_percent"`
	Dividend      float32 `json:"dividend"`
	DividendYield string  `json:"dividend_yield"`
	MarketCap     string  `json:"market_cap"`
	PrevClose     float32 `json:"prev_close"`
	Volume        int     `json:"volume"`
	WeightSP500   float32 `json:"weight_sp500"`
	YearHigh      float32 `json:"year_high"`
	YearLow       float32 `json:"year_low"`
	Datetime      string  `json:"datetime"`
}

func (s *Stock) ToJSON(w io.Writer) error {
	// encoder instead of marshal
	e := json.NewEncoder(w)
	return e.Encode(s)
}

func (s *Stock) FromJSON(r io.Reader) error {
	// decoder to open json
	e := json.NewDecoder(r)
	return e.Decode(s)
}
