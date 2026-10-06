# easy saveVideo

## 节点类型

`easy saveVideo`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `input_mode:COMFY_DYNAMICCOMBO_V3`（10 次）
- `input_mode.video:VIDEO`（10 次）
- `input_mode.audio:AUDIO`（10 次）
- `output_mode:COMFY_DYNAMICCOMBO_V3`（10 次）
- `filename_prefix:STRING`（10 次）

## 输出

- `VIDEO:VIDEO`（10 次）
- `file_path:STRING`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["video", "hide", "h3"]`（5 次）
- `["video", "hide", "H3"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
