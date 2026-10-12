# Load Cache

## 节点类型

`Load Cache`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `latent_path:STRING`（8 次）
- `image_path:STRING`（8 次）
- `conditioning_path:STRING`（8 次）

## 输出

- `LATENT:LATENT`（8 次）
- `IMAGE:IMAGE`（8 次）
- `CONDITIONING:CONDITIONING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", ""]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
