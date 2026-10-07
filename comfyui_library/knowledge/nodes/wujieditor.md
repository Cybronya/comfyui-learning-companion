# WujiEditor

## 节点类型

`WujiEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `正向提示词:STRING`（1 次）
- `负向提示词:STRING`（1 次）
- `多行列表:BOOLEAN`（1 次）
- `艺术流派:COMBO`（1 次）
- `媒介质感:COMBO`（1 次）
- `摄影风格:COMBO`（1 次）
- `动漫插画:COMBO`（1 次）

## 输出

- `正向条件:CONDITIONING`（1 次）
- `负向条件:CONDITIONING`（1 次）
- `空Latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[600, 800, "", "", true, "关闭", "关闭", "关闭", "关闭", "关闭", "关闭", "关闭"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
