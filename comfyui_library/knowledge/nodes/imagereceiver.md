# ImageReceiver

## 节点类型

`ImageReceiver`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:COMBO`（2 次）
- `link_id:INT`（2 次）
- `save_to_workflow:BOOLEAN`（2 次）
- `image_data:STRING`（2 次）
- `trigger_always:BOOLEAN`（2 次）
- `upload:IMAGEUPLOAD`（2 次）

## 输出

- `IMAGE:IMAGE`（6 次）
- `MASK:MASK`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 0, false, "", false, "image"]`（1 次）
- `["None", 1, true, "", false, "image"]`（1 次）
- `["ImgSender_temp_skply_00001_.png [temp]", 3, false, "", false]`（1 次）
- `["ImgSender_temp_efvmf_00001_.png [temp]", 0, false, "", false]`（1 次）
- `["ImgSender_temp_hzxpx_00001_.png [temp]", 2, false, "", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
