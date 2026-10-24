---
name: image_to_image_controlnet_inpaint_sampler_4
type: Image To Image
frequency: 3
level: strong
coverage: 0.616
common_nodes: [Any Switch (rgthree), ApplyInstantIDAdvanced, BasicScheduler, BboxDetectorSEGS, Bookmark (rgthree), Bounded Image Blend, Bounded Image Crop with Mask, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, DetailDaemonSamplerNode, DifferentialDiffusion, Fast Groups Bypasser (rgthree), FreeU_V2, GetNode, Image Comparer (rgthree), ImageRandomTransform+, ImageResize+, ImageToMask, ImpactMakeImageBatch, InpaintModelConditioning, InstantIDModelLoader, JWImageResizeByLongerSide, JWMaskResize, JoinStrings, KSampler, KSamplerSelect, Label (rgthree), LayerMask: MaskEdgeUltraDetail V2, LayerMask: MaskGrow, LineArtPreprocessor, LoadImage, Mask Fill Holes, MaskPreview+, MaskToImage, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Note Plus (mtb), PatchModelAddDownscale, PreviewImage, PulidInsightFaceLoader, RandomNoise, ReActorFaceSwap, RemapMaskRange, SAMDetectorCombined, SAMLoader, SamplerCustomAdvanced, SaveImage, SetNode, String Literal, TextCombinerSix, UltralyticsDetectorProvider, VAEDecode, VAEEncode, easy float, easy imageSize, easy int, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/一键动漫转真人_1972138616271138817.json, 图片生成/图生图/影楼级cos漫画转真人V1-基础版-阿硕_1895686697588293633.json, 图片生成/图生图/影楼级cos漫画转真人V1-基础版_1896558634426621954.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键动漫转真人_1972138616271138817.json、图片生成/图生图/影楼级cos漫画转真人V1-基础版-阿硕_1895686697588293633.json、图片生成/图生图/影楼级cos漫画转真人V1-基础版_1896558634426621954.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ApplyInstantIDAdvanced`
- `BasicScheduler`
- `BboxDetectorSEGS`
- `Bookmark (rgthree)`
- `Bounded Image Blend`
- `Bounded Image Crop with Mask`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailDaemonSamplerNode`
- `DifferentialDiffusion`
- `Fast Groups Bypasser (rgthree)`
- `FreeU_V2`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageRandomTransform+`
- `ImageResize+`
- `ImageToMask`
- `ImpactMakeImageBatch`
- `InpaintModelConditioning`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWMaskResize`
- `JoinStrings`
- `KSampler`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerMask: MaskEdgeUltraDetail V2`
- `LayerMask: MaskGrow`
- `LineArtPreprocessor`
- `LoadImage`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Note Plus (mtb)`
- `PatchModelAddDownscale`
- `PreviewImage`
- `PulidInsightFaceLoader`
- `RandomNoise`
- `ReActorFaceSwap`
- `RemapMaskRange`
- `SAMDetectorCombined`
- `SAMLoader`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `String Literal`
- `TextCombinerSix`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `easy float`
- `easy imageSize`
- `easy int`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `WD14Tagger|pysssss` —— 2/3 个有
- `RH_Captioner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.75 | 0.75 - 0.75 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.44 | 0.44 - 0.44 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.75，观测区间 0.75 - 0.75，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.44，观测区间 0.44 - 0.44，3 个样本，取值集中（一致性 100%）
