---
name: image_to_image_controlnet_inpaint_upscale_7
type: Image To Image
frequency: 2
level: weak
coverage: 0.6625
common_nodes: [Any Switch (rgthree), Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Simple Image Compare, CheckpointLoaderSimple, ConditioningZeroOut, ConstrainImage|pysssss, ControlNetApplySD3, ControlNetLoader, DownloadAndLoadFlorence2Model, DualCLIPLoader, Fast Bypasser (rgthree), Florence2Run, FluxGuidance, GetImageSize+, GetNode, GoogleTranslateTextNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, Image Blend by Mask, Image Comparer (rgthree), ImageRemoveAlpha+, ImageResize+, ImageUpscaleWithModel, InpaintModelConditioning, InvertMask, KSampler, Label (rgthree), LoadImage, LoraLoaderModelOnly, MaskBlur+, MaskToImage, MathExpression|pysssss, PreviewImage, RMBG, RemBGSession+, SAMModelLoader (segment anything), SaveImage, SetNode, ShowText|pysssss, SimpleMath+, StringFunction|pysssss, StyleModelApply, StyleModelLoader, TiledDiffusion, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEDecodeTiled_TiledDiffusion, VAEEncode, VAEEncodeTiled_TiledDiffusion, VAELoader, easy promptReplace, ttN text]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux影楼专用一键更换背景_1924438961127944194.json, 平台全量/影楼专用一键更换背景.FLUX_1891877630654767106.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux影楼专用一键更换背景_1924438961127944194.json、平台全量/影楼专用一键更换背景.FLUX_1891877630654767106.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Simple Image Compare`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Fast Bypasser (rgthree)`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `GetNode`
- `GoogleTranslateTextNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `Image Blend by Mask`
- `Image Comparer (rgthree)`
- `ImageRemoveAlpha+`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RMBG`
- `RemBGSession+`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringFunction|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `TiledDiffusion`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled_TiledDiffusion`
- `VAEEncode`
- `VAEEncodeTiled_TiledDiffusion`
- `VAELoader`
- `easy promptReplace`
- `ttN text`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.15 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
