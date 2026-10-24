# workflow>反推

## 节点类型

`workflow>反推`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `LoRA:PEFTLORA`（1 次）
- `图像:IMAGE`（1 次）
- `model:COMBO`（1 次）
- `precision:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `convert_to_safetensors:BOOLEAN`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `resolution_steps:INT`（1 次）
- `seed:INT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `Florence2Run 图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `caption:STRING`（1 次）
- `json数据:JSON`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiaoshouAI/Florence-2-base-PromptGen-v2.0", "fp16", "sdpa", false, "nearest-exact", 1, 1, 966262102968691, "randomize"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
