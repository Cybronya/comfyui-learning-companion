# SplineEditor

## 节点类型

`SplineEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `bg_image:IMAGE`（4 次）
- `points_to_sample:INT`（4 次）
- `points_store:STRING`（1 次）
- `coordinates:STRING`（1 次）
- `mask_width:INT`（1 次）
- `mask_height:INT`（1 次）
- `sampling_method:COMBO`（1 次）
- `interpolation:COMBO`（1 次）
- `tension:FLOAT`（1 次）
- `repeat_output:INT`（1 次）

## 输出

- `mask:MASK`（4 次）
- `coord_str:STRING`（4 次）
- `float:FLOAT`（4 次）
- `count:INT`（4 次）
- `normalized_str:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[{\"points\":[{\"x\":473.61507704679843,\"y\":288.46833389673225},{\"x\":537.4109585816526,\"y\":309.96477223999835},{`（1 次）
- `["[{\"points\":[{\"x\":481.6036050975475,\"y\":343.5009917281414},{\"x\":568.2103287359886,\"y\":359.88604755163027},{\"`（1 次）
- `["[{\"points\":[{\"x\":599.4883510395135,\"y\":388.1932764927998},{\"x\":588.4322134178832,\"y\":357.4817830993821},{\"x`（1 次）
- `["[{\"points\":[{\"x\":511.4999999999998,\"y\":173.79999999999993},{\"x\":556.5999999999998,\"y\":208.99999999999991},{\`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
