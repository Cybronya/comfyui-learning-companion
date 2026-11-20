---
name: unknown_workflow_lora_sampler_clip_369
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7265
common_nodes: [Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, ConstrainImage|pysssss, DualCLIPLoader, EmptySD3LatentImage, FastCanvas, FastCanvasTool, FluxGuidance, GetImageSize, GetNode, Image Comparer (rgthree), Int, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RH_Translator, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Kontext 溶图_为产品生产海报_Nunchaku 加速_1938861536792207361.json, 平台全量/kontext-溶图V2_1955427457908314114.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_369

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Kontext 溶图_为产品生产海报_Nunchaku 加速_1938861536792207361.json、平台全量/kontext-溶图V2_1955427457908314114.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `Int`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Color Panel` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImageCropper` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `LayerUtility: ImageOpacity` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
