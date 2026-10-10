# RunningHub Ovi Image to Video

## 节点类型

`RunningHub Ovi Image to Video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `ovi_engine:OVI_ENGINE`（2 次）
- `image:IMAGE`（2 次）
- `text_prompt:STRING`（2 次）
- `seed:INT`（2 次）
- `sample_steps:INT`（2 次）
- `solver_name:COMBO`（2 次）
- `shift:FLOAT`（2 次）
- `video_guidance_scale:FLOAT`（2 次）
- `audio_guidance_scale:FLOAT`（2 次）
- `slg_layer:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["<S>Hello world!<E> <AUDCAP>Background music playing<ENDAUDCAP>", 994823600865476, "randomize", 50, "unipc", 5, 4, 3, 1`（1 次）
- `["<S>Hello world!<E> <AUDCAP>Background music playing<ENDAUDCAP>", 721801952384863, "randomize", 50, "unipc", 5, 4, 3, 1`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
