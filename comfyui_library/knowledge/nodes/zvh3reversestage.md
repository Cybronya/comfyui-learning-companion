# ZVH3ReverseStage

## 节点类型

`ZVH3ReverseStage`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `user_prompt:STRING`（6 次）
- `material_context_json:STRING`（6 次）
- `material_evidence:STRING`（6 次）
- `chinese_user_prompt:STRING`（6 次）
- `stage:COMBO`（6 次）
- `system_prompt:STRING`（6 次）

## 输出

- `system_prompt:STRING`（6 次）
- `user_task:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["中文意图整理", ""]`（2 次）
- `["H3提示词生成", ""]`（2 次）
- `["素材理解", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
