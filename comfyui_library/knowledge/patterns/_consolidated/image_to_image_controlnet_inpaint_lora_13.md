---
name: image_to_image_controlnet_inpaint_lora_13
type: Image To Image
frequency: 3
level: moderate
coverage: 0.509
common_nodes: [Anything Everywhere, ApplyInstantID, BlockifyMask, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetLoader, DWPreprocessor, DifferentialDiffusion, FluxGuidance, GetImageSize, GetNode, ImageAndMaskPreview, ImageCompositeMasked, ImageSmartSharpen+, ImpactConditionalBranch, ImpactSwitch, InpaintCropImproved, InpaintModelConditioning, InpaintStitchImproved, InstantIDFaceAnalysis, InstantIDModelLoader, Int, InvertMask (segment anything), KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, MaskToSEGS, PIP_图像联结, PreviewImage, RebatchLatents, ReferenceLatent, RepeatLatentBatch, SaveImage, SegsToCombinedMask, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy imageRemBg, easy seed, workflow>mask mover]
problems: []
missing: []
members: [平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585.json, 平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185.json, 平台全量/🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「垫图重绘版」_2012476314279747585.json、平台全量/Flux.2 klein 换头_换脸_人脸参考IP-局部重绘-聚焦裁剪「色块填充版」_2013655608490205185.json、平台全量/🈚️flux.1 kontext dev-局部重绘-换头_换脸_1955488211936186370.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `ApplyInstantID`
- `BlockifyMask`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DWPreprocessor`
- `DifferentialDiffusion`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImageSmartSharpen+`
- `ImpactConditionalBranch`
- `ImpactSwitch`
- `InpaintCropImproved`
- `InpaintModelConditioning`
- `InpaintStitchImproved`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `Int`
- `InvertMask (segment anything)`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToSEGS`
- `PIP_图像联结`
- `PreviewImage`
- `RebatchLatents`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `SegsToCombinedMask`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy imageRemBg`
- `easy seed`
- `workflow>mask mover`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `CLIPLoader` —— 2/3 个有
- `DrawMaskOnImage` —— 2/3 个有
- `Flux2Scheduler` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `LayerMask: MaskPreview` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `ControlNetApplySD3` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `EmptyFlux2LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LG_Color_Match_V2` —— 1/3 个有
- `LayerFilter: FilmV2` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有
- `TeaCache` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 3 | 72% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 1.5 | 3 | 82% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.5 - 0.8 | 3 | 76% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 1.5，3 个样本，取值集中（一致性 82%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.5 - 0.8，3 个样本
