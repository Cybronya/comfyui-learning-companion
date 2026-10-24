# QI_TextEncodeQwenImageEdit_CN

## 节点类型

`QI_TextEncodeQwenImageEdit_CN`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP模型:CLIP`（1 次）
- `图像:IMAGE`（1 次）
- `VAE:VAE`（1 次）
- `提示词:STRING`（1 次）
- `模式_不缩放网格填充:BOOLEAN`（1 次）
- `填充方式:COMBO`（1 次）
- `网格倍数:INT`（1 次）
- `注入模式:COMBO`（1 次）
- `像素来源:COMBO`（1 次）
- `像素形态:COMBO`（1 次）

## 输出

- `条件:CONDITIONING`（1 次）
- `图像:IMAGE`（1 次）
- `潜空间:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", true, "reflect", 64, "两者都注入", "VAE重建", "色彩场_64", true, 0, 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
