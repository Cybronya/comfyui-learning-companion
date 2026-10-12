# RH_KlingO1_VideoEdit

## 节点类型

`RH_KlingO1_VideoEdit`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video:VIDEO`（2 次）
- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `image4:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `aspect_ratio:COMBO`（2 次）
- `keep_original_sound:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["【在此输入编辑提示词】", "auto", true, 1875207016, "randomize"]`（1 次）
- `["【在此输入编辑提示词】", "auto", true, 1918024789, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
