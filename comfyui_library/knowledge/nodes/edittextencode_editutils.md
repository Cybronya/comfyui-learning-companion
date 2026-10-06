# EditTextEncode_EditUtils

## 节点类型

`EditTextEncode_EditUtils`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `clip:CLIP`（10 次）
- `vae:VAE`（10 次）
- `model_config:DICT`（10 次）
- `configs:LIST`（10 次）
- `prompt:STRING`（10 次）

## 输出

- `conditioning:CONDITIONING`（10 次）
- `latent:LATENT`（10 次）
- `custom_output:ANY`（10 次）
- `main_image:IMAGE`（10 次）
- `mask:MASK`（10 次）
- `pad_info:ANY`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[""]`（8 次）
- `["女人戴着天蓝色墨镜"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
