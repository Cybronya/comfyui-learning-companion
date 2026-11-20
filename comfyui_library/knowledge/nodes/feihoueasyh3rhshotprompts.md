# FeiHouEasyH3RHShotPrompts

## 节点类型

`FeiHouEasyH3RHShotPrompts`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt_text:STRING`（2 次）
- `start:COMBO`（2 次）
- `shot_numbers:STRING`（2 次）

## 输出

- `production_shot:FEIHOU_H3_RH_PRODUCTION_SHOT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "自动续接", "0", null]`（1 次）
- `["鸟叔 Gentleman → 少林足球 人物替换分镜\n@fps 24\n@characters\n1 = R1 主角 PSY → 吴孟达.png\n2 = O4 白发薄荷绿外套老人 / B25–26 舞团最左黑西装短发男 → 主人物：`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
