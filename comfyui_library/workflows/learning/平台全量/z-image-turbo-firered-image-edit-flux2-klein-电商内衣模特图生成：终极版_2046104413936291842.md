---
key: 平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842.json
name: z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842.json
hash: 5158d61e813cd1ed
coverage: 0.967033
learned_at: 2026-11-14 01:20:34
nodes: [KSamplerSelect, DetailDaemonSamplerNode, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, CFGNorm, VAEDecode, SplitSigmas, CLIPTextEncode, KSamplerSelect, SamplerCustomAdvanced, ModelPatchLoader, CLIPLoader_Any, VAELoader_Any, CLIPLoader_Any, VAEEncode, KSamplerSelect, BasicGuider, BasicScheduler, DetailDaemonSamplerNode, ModelSamplingAuraFlow, SamplerCustom, SamplerCustom, UNETLoader_Any, ModelSamplingAuraFlow, SamplerCustom, ImitationHueNode, AIO_Preprocessor, CLIPTextEncode, ImageScaleToTotalPixelsX, ReferenceLatent, BasicScheduler, VAEDecode, ReferenceLatent, ReferenceLatent, ImageScaleToTotalPixelsX, AILab_QwenVL, VAEEncode, VAEEncode, BasicGuider, KSamplerSelect, VAEEncode, CFGNorm, easy imageSize, PreviewImage, EmptyFlux2LatentImage, ImageScaleToTotalPixelsX, LoadImage, ImageScaleToTotalPixelsX, RandomNoise, LoadImage, ImageScaleToTotalPixelsX, VAELoader_Any, SAM3Segment, ReActorFaceSwap, SetLatentNoiseMask, AILab_QwenVL, VAEEncode, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixelsX, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixelsX, DWPreprocessor, ReferenceLatent, easy imageSizeBySide, easy cleanGpuUsed, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, VAEEncode, InpaintStitchImproved, InpaintCropImproved, Flux2Scheduler, PreviewImage, BasicScheduler, PreviewImage, VAEDecode, ImitationHueNode, SaveImage, VAEDecode, LoraLoaderModelOnly, UNETLoader_Any, ZImageFunControlnet, LoadImage, Seed (rgthree), CLIPTextEncode, CLIPTextEncode, Seed (rgthree), LoadImage, RandomNoise]
patterns: []
missing: []
---

# 平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842.json

> 来源文件 `comfyui_library/workflows/平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商内衣模特图生成：终极版_2046104413936291842.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `KSamplerSelect` ★核心
- `DetailDaemonSamplerNode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `VAEDecode` ★核心
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelPatchLoader`
- `CLIPLoader_Any`
- `VAELoader_Any`
- `CLIPLoader_Any`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `BasicScheduler`
- `DetailDaemonSamplerNode` ★核心
- `ModelSamplingAuraFlow`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `UNETLoader_Any` ★核心
- `ModelSamplingAuraFlow`
- `SamplerCustom` ★核心
- `ImitationHueNode`
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixelsX`
- `ReferenceLatent`
- `BasicScheduler`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageScaleToTotalPixelsX`
- `AILab_QwenVL`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `CFGNorm`
- `easy imageSize`
- `PreviewImage`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixelsX`
- `LoadImage`
- `ImageScaleToTotalPixelsX`
- `RandomNoise`
- `LoadImage`
- `ImageScaleToTotalPixelsX`
- `VAELoader_Any`
- `SAM3Segment`
- `ReActorFaceSwap`
- `SetLatentNoiseMask`
- `AILab_QwenVL`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixelsX`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixelsX`
- `DWPreprocessor`
- `ReferenceLatent`
- `easy imageSizeBySide`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `InpaintStitchImproved`
- `InpaintCropImproved`
- `Flux2Scheduler`
- `PreviewImage`
- `BasicScheduler`
- `PreviewImage`
- `VAEDecode` ★核心
- `ImitationHueNode`
- `SaveImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader_Any` ★核心
- `ZImageFunControlnet`
- `LoadImage`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `LoadImage`
- `RandomNoise`

## 知识

覆盖率 **97%**（88/91）

**有卡**：`KSamplerSelect`、`DetailDaemonSamplerNode`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`VAEDecode`、`SplitSigmas`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`ModelPatchLoader`、`CLIPLoader_Any`、`VAELoader_Any`、`VAEEncode`、`BasicGuider`、`BasicScheduler`、`ModelSamplingAuraFlow`、`SamplerCustom`、`UNETLoader_Any`、`ImitationHueNode`、`AIO_Preprocessor`、`ImageScaleToTotalPixelsX`、`ReferenceLatent`、`AILab_QwenVL`、`easy imageSize`、`EmptyFlux2LatentImage`、`LoadImage`、`RandomNoise`、`SAM3Segment`、`ReActorFaceSwap`、`SetLatentNoiseMask`、`TextEncodeQwenImageEditPlus`、`DWPreprocessor`、`easy imageSizeBySide`、`easy cleanGpuUsed`、`InpaintStitchImproved`、`InpaintCropImproved`、`Flux2Scheduler`、`SaveImage`、`ZImageFunControlnet`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、ZImageFunControlnet
