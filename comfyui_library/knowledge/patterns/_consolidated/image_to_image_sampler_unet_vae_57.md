---
name: image_to_image_sampler_unet_vae_57
type: Image To Image
frequency: 2
level: weak
coverage: 0.867
common_nodes: [AILab_QwenVL, CLIPLoader, CR Text Replace, ConditioningZeroOut, Image Comparer (rgthree), InspyrenetRembg, KSampler, LayerUtility: ImageRemoveAlpha, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/电商人必冲-Flux2-Klein-9B-产品换背景_2014326310281154561.json, 图片生成/图生图/电商人必冲Qwen-edit-2511产品换背景快准狠_2014689708055470081.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_57

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/电商人必冲-Flux2-Klein-9B-产品换背景_2014326310281154561.json、图片生成/图生图/电商人必冲Qwen-edit-2511产品换背景快准狠_2014689708055470081.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CR Text Replace`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `InspyrenetRembg`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `Text` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
