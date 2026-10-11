# RH_Jimeng_Image2Video_V2

## 节点类型

`RH_Jimeng_Image2Video_V2`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `model:COMBO`（3 次）
- `duration:COMBO`（3 次）
- `resolution:COMBO`（3 次）
- `ratio:COMBO`（3 次）
- `seed:INT`（3 次）

## 输出

- `video:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["男子难受的按自己的头", "doubao-seedance-1-0-pro-fast-251015", "5", "1080p", "16:9", 1165730955, "randomize"]`（1 次）
- `["镜头缓慢推进，女子难受的抚摸自己的脸", "doubao-seedance-1-0-pro-fast-251015", "5", "1080p", "16:9", 759430821, "randomize"]`（1 次）
- `["人物不动，坐着休息", "doubao-seedance-1-0-pro-250528", "10", "1080p", "16:9", 1194439261, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
