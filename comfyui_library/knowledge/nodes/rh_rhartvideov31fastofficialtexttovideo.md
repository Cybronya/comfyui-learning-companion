# RH_RhartVideoV31FastOfficialTextToVideo

## 节点类型

`RH_RhartVideoV31FastOfficialTextToVideo`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `prompt:STRING`（2 次）
- `duration:COMBO`（2 次）
- `resolution:COMBO`（2 次）
- `generateAudio:BOOLEAN`（2 次）
- `negativePrompt:STRING`（2 次）
- `aspectRatio:COMBO`（2 次）
- `seed:INT`（2 次）
- `skip_error:BOOLEAN`（2 次）

## 输出

- `video:VIDEO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["粘土定格动画风格。一个胖乎乎的粘土小人正在厨房里笨手笨脚地揉面团，脸上沾满了面粉。角色动作带有轻微的停顿感，色彩明亮，能清晰看到粘土上的手工指纹压痕，非常可爱治愈。", "8", "720p", true, "", "16:9", 66`（1 次）
- `["【在此输入视频提示词】", "8", "720p", true, "", "9:16", 1078809155845191, "randomize", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
