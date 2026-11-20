---
name: unknown_workflow_lora_sampler_unet_35
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.6464
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2509真人风格转换_1991357384436088834.json, 图片生成/图生图/QwenEdit2511风格转写实（一致性）_2010967343677054977.json, 图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json, 图片生成/图生图/Qwen换装-图生图-衣物迁移_1992841662271647746.json, 图片生成/图生图/qwen-edit-2511电商服饰替换_2093978256927182850.json, 图片生成/图生图/【全自动换装+超强一致性】_2040251598290558978.json, 图片生成/图生图/一键换装增强版：完美替换衣物，人物一致性_2086810156494577666.json, 图片生成/图生图/全自动换装+超强一致性_1994552832286134274.json, 图片生成/图生图/千问 无遮罩控制 全自动换装_2000220845391872001.json, 图片生成/图生图/千问2511高清4k换装，全自动换装+超强一致性（单图35Mb）_2026664684333568001.json, 图片生成/图生图/千问换装【全自动换装+超强一致性】_1990256833518596097.json, 图片生成/文生图/千问【全自动换装+超强一致性】_2000213218951917569.json, 平台全量/Qwen edit 全自动换装 千问 无需遮罩控制  换装换脸_2019255178779693057.json, 平台全量/qwen2509全自动千问换装换装超强一致性_2004748601836404738.json, 平台全量/【精准换装】Qwen 自动换装 千问写实摄影时装秀 杂志封面海报 人物一致换装 完美换脸换装_2015259071531720706.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_35

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/QwenEdit2509真人风格转换_1991357384436088834.json、图片生成/图生图/QwenEdit2511风格转写实（一致性）_2010967343677054977.json、图片生成/图生图/QwenEditUtils 2.2 Optional Mask换装-(适合全身换)_1992103898848751617.json、图片生成/图生图/Qwen换装-图生图-衣物迁移_1992841662271647746.json、图片生成/图生图/qwen-edit-2511电商服饰替换_2093978256927182850.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 15 个 workflow 都包含：
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
- `CropWithPadInfo` —— 13/15 个有
- `Image Comparer (rgthree)` —— 13/15 个有
- `PrimitiveStringMultiline` —— 13/15 个有
- `QwenEditAdaptiveLongestEdge` —— 12/15 个有
- `GetNode` —— 11/15 个有
- `ImageScaleBy` —— 11/15 个有
- `SetNode` —— 11/15 个有
- `Seed (rgthree)` —— 10/15 个有
- `CFGNorm` —— 2/15 个有
- `ImageScaleToTotalPixels` —— 2/15 个有
- `ModelSamplingAuraFlow` —— 2/15 个有
- `SeedVR2` —— 2/15 个有
- `SeedVR2BlockSwap` —— 2/15 个有
- `SeedVR2ExtraArgs` —— 2/15 个有
- `ImageUpscaleWithModel` —— 1/15 个有
- `UpscaleModelLoader` —— 1/15 个有
- `easy imageConcat` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 15 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | beta57 | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 beta57，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
