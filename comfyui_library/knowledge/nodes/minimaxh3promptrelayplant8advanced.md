# MiniMaxH3PromptRelayPlanT8Advanced

## 节点类型

`MiniMaxH3PromptRelayPlanT8Advanced`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt_relay_events:H3_T8_PROMPT_RELAY_EVENTS`（1 次）
- `global_prompt:STRING`（1 次）
- `local_prompts:STRING`（1 次）
- `length:INT`（1 次）
- `timing_mode:COMBO`（1 次）
- `time_ranges:STRING`（1 次）
- `math_profile:COMBO`（1 次）
- `epsilon:FLOAT`（1 次）
- `allow_gaps:BOOLEAN`（1 次）
- `allow_overlaps:BOOLEAN`（1 次）

## 输出

- `prompt_relay_plan:H3_T8_PROMPT_RELAY_PLAN`（1 次）
- `compiled_prompt:STRING`（1 次）
- `length:INT`（1 次）
- `timeline_json:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["3D CG，皮克斯风格动画卡通。唐代乡村，一座破旧茅草屋，门外堆着柴垛。主角是卡通杜甫：瘦弱、略微佝偻，穿补丁累累的灰蓝色布袍，戴旧头巾。全片保持杜甫的外貌、衣着和声音一致。杜甫使用同一个滑稽、细弱、略带喘息而兴奋的男性声音（S1），说`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
