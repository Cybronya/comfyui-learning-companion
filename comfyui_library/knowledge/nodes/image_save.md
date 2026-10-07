# Image Save

## 节点类型

`Image Save`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `output_path:STRING`（1 次）
- `filename_prefix:STRING`（1 次）
- `filename_delimiter:STRING`（1 次）
- `filename_number_padding:INT`（1 次）
- `filename_number_start:COMBO`（1 次）
- `extension:COMBO`（1 次）
- `dpi:INT`（1 次）
- `quality:INT`（1 次）
- `optimize_image:COMBO`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `files:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["哼哼AI", "QT103-文生图双引擎（Qwen-image）", "_", 4, "false", "png", 300, 100, "true", "false", "false", "false", "true", "true"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
