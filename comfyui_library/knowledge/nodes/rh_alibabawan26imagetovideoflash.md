# RH_AlibabaWan26ImageToVideoFlash

## 节点类型

`RH_AlibabaWan26ImageToVideoFlash`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（1 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "1080p", "5", "single", true, true, "", false, 0, "randomize"]`（1 次）
- `["镜头缓慢推近，人物自然呼吸、轻微转头，光线柔和流动，画面稳定。 / Slow push-in, the subject breathes naturally and turns the head slightly, soft shift`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
