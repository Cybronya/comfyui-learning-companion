# OpenAI_Sora_API_Plus

## 节点类型

`OpenAI_Sora_API_Plus`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `base_url:STRING`（1 次）
- `model:STRING`（1 次）
- `api_key:STRING`（1 次）
- `user_prompt:STRING`（1 次）
- `aspect_ratio:STRING`（1 次）
- `hd:BOOLEAN`（1 次）
- `duration:INT`（1 次）
- `image:IMAGE`（1 次）

## 输出

- `video:VIDEO`（1 次）
- `video_url:STRING`（1 次）
- `tokens_usage:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://ai.t8star.cn/v1/", "sora_video2-landscape-15s", "", "小狗的历险记\n", "16:9", true, 15]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
