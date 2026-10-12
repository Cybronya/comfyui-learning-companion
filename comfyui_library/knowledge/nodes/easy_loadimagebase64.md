# easy loadImageBase64

## 节点类型

`easy loadImageBase64`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `base64_data:STRING`（2 次）
- `image_output:COMBO`（2 次）
- `save_prefix:STRING`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Hide", "ComfyUI"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
