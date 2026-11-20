---
name: unknown_workflow_generic_538
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.745
common_nodes: [MultiplePathsInput, Qwen3_VQA, ShowText|pysssss, easy positive, easy saveText]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3-VL-4B 视频反推_1993936457918251009.json, 图片生成/反推提示词/千问反推-视频提示词-Qwen3VL_1983393808253689857.json, 图片生成/反推提示词/反推-视频提示词2-Qwen3VL_1982447180357214210.json, 图片生成/反推提示词/反推-视频提示词2-Qwen3VL_2066055925569744896.json, 图片生成/反推提示词/反推-视频翻译-Qwen3VL_1988327686353371137.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_538

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/反推提示词/Qwen3-VL-4B 视频反推_1993936457918251009.json、图片生成/反推提示词/千问反推-视频提示词-Qwen3VL_1983393808253689857.json、图片生成/反推提示词/反推-视频提示词2-Qwen3VL_1982447180357214210.json、图片生成/反推提示词/反推-视频提示词2-Qwen3VL_2066055925569744896.json、图片生成/反推提示词/反推-视频翻译-Qwen3VL_1988327686353371137.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `MultiplePathsInput`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `easy positive`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `VideoLoader` —— 3/5 个有
- `VideoLoaderPlus` —— 2/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
