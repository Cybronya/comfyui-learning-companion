---
name: image_to_image_lora_sampler_clip_142
type: Image To Image
frequency: 2
level: weak
coverage: 0.8605
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, FluxGuidance, Image Comparer (rgthree), ImpactInt, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux2透视溶图，光影融合，物体高清放大_2094369813144629250.json, 图片生成/图生图/溶图打光超绝一致性_2037708314812878850.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux2透视溶图，光影融合，物体高清放大_2094369813144629250.json、图片生成/图生图/溶图打光超绝一致性_2037708314812878850.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `Float` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `InversionDemoLazySwitch` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `workflow>加密节点` —— 1/2 个有
- `workflow>加密节点2` —— 1/2 个有
- `workflow>加密节点3` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
