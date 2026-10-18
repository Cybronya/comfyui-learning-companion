# YuE2GenerateSong

## 节点类型

`YuE2GenerateSong`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:YUE2_MODEL`（1 次）
- `trained_style_model:YUE2_STYLE_MODEL`（1 次）
- `style:STRING`（1 次）
- `lyrics:STRING`（1 次）
- `cot:COMBO`（1 次）
- `seed:INT`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `candidates:INT`（1 次）
- `abc:STRING`（1 次）
- `style_model:COMBO`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `result:YUE2_RESULT`（1 次）
- `metadata:STRING`（1 次）
- `output_directory:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Mandarin pop, warm female vocal, piano, strings", "[Verse]\n晚风穿过城市的灯\n[Chorus]\n让这首歌飞过长空", "full", 831001, "fixed", 1.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
