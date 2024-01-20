import parser_script

if __name__ == "__main__":
    all_datas = parser_script.parse(
        "./dataset/Exchange_1.json",
        "./dataset/Exchange_2.json",
        "./dataset/Exchange_3.json",
    )
