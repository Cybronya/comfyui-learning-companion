---
name: unknown_workflow_generic_1319
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.809
common_nodes: [CR Prompt Text, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveStringMultiline, StringFunction|pysssss, easy saveText, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/推理-单图多分镜提示词-Qwen3VL_1999797119504482306.json, 图片生成/反推提示词/推理-单图多分镜提示词-RH_1999781948660871169.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1319

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/推理-单图多分镜提示词-Qwen3VL_1999797119504482306.json、图片生成/反推提示词/推理-单图多分镜提示词-RH_1999781948660871169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `StringFunction|pysssss`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Qwen3_VQA` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
