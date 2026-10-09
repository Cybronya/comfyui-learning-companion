# SeedreamVideoGeneratorNode

## 节点类型

`SeedreamVideoGeneratorNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model_selection:COMBO`（1 次）
- `duration:COMBO`（1 次）
- `ratio:COMBO`（1 次）
- `watermark:BOOLEAN`（1 次）
- `seed:INT`（1 次）
- `fps:COMBO`（1 次）

## 输出

- `frames:IMAGE`（1 次）
- `frame_count:INT`（1 次）
- `fps:FLOAT`（1 次）
- `video_url:STRING`（1 次）
- `task_id:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一个愤怒的孔明灯，火焰微微颤抖，发出橘红色的光芒，映照在水面上，水面泛起细小的涟漪，月亮高悬在夜空中，银白色的月光洒在孔明灯和水面上，形成斑驳的光影，夜色宁静而神秘，水边长满青苔，远处隐约可见山影，整个场景充满诗意和想象力，高清细节，写`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
