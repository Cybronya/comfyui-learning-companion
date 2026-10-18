# T8_IndexTTS25_Pronunciation

## 节点类型

`T8_IndexTTS25_Pronunciation`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 18 个 workflow 中。

## 输入

- `text:STRING`（18 次）
- `language:COMBO`（18 次）
- `dictionary:STRING`（18 次）
- `strict:BOOLEAN`（18 次）

## 输出

- `发音标注文本:STRING`（18 次）
- `替换/校验报告:STRING`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["他在银行里工作，工作能力非常行，行长正在开会；这段手工标注的银<行|HANG2>不会被词典覆盖。", "ZH", "行|XING2|ZH\n银行|YIN2 HANG2|ZH\n行长|HANG2 ZHANG3|ZH\n重庆|CHONG2 `（10 次）
- `["", "ZH", "", true]`（3 次）
- `["他在银行里工作，行长正在开会。", "ZH", "银行|YIN2 HANG2|ZH\n行长|HANG2 ZHANG3|ZH", true]`（2 次）
- `["这里填语音内容", "ZH", "这里填多音字的字典", true]`（1 次）
- `["彼は料理が<上手|じょうず>だが、囲碁では<上手|うわて>に負けた。", "JA", "", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
