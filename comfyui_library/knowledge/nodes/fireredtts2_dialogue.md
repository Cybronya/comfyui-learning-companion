# FireRedTTS2_Dialogue

## 节点类型

`FireRedTTS2_Dialogue`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `S1:AUDIO`（4 次）
- `S2:AUDIO`（4 次）
- `text_list:STRING`（4 次）
- `temperature:FLOAT`（4 次）
- `topk:INT`（4 次）
- `S1_text:STRING`（4 次）
- `S2_text:STRING`（4 次）

## 输出

- `audio:AUDIO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0.9, 20, "", ""]`（2 次）
- `["[S1]你在干嘛呀贞贞？\n[S2]我正在学习AI呢\n[S1]That's wonderful to hear.", 0.7000000000000002, 20, "你在干嘛呀贞贞？", "我正在学习AI呢"]`（1 次）
- `["[S1]你在干嘛呀贞贞？\n[S2]我正在学习AI呢\n[S1]That's wonderful to hear.", 0.9, 30, "我刚做好的模型，被调试时不小心弄坏了，数据全没了", "那是我花了一周才搭建好的！你调试前都不确`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
