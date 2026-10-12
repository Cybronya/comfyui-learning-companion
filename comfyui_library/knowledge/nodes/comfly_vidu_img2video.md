# Comfly_vidu_img2video

## 节点类型

`Comfly_vidu_img2video`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `model:COMBO`（2 次）
- `prompt:STRING`（2 次）
- `api_key:STRING`（2 次）
- `audio:BOOLEAN`（2 次）
- `voice_language:COMBO`（2 次）
- `voice_id:COMBO`（2 次）
- `is_rec:BOOLEAN`（2 次）
- `duration:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `video_url:STRING`（2 次）
- `task_id:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["viduq2-turbo", "", "", false, "中文(普通话)", "male-qn-jingying", false, 5, 1362162984, "randomize", "720p", "auto", false,`（1 次）
- `["viduq2-turbo", "", "", true, "中文(普通话)", "female-chengshu-jingpin", false, 5, 237194335, "randomize", "720p", "auto", t`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
