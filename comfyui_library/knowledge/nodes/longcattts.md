# LongCatTTS

## 节点类型

`LongCatTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model_path:COMBO`（2 次）
- `text:STRING`（2 次）
- `steps:INT`（2 次）
- `guidance_strength:FLOAT`（2 次）
- `guidance_method:COMBO`（2 次）
- `device:COMBO`（2 次）
- `dtype:COMBO`（2 次）
- `attention:COMBO`（2 次）
- `seed:INT`（2 次）
- `keep_model_loaded:BOOLEAN`（2 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["LongCat-AudioDiT-3.5B-bf16", "", 40, 4, "cfg", "auto", "fp32", "auto", 777329333, "randomize", false]`（1 次）
- `["LongCat-AudioDiT-3.5B-bf16", "", 40, 4, "cfg", "auto", "fp32", "auto", 561025643, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
