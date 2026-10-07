# CR Hires Fix Process Switch

## 节点类型

`CR Hires Fix Process Switch`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `latent_upscale:LATENT`（1 次）
- `image_upscale:LATENT`（1 次）

## 输出

- `LATENT:LATENT`（1 次）
- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["latent_upscale"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
