# LayerUtility: SaveImagePlus

## 节点类型

`LayerUtility: SaveImagePlus`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `images:IMAGE`（18 次）
- `custom_path:STRING`（18 次）
- `filename_prefix:STRING`（18 次）
- `timestamp:COMBO`（18 次）
- `format:COMBO`（18 次）
- `quality:INT`（18 次）
- `meta_data:BOOLEAN`（18 次）
- `blind_watermark:STRING`（18 次）
- `save_workflow_as_json:BOOLEAN`（18 次）
- `preview:BOOLEAN`（18 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "高清图-原版", "millisecond", "jpg", 80, true, "", false, true]`（12 次）
- `["", "高清图-官方", "millisecond", "jpg", 80, true, "", false, true]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
