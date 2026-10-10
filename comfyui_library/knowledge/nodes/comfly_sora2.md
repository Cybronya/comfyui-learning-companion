# Comfly_sora2

## 节点类型

`Comfly_sora2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image1:IMAGE`（5 次）
- `image2:IMAGE`（5 次）
- `image3:IMAGE`（5 次）
- `image4:IMAGE`（5 次）
- `prompt:STRING`（5 次）
- `aspect_ratio:COMBO`（5 次）
- `duration:COMBO`（5 次）
- `hd:BOOLEAN`（5 次）
- `apikey:STRING`（5 次）
- `model:COMBO`（4 次）

## 输出

- `video:VIDEO`（5 次）
- `video_url:STRING`（5 次）
- `response:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一个美丽的中国女孩，穿越到中国古代东汉末年赤壁大战的现场，拿着手机自拍杆做现场直播", "sora-2-pro", "9:16", "15", true, "", 1069238470, "randomize"]`（1 次）
- `["一个老板在办公室问员工：“这个班还上不上了”，女员工发疯式的回答：“不上了，不上了，不上了”", "sora_video2", "9:16", "10", false, ""]`（1 次）
- `["一个美丽的中国女孩，穿越到中国古代东汉末年赤壁大战的现场，拿着手机自拍杆做现场直播", "sora-2-pro", "16:9", "15", true, "", 834672233, "randomize"]`（1 次）
- `["一个美丽的中国女孩，穿越到中国古代东汉末年赤壁大战的现场，拿着手机自拍杆做现场直播", "sora-2-pro", "9:16", "25", false, "", 459566990, "randomize", true]`（1 次）
- `["一个美丽的中国女孩，穿越到中国古代东汉末年赤壁大战的现场，拿着手机自拍杆做现场直播", "sora-2", "16:9", "15", false, "", 671758111, "randomize", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
