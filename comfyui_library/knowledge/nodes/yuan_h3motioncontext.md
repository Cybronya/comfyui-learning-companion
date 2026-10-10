# Yuan_H3MotionContext

## 节点类型

`Yuan_H3MotionContext`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `条件化:CONDITIONING`（1 次）
- `潜空间:LATENT`（1 次）
- `VAE:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `衔接模式:COMBO`（1 次）
- `模式:COMBO`（1 次）
- `启用上下文:BOOLEAN`（1 次）
- `存储位置:STRING`（1 次）
- `片段序号:INT`（1 次）
- `上下文长度:COMBO`（1 次）

## 输出

- `条件化:CONDITIONING`（1 次）
- `裁剪帧数:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["视频图像", "自动索引", true, "H3-Mubu", 1, "5", "5", "34", "17", "17", "", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
