# LoadImagesFromPath

## 节点类型

`LoadImagesFromPath`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `seed:*`（2 次）
- `file_path:STRING`（1 次）
- `white_bg:COMBO`（1 次）
- `sort_by:COMBO`（1 次）
- `index_variable:INT`（1 次）
- `watcher:COMBO`（1 次）
- `result:WATCHER`（1 次）
- `prompt:PROMPT`（1 次）

## 输出

- `image list:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `prompt_for_FloatingVideo:STRING`（2 次）
- `filepaths:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Z:\\工作流_测试\\抠图", "disable", "file_name", 5, "disable", null, null]`（1 次）
- `["", "disable", "file_name", -1, "disable", null, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
