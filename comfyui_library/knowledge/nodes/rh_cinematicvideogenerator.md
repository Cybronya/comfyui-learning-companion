# RH_CinematicVideoGenerator

## 节点类型

`RH_CinematicVideoGenerator`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 14 个 workflow 中。

## 输入

- `image1:IMAGE`（14 次）
- `image2:IMAGE`（14 次）
- `image3:IMAGE`（14 次）
- `image4:IMAGE`（14 次）
- `api_config:RH_OPENAPI_CONFIG`（14 次）
- `prompt:STRING`（14 次）
- `duration:COMBO`（14 次）
- `aspectRatio:COMBO`（14 次）
- `skip_error:BOOLEAN`（14 次）
- `seed:INT`（14 次）

## 输出

- `video:VIDEO`（14 次）
- `url:STRING`（14 次）
- `response:STRING`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "5", "16:9", false, 832501091993479, "randomize"]`（2 次）
- `["", "15", "9:16", false, 1015691188735965, "randomize"]`（1 次）
- `["镜头 1: 穿越光影 (Crossing the Light Barrier)\n\n[画面] 慢动作，两名男子以优雅的跑酷姿态，从霓虹灯构成的光影幕墙前跃过，仿佛穿越了一层流动的彩色屏障。无数璀璨的光点如雨般在他们周围飞舞。\n\n镜`（1 次）
- `["0–3s\nHigh-angle panoramic shot, 2D-3D style, sweet cool pink-white with neon pink-purple lighting. In a girl group pr`（1 次）
- `["请描述希望视频如何运动。\\n示例：镜头从近到远慢慢拉开，人物轻轻转头微笑，背景灯光逐渐变亮，电影感。\\n提示：图像负责“长什么样”，提示词负责“怎么动”。", "15", "16:9", false, 101240877256826`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
