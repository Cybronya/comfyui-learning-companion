# WujiLyricist2

## 节点类型

`WujiLyricist2`

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
- `输出格式:COMBO`（1 次）
- `接口模式:COMBO`（1 次）
- `openai_temperature:FLOAT`（1 次）
- `openai_max_tokens:INT`（1 次）
- `声色:COMBO`（1 次）
- `押韵方案:COMBO`（1 次）

## 输出

- `🎤 歌词:STRING`（1 次）
- `🏷️ 风格标签:STRING`（1 次）
- `时长（整数秒）:INT`（1 次）
- `时长（浮点秒）:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "MiniMax Music 3.0（官方格式）", "外接助力源（无极动力源）", 0.7, 4096, "温暖男声", "AAAA", "240", "中文", "短（4-8秒）", "自动判断（按时长与平台）", "平衡扩写`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
