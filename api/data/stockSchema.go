package data

import (
	"encoding/json"
	"io"
)

// "fmt"

// "time"

// defines structure for a stock with json struct tags
type Stock struct {
	company_name   string  `json:"company_name"`
	ticker         string  `json:"ticker"`
	price          float32 `json:"price"`
	EPS_forward    float32 `json:"EPS_forward"`
	EPS_trailing   float32 `json:"EPS_trailing"`
	PE_forward     float32 `json:"PE_forward"`
	PE_trailing    float32 `json:"PE_trailing"`
	change         float32 `json:"change"`
	change_percent string  `json:"change_percent"`
	dividend       float32 `json:"dividend"`
	dividend_yield string  `json:"dividend_yield"`
	market_cap     string  `json:"market_cap"`
	prev_close     float32 `json:"prev_close"`
	volume         int     `json:"volume"`
	weight_sp500   float32 `json:"weight_sp500"`
	year_high      float32 `json:"year_high"`
	year_low       float32 `json:"year_low"`
	date_time      string  `json:"datetime"`
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
