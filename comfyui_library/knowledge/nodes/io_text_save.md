# io-text-save

## 节点类型

`io-text-save`

## 分类

Output

## 作用

输出类节点：把结果写到磁盘（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `text:STRING`（4 次）
- `path:STRING`（4 次）
- `filename_prefix:STRING`（4 次）
- `filename_delimiter:STRING`（4 次）
- `filename_number_padding:INT`（4 次）
- `overwrite_mode:COMBO`（4 次）
- `ext:STRING`（4 次）

## 输出

- `content:STRING`（4 次）
- `filenameWithoutExt:STRING`（4 次）
- `ext:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["./ComfyUI/output/[time(%Y-%m-%d)]", "ComfyUI", "_", 4, "false", ".txt"]`（2 次）
- `["E:\\Digital Media Art\\ending\\windows\\98-master\\TXT", "ComfyUI_2", "_", 4, "false", ".txt"]`（1 次）
- `["E:\\Digital Media Art\\ending\\windows\\98-master\\TXT", "ComfyUI_1", "_", 4, "false", ".txt"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
