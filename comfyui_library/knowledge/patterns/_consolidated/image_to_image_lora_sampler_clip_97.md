---
name: image_to_image_lora_sampler_clip_97
type: Image To Image
frequency: 3
level: strong
coverage: 0.88
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, Image Comparer (rgthree), KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/QY7-千像归一（kontext）双图版 自动抠图一键融合打光，溶图kontext_1967598647435288578.json, 图片生成/图生图/kontext 产品融合场景2.0 (光影lora)_1954190048486944770.json, 图片生成/图生图/kontext产品溶图_1966031556299100161.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_97

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QY7-千像归一（kontext）双图版 自动抠图一键融合打光，溶图kontext_1967598647435288578.json、图片生成/图生图/kontext 产品融合场景2.0 (光影lora)_1954190048486944770.json、图片生成/图生图/kontext产品溶图_1966031556299100161.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DetailTransfer` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LayerUtility: FluxKontextImageScale` —— 1/3 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy imageDetailTransfer` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | deis | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
