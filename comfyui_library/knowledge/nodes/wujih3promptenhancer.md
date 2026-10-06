# WujiH3PromptEnhancer

## 节点类型

`WujiH3PromptEnhancer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `first_frame:IMAGE`（2 次）
- `last_frame:IMAGE`（2 次）
- `reference_images.reference_image_0:IMAGE`（2 次）
- `reference_images.reference_image_1:IMAGE`（2 次）
- `reference_images.reference_image_2:IMAGE`（2 次）
- `reference_videos.reference_video_0:VIDEO`（2 次）
- `助力源:WUJI_LLM`（2 次）
- `prompt:STRING`（2 次）
- `task_type:COMBO`（2 次）
- `duration_seconds:INT`（2 次）

## 输出

- `enhanced_prompt:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一、核心要求\n一支高燃双人仙侠对决短片。\n场景为夜晚中式古代楼阁、屋檐、庭院石地，地面湿润，有明显倒影；环境同时存在冷蓝月光与暖黄灯火，远处乌云翻涌，整体氛围冷峻、压迫、华丽。\n全片围绕两位固定角色展开，人物外貌、服装、武器、能量`（1 次）
- `["一、核心要求\n一支高燃双人仙侠对决短片。\n场景为夜晚中式古代楼阁、屋檐、庭院石地，地面湿润，有明显倒影；环境同时存在冷蓝月光与暖黄灯火，远处乌云翻涌，整体氛围冷峻、压迫、华丽。\n全片围绕两位固定角色展开，人物外貌、服装、武器、能量`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
