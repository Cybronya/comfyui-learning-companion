---
key: 图片生成/图生图/FLUX.krea真实皮肤质感_1971483655719862274.json
name: FLUX.krea真实皮肤质感_1971483655719862274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.krea真实皮肤质感_1971483655719862274.json
hash: 9be972a660ee085c
coverage: 0.944444
learned_at: 2026-10-23 10:54:17
nodes: [MaskPreview+, easy imageSize, MaskToImage, Colored Image (mtb), MaskToImage, LayerUtility: ImageBlendAdvance, ImageToMask, FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParse(FaceParsing), NunchakuTextEncoderLoaderV2, VAELoader, CLIPTextEncode, CLIPTextEncode, RandomNoise, KSamplerSelect, FluxGuidance, BasicGuider, SamplerCustomAdvanced, VAEDecode, LayerMask: MaskPreview, ImpactGaussianBlurMask, SaveImage, InpaintModelConditioning, Image Comparer (rgthree), PreviewImage, MaskPreview+, LayerUtility: ImageBlendAdvance, Colored Image (mtb), LayerUtility: ImageBlendAdvance, NunchakuFluxDiTLoader, FaceParsingResultsParser(FaceParsing), FaceParsingResultsParser(FaceParsing), BasicScheduler, AdvancedLyingSigmaSampler, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.krea真实皮肤质感_1971483655719862274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.krea真实皮肤质感_1971483655719862274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `MaskPreview+`
- `easy imageSize`
- `MaskToImage`
- `Colored Image (mtb)`
- `MaskToImage`
- `LayerUtility: ImageBlendAdvance`
- `ImageToMask`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParse(FaceParsing)`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerMask: MaskPreview`
- `ImpactGaussianBlurMask`
- `SaveImage`
- `InpaintModelConditioning`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `MaskPreview+`
- `LayerUtility: ImageBlendAdvance`
- `Colored Image (mtb)`
- `LayerUtility: ImageBlendAdvance`
- `NunchakuFluxDiTLoader`
- `FaceParsingResultsParser(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `BasicScheduler`
- `AdvancedLyingSigmaSampler` ★核心
- `LoadImage`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`MaskPreview+`、`easy imageSize`、`MaskToImage`、`Colored Image (mtb)`、`LayerUtility: ImageBlendAdvance`、`ImageToMask`、`FaceParsingModelLoader(FaceParsing)`、`FaceParsingProcessorLoader(FaceParsing)`、`FaceParse(FaceParsing)`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`FluxGuidance`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`LayerMask: MaskPreview`、`ImpactGaussianBlurMask`、`SaveImage`、`InpaintModelConditioning`、`NunchakuFluxDiTLoader`、`FaceParsingResultsParser(FaceParsing)`、`BasicScheduler`、`AdvancedLyingSigmaSampler`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、AdvancedLyingSigmaSampler
