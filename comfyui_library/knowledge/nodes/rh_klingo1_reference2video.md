# RH_KlingO1_Reference2Video

## 节点类型

`RH_KlingO1_Reference2Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image1:IMAGE`（3 次）
- `video:VIDEO`（3 次）
- `image2:IMAGE`（3 次）
- `image3:IMAGE`（3 次）
- `image4:IMAGE`（3 次）
- `image5:IMAGE`（3 次）
- `image6:IMAGE`（3 次）
- `prompt:STRING`（3 次）
- `aspect_ratio:COMBO`（3 次）
- `duration:COMBO`（3 次）

## 输出

- `video:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "auto", "5", false, 607255520, "randomize"]`（1 次）
- `["", "1:1", "5", true, 1296248029, "decrement"]`（1 次）
- `["【在此输入编辑提示词】", "auto", "5", true, 268546002, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
