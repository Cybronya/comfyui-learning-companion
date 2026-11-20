---
name: unknown_workflow_generic_687
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.825
common_nodes: [ImageLoader, MultiplePathsInput, Qwen3_VQA, ShowText|pysssss, easy saveText]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3-VL 图像反推_2013667916629151746.json, 图片生成/反推提示词/Qwen3-VL-8B 图像反推_2018232325892476930.json, 图片生成/反推提示词/图片反推提示词Qwen3-VL_2018505343491379201.json, 视频生成/图生视频/推理-首尾帧生视频提示词-qwen3VL_1982744634411630593.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_687

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Qwen3-VL 图像反推_2013667916629151746.json、图片生成/反推提示词/Qwen3-VL-8B 图像反推_2018232325892476930.json、图片生成/反推提示词/图片反推提示词Qwen3-VL_2018505343491379201.json、视频生成/图生视频/推理-首尾帧生视频提示词-qwen3VL_1982744634411630593.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageLoader`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `StringFunction|pysssss` —— 1/4 个有
- `easy positive` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
