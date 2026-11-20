---
name: unknown_workflow_lora_sampler_unet_41
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.6765
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2509真人风格转换_1991357384436088834.json, 图片生成/图生图/QwenEdit2511风格转写实（一致性）_2010967343677054977.json, 图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json, 图片生成/图生图/Qwen换装-图生图-衣物迁移_1992841662271647746.json, 图片生成/图生图/qwen-edit-2511电商服饰替换_2093978256927182850.json, 图片生成/图生图/【全自动换装+超强一致性】_2040251598290558978.json, 图片生成/图生图/一键换装增强版：完美替换衣物，人物一致性_2086810156494577666.json, 图片生成/图生图/全自动换装+超强一致性_1994552832286134274.json, 图片生成/图生图/千问 无遮罩控制 全自动换装_2000220845391872001.json, 图片生成/图生图/千问2511高清4k换装，全自动换装+超强一致性（单图35Mb）_2026664684333568001.json, 图片生成/图生图/千问换装【全自动换装+超强一致性】_1990256833518596097.json, 图片生成/文生图/千问【全自动换装+超强一致性】_2000213218951917569.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/QwenEdit2509真人风格转换_1991357384436088834.json、图片生成/图生图/QwenEdit2511风格转写实（一致性）_2010967343677054977.json、图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json、图片生成/图生图/Qwen换装-图生图-衣物迁移_1992841662271647746.json、图片生成/图生图/qwen-edit-2511电商服饰替换_2093978256927182850.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 10/12 个有
- `Image Comparer (rgthree)` —— 10/12 个有
- `PrimitiveStringMultiline` —— 10/12 个有
- `QwenEditAdaptiveLongestEdge` —— 9/12 个有
- `GetNode` —— 8/12 个有
- `ImageScaleBy` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `Seed (rgthree)` —— 7/12 个有
- `CFGNorm` —— 2/12 个有
- `ImageScaleToTotalPixels` —— 2/12 个有
- `ModelSamplingAuraFlow` —— 2/12 个有
- `SeedVR2` —— 2/12 个有
- `SeedVR2BlockSwap` —— 2/12 个有
- `SeedVR2ExtraArgs` —— 2/12 个有
- `ImageUpscaleWithModel` —— 1/12 个有
- `UpscaleModelLoader` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 12 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | beta57 | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 beta57，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
