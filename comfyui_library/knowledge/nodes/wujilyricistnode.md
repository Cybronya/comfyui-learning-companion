# WujiLyricistNode

## 节点类型

`WujiLyricistNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `成品歌词:STRING`（1 次）
- `手动标签:STRING`（1 次）
- `动力源:WUJI_LLM`（1 次）
- `创作主题:STRING`（1 次）
- `声色选择:COMBO`（1 次）
- `押韵方案:COMBO`（1 次）
- `预计时长:COMBO`（1 次）
- `语言选择:COMBO`（1 次）
- `_高级流派:STRING`（1 次）
- `_高级情绪:STRING`（1 次）

## 输出

- `🎤 歌词:STRING`（1 次）
- `🏷️ 英文标签:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一首打工人的歌", "女性", "AAAA", "2分钟(短曲)", "中文", "", "", "", "", "", "", "", 0, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
