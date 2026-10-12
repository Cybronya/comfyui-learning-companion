# InfiniteTalkMultiImage

## 节点类型

`InfiniteTalkMultiImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `auto_start_time_list:START_TIME_LIST`（4 次）
- `image1:IMAGE`（4 次）
- `image2:IMAGE`（4 次）
- `image3:IMAGE`（4 次）
- `image4:IMAGE`（4 次）
- `image5:IMAGE`（4 次）
- `image6:IMAGE`（4 次）
- `image7:IMAGE`（4 次）
- `image8:IMAGE`（4 次）
- `image9:IMAGE`（4 次）

## 输出

- `image_list:IMAGE`（4 次）
- `frame_count_list:INT`（4 次）
- `real_start_time_list:FLOAT`（4 次）
- `prompt_list:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, "", 0, 11.760000000000002, 21.360000000000003, 33.24000000000001, 41.64000000000001, 50.040000000000006, 100.0000000`（2 次）
- `[8, "", 0, 6.120000000000001, 13.150000000000002, 20.000000000000004, 27.100000000000005, 33.220000000000006, 40.1800000`（1 次）
- `[8, "", 0, 4, 8, 12.8, 16.4, 100, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
