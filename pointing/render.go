package pointing

import "net/http"

type NextPasses []*NextPassReply

func (nps *NextPasses) Render(w http.ResponseWriter, r *http.Request) error {
	return nil
}
