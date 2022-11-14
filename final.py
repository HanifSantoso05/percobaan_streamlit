import streamlit as st
import re
import pandas as pd 


st.title("""Aplikasi Pemecahan masalah Knapsack""")
st.write("""Menggunakan optimasi algoritma greedy""")

convert_list = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]

n = profit = st.text_input("Masukkan jumlah itemnya(n) :")
n = convert_list(n)

profit = st.text_input("Masukkan jumlah profit(p) dari setiap itemnya :")
profit = convert_list(profit)

weight = st.text_input("Masukkan jumlah weight(w) dari setiap itemnya :")
weight = convert_list(weight)

m = int(st.number_input("Masukkan kapasitas maksimum berat yang dapat di tampung(m) :",0))

submit = st.button("submit")

if submit:
    def fractional_knapsack(profit, weight,m):
        # Membuat variable index untuk mengambil penjang dari items nya
        index = list(range(len(n)))

        # Membuat variable ratio dimana inputan profit dibagi dengan inputan weight atau nilai P/W
        ratio = [p/w for p, w in zip(profit, weight)]
        
        # Kemudian index di urutkan berdasarkan ratio antara profit dan weight yang di urutkan secara menurun
        index.sort(key=lambda i: ratio[i], reverse=True)
 
        maksimum_profit = 0
        pecahan = [0]*len(profit)
        for i in index:
            if weight[i] <= m:
                pecahan [i] = 1
                maksimum_profit += profit[i]
                m -= weight[i]
            else:
                pecahan [i] = m/weight[i]
                maksimum_profit += profit[i]*m/weight[i]
                break

        return maksimum_profit, pecahan, ratio


    maksimum_profit, pecahan, ratio = fractional_knapsack(profit, weight, m)

    df = pd.DataFrame({
        'item': n,
        'Profit': profit,
        'Weight': weight,
        'P/W': ratio,
        ' ': pecahan
    })
    st.dataframe(df.style.format({'P/W': '{:.2f}', ' ': '{:.2f}'}))

    st.info("Maksimum profit dari itemnya adalah : %0.2f"%maksimum_profit)
