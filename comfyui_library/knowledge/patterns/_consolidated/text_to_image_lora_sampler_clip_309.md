---
name: text_to_image_lora_sampler_clip_309
type: Text To Image
frequency: 3
level: moderate
coverage: 0.841333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, KSamplerAdvanced, LayerFilter: HDREffects, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json, 图片生成/文生图/wan2.2 高噪 + Z-image 文生图（分段采样）_2009428216460611585.json, 图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_309

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json、图片生成/文生图/wan2.2 高噪 + Z-image 文生图（分段采样）_2009428216460611585.json、图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerAdvanced`
- `LayerFilter: HDREffects`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `InversionDemoLazyIndexSwitch` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `Text` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 10 | 1 - 10 | 3 | 39% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | sgm_uniform | - | 3 | 67% |
| 宽度 | 960 | 960 - 1728 | 3 | 70% |
| 高度 | 1536 | 1536 - 2304 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 1 - 10，3 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 sgm_uniform，3 个样本，一致性 67%
- 宽度 中位数 960，观测区间 960 - 1728，3 个样本
- 高度 中位数 1536，观测区间 1536 - 2304，3 个样本
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
