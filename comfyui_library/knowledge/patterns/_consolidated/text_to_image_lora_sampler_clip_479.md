---
name: text_to_image_lora_sampler_clip_479
type: Text To Image
frequency: 4
level: moderate
coverage: 0.83625
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570.json, 图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json, 图片生成/文生图/wan2.2 高噪 + Z-image 文生图（分段采样）_2009428216460611585.json, 图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_479

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/ernie turbo + wan2.2 高噪 + Z-image 三阶采样 多样性超写实 文生图_2044692195583725570.json、图片生成/文生图/wan2.2 低噪 + Z-image 文生图（分段采样）_2009498340953690113.json、图片生成/文生图/wan2.2 高噪 + Z-image 文生图（分段采样）_2009428216460611585.json、图片生成/文生图/写实皮肤wan2.2 t2v+Z-image超真实文生图_2015804951070515201.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerAdvanced`
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
- `CheckpointLoaderSimple` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `InversionDemoLazyIndexSwitch` —— 3/4 个有
- `LayerFilter: HDREffects` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `Text` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 10 | 1 - 10 | 4 | 50% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 4 | 75% |
| 重绘幅度 | sgm_uniform | - | 4 | 75% |
| 宽度 | 960 | 960 - 1728 | 4 | 71% |
| 高度 | 1536 | 1536 - 2304 | 4 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 10，观测区间 1 - 10，4 个样本，取值分散，一致性仅 50%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 75%
- 重绘幅度 最常用 sgm_uniform，4 个样本，一致性 75%
- 宽度 中位数 960，观测区间 960 - 1728，4 个样本
- 高度 中位数 1536，观测区间 1536 - 2304，4 个样本，取值集中（一致性 81%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
