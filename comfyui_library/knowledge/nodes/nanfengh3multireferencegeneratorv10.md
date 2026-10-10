# NanFengH3MultiReferenceGeneratorV10

## 节点类型

`NanFengH3MultiReferenceGeneratorV10`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:COMBO`（1 次）
- `文本编码器:COMBO`（1 次）
- `文本编码器类型:COMBO`（1 次）
- `文本编码器设备:COMBO`（1 次）
- `视频VAE:COMBO`（1 次）
- `音频VAE:COMBO`（1 次）
- `模型权重精度:COMBO`（1 次）
- `SageAttention:COMBO`（1 次）
- `允许编译:BOOLEAN`（1 次）
- `画面比例:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `音频:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_hybrid_fl2va_ref2va_b25-49-bf16-v1.01.safetensors", "qwen3vl_32b_minimax_h3_int8_convrot.safetensors", "min`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
