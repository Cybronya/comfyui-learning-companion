# SDXL Power Prompt - Positive (rgthree)

## 节点类型

`SDXL Power Prompt - Positive (rgthree)`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `opt_model:MODEL`（1 次）
- `opt_clip:CLIP`（1 次）
- `opt_clip_width:INT`（1 次）
- `opt_clip_height:INT`（1 次）
- `prompt_l:STRING`（1 次）
- `prompt_g:STRING`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `TEXT_G:STRING`（1 次）
- `TEXT_L:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1girl, solo, long_hair, looking_at_viewer, red_eyes, gloves, jewelry, red_hair, earrings, belt, white_gloves, cape, or`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
