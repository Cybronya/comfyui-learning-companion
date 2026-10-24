---
name: unknown_workflow_lora_sampler_unet_83
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.82125
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_edit_2509童装上身工作流_2010558260528553985.json, 图片生成/图生图/【阡陌】 Qwen-Imag-eEdit 图像编辑解决偏移问题_1969954034549485570.json, 图片生成/图生图/千问edit一致性编辑（小志jason开源）_1968291733631053826.json, 图片生成/图生图/千问编辑Plus-小志一致性优化版_1971874296203243521.json, 图片生成/图生图/商用级PS+QwenEdit2509电商产品图_2043845775716786177.json, 图片生成/图生图/更改服装Change clothes_2043630491630313473.json, 图片生成/图生图/超级模特换装展示-图生图_2066382280444174338.json, 图片生成/图生图/👾怪獸-千问桌面手办👾_1982436024448098306.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_83

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/qwen_edit_2509童装上身工作流_2010558260528553985.json、图片生成/图生图/【阡陌】 Qwen-Imag-eEdit 图像编辑解决偏移问题_1969954034549485570.json、图片生成/图生图/千问edit一致性编辑（小志jason开源）_1968291733631053826.json、图片生成/图生图/千问编辑Plus-小志一致性优化版_1971874296203243521.json、图片生成/图生图/商用级PS+QwenEdit2509电商产品图_2043845775716786177.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `CFGNorm` —— 6/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 5/8 个有
- `CR Text` —— 3/8 个有
- `GetNode` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 2/8 个有
- `Easy_QwenEdit2509` —— 1/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `TextInputNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 8 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，8 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
