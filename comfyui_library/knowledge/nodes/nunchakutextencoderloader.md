# NunchakuTextEncoderLoader

## 节点类型

`NunchakuTextEncoderLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_type:COMBO`（1 次）
- `text_encoder1:COMBO`（1 次）
- `text_encoder2:COMBO`（1 次）
- `t5_min_length:INT`（1 次）
- `use_4bit_t5:COMBO`（1 次）
- `int4_model:COMBO`（1 次）

## 输出

- `CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux", "sd3/t5xxl_fp16.safetensors", "clip_l.safetensors", 1024, "disable", "none"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
