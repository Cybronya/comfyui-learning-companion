# WujiClosedSourceGenerator

## 节点类型

`WujiClosedSourceGenerator`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `助力源:WUJI_LLM`（2 次）
- `助力源2:WUJI_LLM`（2 次）
- `images.image_0:IMAGE`（2 次）
- `images.image_1:IMAGE`（2 次）
- `videos.video_0:VIDEO`（2 次）
- `audios.audio_0:AUDIO`（2 次）
- `generation_type:COMBO`（2 次）
- `prompt:STRING`（2 次）
- `constraints:STRING`（2 次）
- `meta_instruction:STRING`（2 次）

## 输出

- `文本:STRING`（2 次）
- `图像:IMAGE`（2 次）
- `视频:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["图像", "图1的美女在古代花园里喂鱼", "", "", "⑤ 多参｜全部作参考图，不设首尾帧", false, "3:4", "1K", 0, 395652853429489, "randomize", -1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
