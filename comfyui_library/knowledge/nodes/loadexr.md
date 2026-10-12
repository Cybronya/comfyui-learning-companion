# LoadEXR

## 节点类型

`LoadEXR`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `filepath:STRING`（8 次）
- `linear_to_sRGB:BOOLEAN`（8 次）
- `image_load_cap:INT`（8 次）
- `skip_first_images:INT`（8 次）
- `select_every_nth:INT`（8 次）

## 输出

- `RGB:IMAGE`（8 次）
- `alpha:MASK`（8 次）
- `batch_size:INT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["path to directory or .exr file", true, 0, 0, 1]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
