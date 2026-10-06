# Yuan_H3MotionContextTrim

## 节点类型

`Yuan_H3MotionContextTrim`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `潜空间:LATENT`（2 次）
- `VAE:VAE`（2 次）
- `audio_vae:VAE`（2 次）
- `衔接模式:COMBO`（2 次）
- `片段序号:INT`（2 次）
- `保存到本地:BOOLEAN`（2 次）
- `存储位置:STRING`（2 次）
- `裁剪帧数:STRING`（1 次）

## 输出

- `图像:IMAGE`（2 次）
- `音频:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["解码模式", 1, false, "H3-Mubu"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
