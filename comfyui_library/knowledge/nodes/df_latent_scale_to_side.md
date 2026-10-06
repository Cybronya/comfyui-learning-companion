# DF_Latent_Scale_to_side

## 节点类型

`DF_Latent_Scale_to_side`

## 分类

Latent

## 作用

latent 空间处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `latent:LATENT`（2 次）
- `side_length:INT`（2 次）
- `side:COMBO`（2 次）
- `scale_method:COMBO`（2 次）
- `crop:COMBO`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2048, "Longest", "nearest-exact", "disabled"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
