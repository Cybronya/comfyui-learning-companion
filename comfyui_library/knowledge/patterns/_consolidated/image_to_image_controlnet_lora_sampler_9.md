---
name: image_to_image_controlnet_lora_sampler_9
type: Image To Image
frequency: 3
level: moderate
coverage: 0.908667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EG_ZZ_TMTX, EmptySD3LatentImage, FluxGuidance, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), ImageScale, KSampler, LayerFilter: GaussianBlur, LayerUtility: AnyRerouter, LayerUtility: FluxKontextImageScale, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RMBG, ReferenceLatent, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/千问+kontext电商主图制作_1961306981845897217.json, 图片生成/图生图/电商主图制作（无需PS）_1966026089309048834.json, 图片生成/图生图/白底图制作电商主图_1969068163621154817.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问+kontext电商主图制作_1961306981845897217.json、图片生成/图生图/电商主图制作（无需PS）_1966026089309048834.json、图片生成/图生图/白底图制作电商主图_1969068163621154817.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EG_ZZ_TMTX`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageScale`
- `KSampler`
- `LayerFilter: GaussianBlur`
- `LayerUtility: AnyRerouter`
- `LayerUtility: FluxKontextImageScale`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RMBG`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `BatchCropFromMask` —— 1/3 个有
- `CR Overlay Text` —— 1/3 个有
- `FastCanvas` —— 1/3 个有
- `FastCanvasTool` —— 1/3 个有
- `LayerMask: RmBgUltra V2` —— 1/3 个有
- `LayerUtility: ColorImage` —— 1/3 个有
- `LayerUtility: ImageBlend` —— 1/3 个有
- `LayerUtility: ImageBlendAdvance` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 1 | 3 | 74% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 3 | 65% |
| 采样算法 | res_2s | - | 3 | 67% |
| 调度器 | beta | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 1，3 个样本
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 res_2s，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
