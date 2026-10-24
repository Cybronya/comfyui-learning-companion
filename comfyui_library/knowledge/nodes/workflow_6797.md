# workflow>一次采样

## 节点类型

`workflow>一次采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `列表（可选）:LIST`（1 次）
- `TextEncodeQwenImageEditPlus (Positive) image1:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus (Positive) image2:IMAGE`（1 次）
- `TextEncodeQwenImageEditPlus (Positive) image3:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `Latent:LATENT`（1 次）
- `字符串:STRING`（1 次）
- `列表:LIST`（1 次）
- `图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1568, 880, 1, "qwen_image_vae.safetensors", "qwen_image_edit_2511_fp8mixed.safetensors", "fp8_e4m3fn", "qwen_2.5_vl_7b.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
