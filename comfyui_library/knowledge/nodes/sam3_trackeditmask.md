# SAM3_TrackEditMask

## 节点类型

`SAM3_TrackEditMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `track_data:SAM3_TRACK_DATA`（1 次）
- `roles_json:STRING`（1 次）
- `replace_background:BOOLEAN`（1 次）

## 输出

- `edit_masks:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[\"REPLACE\"]", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
