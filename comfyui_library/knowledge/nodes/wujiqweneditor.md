# WujiQwenEditor

## 节点类型

`WujiQwenEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `vae:VAE`（3 次）
- `图像:IMAGE`（3 次）
- `图像_2:IMAGE`（3 次）
- `图像_3:IMAGE`（3 次）
- `遮罩:MASK`（3 次）
- `宽度:INT`（3 次）
- `高度:INT`（3 次）
- `正面提示词:STRING`（3 次）
- `负面提示词:STRING`（3 次）

## 输出

- `正面条件:CONDITIONING`（3 次）
- `负面条件:CONDITIONING`（3 次）
- `潜在空间:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[720, 1280, "", "", "pad", "index_timestep_zero", "关闭", 1, "手动优先", "写实风格", "关闭", "关闭", "关闭", "关闭", "关闭"]`（1 次）
- `[720, 1280, "", "", "pad", "index_timestep_zero", "关闭", 1, "手动优先", "写实风格", "关闭", "关闭", "关闭", "关闭", "图像通用"]`（1 次）
- `[600, 800, "", "e", "pad", "index_timestep_zero", "关闭", 1, "手动优先", "关闭", "关闭", "关闭", "关闭", "关闭", "关闭"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
