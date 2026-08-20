package main

import (
"encoding/json"
"fmt"
"net"
"os"
"time"
)

type ScanResult struct {
Target     string   `json:"target"`
OpenPorts  []int    `json:"open_ports"`
Timestamp  string   `json:"timestamp"`
}

func main() {
if len(os.Args) < 2 {
tln("Usage: go run scanner.go <target_ip>")

}
target := os.Args[1]
ports := []int{21, 22, 80, 443, 3306, 3389, 8080}
var open []int

for _, p := range ports {
tf("%s:%d", target, p)
n, err := net.DialTimeout("tcp", address, 500*time.Millisecond)
nil {
 = append(open, p)
n.Close()
Result{
 target,
Ports: open,
ow().UTC().Format(time.RFC3339),
}
out, _ := json.MarshalIndent(res, "", "  ")
fmt.Println(string(out))
}
