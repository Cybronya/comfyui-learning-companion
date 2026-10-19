---
name: text_to_image_upscale_lora_sampler_30
type: Text To Image
frequency: 2
level: weak
coverage: 0.7705
common_nodes: [CLIPTextEncode, CR Latent Batch Size, CR Latent Input Switch, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, ImageUpscaleWithModel, ImpactInt, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: CropByMask V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, ResizeLongestToNode, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerMask: SegformerB2ClothesUltra, LayerUtility: CropByMask V2, CR Latent Batch Size, CR Latent Input Switch, LayerUtility: ImageAutoCrop V2]
members: [图片生成/文生图/1967455597295702017.json, 图片生成/文生图/1989951791611736065.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1967455597295702017.json、图片生成/文生图/1989951791611736065.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `CR Latent Input Switch`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `ResizeLongestToNode`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageAutoCrop V2` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1104 | - | 2 | 70% |
| 高度 | 1232 | - | 2 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1104，样本不足，未给区间，2 个样本
- 高度 中位数 1232，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: SegformerB2ClothesUltra、LayerUtility: CropByMask V2、CR Latent Batch Size、CR Latent Input Switch、LayerUtility: ImageAutoCrop V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
