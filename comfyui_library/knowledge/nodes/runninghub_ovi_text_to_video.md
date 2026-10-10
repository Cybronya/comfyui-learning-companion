# RunningHub Ovi Text to Video

## 节点类型

`RunningHub Ovi Text to Video`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `ovi_engine:OVI_ENGINE`（4 次）
- `text_prompt:STRING`（4 次）
- `video_height:INT`（4 次）
- `video_width:INT`（4 次）
- `seed:INT`（4 次）
- `sample_steps:INT`（4 次）
- `solver_name:COMBO`（4 次）
- `shift:FLOAT`（4 次）
- `video_guidance_scale:FLOAT`（4 次）
- `audio_guidance_scale:FLOAT`（4 次）

## 输出

- `video:VIDEO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The theme \"AI is taking over the world\" produces speeches like:\n<S>AI declares: humans obsolete now.<E>\n<S>Machine`（1 次）
- `["", 512, 992, 947728739205968, "randomize", 50, "unipc", 5, 4, 3, 11, "", ""]`（1 次）
- `["女孩挥动手里的灯笼，前面荧光蝴蝶围绕她飞舞，身后水墨背景流动光辉<S>Butterflies fluttering, loving dapao the most.<E> <AUDCAP>女人微笑的声音，蝴蝶飞舞背景音<ENDAUDCAP`（1 次）
- `["一个都市丽人在街上走路，手里拿着手机自拍，边走边解说<S>Hello world!<E> <AUDCAP>马路行车声<ENDAUDCAP>", 512, 992, 493148382032006, "randomize", 50, "u`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
