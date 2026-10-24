# workflow>Load PuLID FluxI

## 节点类型

`workflow>Load PuLID FluxI`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `pulid_flux:PULIDFLUX`（1 次）
- `image:IMAGE`（1 次）
- `attn_mask:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["CUDA", 1.15, 0.5, 0.9, 0, 1, 1024, 1024]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
