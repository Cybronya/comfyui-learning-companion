# Light-Tool: LoadImageFromURL

## 节点类型

`Light-Tool: LoadImageFromURL`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `url:STRING`（20 次）
- `keep_alpha_channel:BOOLEAN`（20 次）
- `timeout:INT`（20 次）
- `max_retries:INT`（20 次）

## 输出

- `image:IMAGE`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", false, 30, 3]`（20 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
