---
name: image_to_image_controlnet_inpaint_lora_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.8175
common_nodes: [ACN_AdvancedControlNetApply, ApplyPulidFlux, Automatic CFG, BasicGuider, BasicScheduler, BboxDetectorSEGS, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConcatText_Zho, ControlNetLoaderAdvanced, DualCLIPLoader, FluxGuidance, GetNode, GrowMask, ImageComposite+, ImageCrop+, ImageResize+, InpaintModelConditioning, KSampler, KSamplerSelect, Label (rgthree), LoadImage, LoraLoaderModelOnly, Mask Crop Region, MaskBlur+, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RandomNoise, SAMDetectorCombined, SAMLoader, SamplerCustom, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, UltralyticsDetectorProvider, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy getNode, easy setNode]
problems: []
missing: []
members: [平台全量/一键换脸粘土风格_1849651042085466114.json, 平台全量/石塑黏土人偶_1847158852583297026.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/一键换脸粘土风格_1849651042085466114.json、平台全量/石塑黏土人偶_1847158852583297026.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `ApplyPulidFlux`
- `Automatic CFG`
- `BasicGuider`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConcatText_Zho`
- `ControlNetLoaderAdvanced`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `GrowMask`
- `ImageComposite+`
- `ImageCrop+`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Crop Region`
- `MaskBlur+`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RandomNoise`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustom`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UltralyticsDetectorProvider`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Crop Face` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Load RetinaFace` —— 1/2 个有
- `MaskToImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral_cfg_pp | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.565 | - | 2 | 94% |
| ControlNet 权重 | 0.95 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral_cfg_pp，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.565，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- ControlNet 权重 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
