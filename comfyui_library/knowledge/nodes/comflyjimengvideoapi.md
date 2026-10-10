# ComflyJimengVideoApi

## 节点类型

`ComflyJimengVideoApi`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `duration:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `cfg_scale:FLOAT`（1 次）
- `api_key:STRING`（1 次）
- `seed:INT`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `task_id:STRING`（1 次）
- `response:STRING`（1 次）
- `video_url:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["古风，一个英俊白衣男人和一个美若天仙的女人抱在一起接吻，长安灯火夜景", 5, "16:9", 0.5, "", 848571975, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
