---
name: text_to_image_lora_sampler_clip_561
type: Text To Image
frequency: 3
level: strong
coverage: 0.939667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, Seed (rgthree), Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image全功能+网红美女爆图工作流_1995507321415598081.json, 图片生成/文生图/z-image_一张图片一次性洗多张一致性图片_1996107207425114113.json, 图片生成/文生图/美女模特 反推提示词 图片裂变 9宫格分镜图 洗图  Z-Image-Turbo D-OPSD_2056920485178462210.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_561

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image全功能+网红美女爆图工作流_1995507321415598081.json、图片生成/文生图/z-image_一张图片一次性洗多张一致性图片_1996107207425114113.json、图片生成/文生图/美女模特 反推提示词 图片裂变 9宫格分镜图 洗图  Z-Image-Turbo D-OPSD_2056920485178462210.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `MaskBlur+` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PreviewAny` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.85 - 1 | 3 | 93% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，3 个样本，取值集中（一致性 93%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
