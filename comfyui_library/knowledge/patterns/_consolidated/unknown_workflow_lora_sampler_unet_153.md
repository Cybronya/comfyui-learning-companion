---
name: unknown_workflow_lora_sampler_unet_153
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.854
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图丨美食解构海报_2054801927573123073.json, 图片生成/图生图/换装+换衣+电商+FireRed-Image-Edit+多件服饰批量叠穿_2092526645906329601.json, 图片生成/图生图/模特套图工作流_1979044192452251649.json, 图片生成/图生图/模特套图工作流_1995150910940753922.json, 图片生成/文生图/Qwen_手写字体生成_2054073147015614466.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_153

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图生图丨美食解构海报_2054801927573123073.json、图片生成/图生图/换装+换衣+电商+FireRed-Image-Edit+多件服饰批量叠穿_2092526645906329601.json、图片生成/图生图/模特套图工作流_1979044192452251649.json、图片生成/图生图/模特套图工作流_1995150910940753922.json、图片生成/文生图/Qwen_手写字体生成_2054073147015614466.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `easy promptList` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `seed _O` —— 2/5 个有
- `MultiTextConcatenate` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Text _O` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
