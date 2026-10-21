# LayerUtility: LoadImagesFromPath

## 节点类型

`LayerUtility: LoadImagesFromPath`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `path:STRING`（4 次）
- `image_load_cap:INT`（4 次）
- `select_every_nth:INT`（4 次）

## 输出

- `images:IMAGE`（4 次）
- `masks:MASK`（4 次）
- `file_name:STRING`（4 次）
- `frame_count:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["D:\\Qwen体系课程录制\\Qwen实操课4\\批量图", 0, 1]`（2 次）
- `["E:\\load-image", 0, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
