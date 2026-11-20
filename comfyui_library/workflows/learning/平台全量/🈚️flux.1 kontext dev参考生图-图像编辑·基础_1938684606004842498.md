---
key: 平台全量/🈚️flux.1 kontext dev参考生图-图像编辑·基础_1938684606004842498.json
name: 🈚️flux.1 kontext dev参考生图-图像编辑·基础_1938684606004842498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️flux.1 kontext dev参考生图-图像编辑·基础_1938684606004842498.json
hash: c5205b07f4c4af7d
coverage: 0.55914
learned_at: 2026-11-14 02:54:27
nodes: [CLIPTextEncode, FluxGuidance, GetNode, SetNode, SetNode, VAELoader, GetNode, GetNode, VAEEncode, SetNode, SetNode, BasicGuider, GetNode, SamplerCustomAdvanced, VAEDecode, SetNode, GetNode, VAEDecode, KSamplerSelect, BasicGuider, UpscaleModelLoader, LatentPixelScale, BasicScheduler, InjectLatentNoise+, MarkdownNote, MarkdownNote, GetNode, SamplerCustomAdvanced, SetNode, GetNode, GetNode, RandomNoise, ModelSamplingFlux, GetNode, SetNode, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, easy imageConcat, SaveImage, MarkdownNote, RandomNoise, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, LoadImage, GetNode, GetNode, GetNode, LoadImage, Image Comparer (rgthree), DeepTranslatorTextNode, SaveImage, ImageConcanate, LoadImage, LoadImage, RH_ComfyFluxKontext, easy imageScaleDownToSize, Text Multiline, Text Multiline, Image Comparer (rgthree), DeepTranslatorTextNode, SaveImage, RH_ComfyFluxKontext, LoadImage, Text Multiline, SetNode, LoraLoaderModelOnly, UNETLoader, NunchakuFluxDiTLoader, DualCLIPLoader, ShowText|pysssss, LoadKontextPresets, LoraLoaderModelOnly, LoraLoaderModelOnly, ReferenceLatent, SetNode, BasicScheduler, KSamplerSelect, CR Aspect Ratio, FluxKontextImageScale, PreviewImage, SetNode, RH_Translator]
patterns: []
missing: []
---

# 平台全量/🈚️flux.1 kontext dev参考生图-图像编辑·基础_1938684606004842498.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️flux.1 kontext dev参考生图-图像编辑·基础_1938684606004842498.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `SetNode`
- `BasicGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `UpscaleModelLoader`
- `LatentPixelScale`
- `BasicScheduler`
- `InjectLatentNoise+`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `ModelSamplingFlux`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy imageConcat`
- `SaveImage`
- `MarkdownNote`
- `RandomNoise`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Image Comparer (rgthree)`
- `DeepTranslatorTextNode`
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `LoadImage`
- `RH_ComfyFluxKontext`
- `easy imageScaleDownToSize`
- `Text Multiline`
- `Text Multiline`
- `Image Comparer (rgthree)`
- `DeepTranslatorTextNode`
- `SaveImage`
- `RH_ComfyFluxKontext`
- `LoadImage`
- `Text Multiline`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `ShowText|pysssss`
- `LoadKontextPresets`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `SetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `CR Aspect Ratio`
- `FluxKontextImageScale`
- `PreviewImage`
- `SetNode`
- `RH_Translator`

## 知识

覆盖率 **56%**（52/93）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`VAELoader`、`VAEEncode`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`KSamplerSelect`、`UpscaleModelLoader`、`LatentPixelScale`、`BasicScheduler`、`InjectLatentNoise+`、`RandomNoise`、`ModelSamplingFlux`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageConcat`、`SaveImage`、`LoadImage`、`DeepTranslatorTextNode`、`ImageConcanate`、`RH_ComfyFluxKontext`、`easy imageScaleDownToSize`、`Text Multiline`、`LoraLoaderModelOnly`、`UNETLoader`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`LoadKontextPresets`、`ReferenceLatent`、`CR Aspect Ratio`、`FluxKontextImageScale`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
