Data: https://uofwaterloo-my.sharepoint.com/personal/jitoi_uwaterloo_ca/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjitoi%5Fuwaterloo%5Fca%2FDocuments%2FResult%20from%2031th%20Aug%202021%2FQRNG1%2FD1%2FRaw%20Data&ct=1639544325980&or=OWA%2DNT&cid=467d6d68%2Dbe1b%2Ddf2b%2D3e0e%2Dbae7a851897d

`D1_14.95MHz.txt`: length 1650124 (1 650 124)

serious typo: previuosly, line 111, `loss = nn.functional.mse_loss(reconstruction, past_seq)`

should be `loss = nn.functional.mse_loss(reconstruction, future_val)`?
