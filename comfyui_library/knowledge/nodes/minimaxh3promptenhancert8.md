# MiniMaxH3PromptEnhancerT8

## 节点类型

`MiniMaxH3PromptEnhancerT8`

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
- `api_key:STRING`（2 次）
- `performance_director_config:T8_PERFORMANCE_DIRECTOR_CONFIG`（2 次）
- `provider_config:T8_LLM_PROVIDER_CONFIG`（2 次）
- `character_performance_bible:T8_CHARACTER_PERFORMANCE_BIBLE`（2 次）

## 输出

- `enhanced_prompt:STRING`（2 次）
- `global_prompt:STRING`（2 次）
- `local_prompts:STRING`（2 次）
- `time_ranges:STRING`（2 次）
- `relay_length:INT`（2 次）
- `relay_report:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Ref2VA（参考图/视频生音视频）", 5, "AUTO（系统自动判断）", "creative", 0, "中文", "官方增强", "现有兼容（保留中英文）", "AUTO（根据意图判断）", "无（不使用 T8 案例）"`（1 次）
- `["女人在跳舞", "Ref2VA（参考图/视频生音视频）", 10, "AUTO（系统自动判断）", "balanced", 0, "中文", "官方增强", "官方 Skill 严格（全英文协议）", "AUTO（根据意图判断）", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
