# WujiSuperEditor

## 节点类型

`WujiSuperEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `图像1:IMAGE`（2 次）
- `图像2:IMAGE`（2 次）
- `图像3:IMAGE`（2 次）
- `图像4:IMAGE`（2 次）
- `图像1遮罩:MASK`（2 次）
- `提示词:STRING`（2 次）
- `负向提示词:STRING`（2 次）
- `宽度:INT`（2 次）

## 输出

- `正向条件:CONDITIONING`（2 次）
- `负向条件:CONDITIONING`（2 次）
- `潜空间:LATENT`（2 次）
- `宽度:INT`（2 次）
- `高度:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "nsfw", 1024, 1024, true, "参考图像尺寸", "disabled", "关闭", "关闭", "关闭", "关闭", "关闭", "关闭", "关闭", 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
