# Seedream4StreamingNode

## 节点类型

`Seedream4StreamingNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `api_key:STRING`（1 次）
- `max_images:INT`（1 次）
- `size:COMBO`（1 次）
- `sequential_image_generation:COMBO`（1 次）
- `watermark:BOOLEAN`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `task_id:STRING`（1 次）
- `status:STRING`（1 次）
- `batch_count:INT`（1 次）
- `generation_time:FLOAT`（1 次）
- `progress:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 2, "4:3 (2304x1728)", "auto", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
