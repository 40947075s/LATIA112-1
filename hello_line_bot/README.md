# HW3: Sentiment Analysis Line Bot

## Part 1: Azure 語言服務

#### Azure 語言服務簡介

Azure 提供了多種語言服務，這些服務旨在幫助開發人員處理和分析自然語言文本。以下是一些Azure語言服務所提供的主要功能：

1. 文本分析（Text Analytics）：

   - 情感分析（Sentiment Analysis）： 分析文本中的情感，分辨正面、負面或中性的情感傾向。
   - 實體識別（Entity Recognition）： 辨識文本中的實體（如人名、地點、組織等）。
   - 主題識別（Key Phrase Extraction）： 提取文本中的關鍵詞，以幫助理解文本的核心內容。

2. 語音服務（Speech Service）：

   - 語音轉文字（Speech-to-Text）： 將語音轉換成文字。
   - 文字轉語音（Text-to-Speech）： 將文字轉換為自然、流暢的語音。
   - 語音識別（Speech Recognition）： 辨認語音中的指定命令或詞彙。

3. 語言理解（Language Understanding）：

   - LUIS（Language Understanding）： 通過機器學習來實現自然語言的理解，以使應用程式能理解用戶的輸入，並提取意圖和任何有用的實體訊息。

4. 機器翻譯（Translator）：

   - 文本翻譯： 提供多種語言之間的文本翻譯。
   - 語音翻譯： 可以將一種語言的語音翻譯為另一種語言的語音。

5. 語音分析（Speaker Recognition）：

   - 語音識別： 辨認語音中的說話者，用於語音驗證等應用。

6. 語言合成（Speech Synthesis）：

   - 自然語音生成（Neural Text-to-Speech）： 使用神經網絡生成更自然的語音。

透過這些服務的組合，我們可以實現諸如截取資訊、分類文字、了解交談語言、回答問題、翻譯文本、以及摘要文字等各式各樣的應用功能。

---

#### Azure 語言服務的教育應用 - 智慧筆記

學生可以透過語音或文本來輸入內容，並由應用程式來製作重點筆記。

這個應用可能會使用到以下服務：

1. 語音轉文字（Speech-to-Text）： 將語音輸入轉換成可供分析的文字。

2. 文本分析：用於分析文字，提取筆記的關鍵詞與重點內容以製作筆記；更甚者，可以透過情感分析來判斷筆記的正負面情緒，以及辨識筆記中的人名、地點、組織等，以供更詳細的參考。

3. 語言理解：用於理解學生的自然語言輸入，以提取意圖和實體訊息。

4. 語音合成：當學生需要聽取筆記時，可以將文字轉換成語音，以便學生在需要的時候可以聽取筆記的內容。

---

## Part 2: Line Bot

程式重點修改部分在約莫第75行的函數 `azure_sentiment` 中。

> 註：[程式碼連結](app.py)

#### Line Bot screenshot

![](screenshot.jpg)
