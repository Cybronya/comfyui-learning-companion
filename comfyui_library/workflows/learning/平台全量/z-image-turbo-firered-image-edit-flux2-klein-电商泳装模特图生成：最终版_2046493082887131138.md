---
key: 平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138.json
name: z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138.json
hash: c412f7afd0a13514
coverage: 0.924731
learned_at: 2026-11-14 01:20:35
nodes: [VAEDecode, SplitSigmas, CLIPTextEncode, KSamplerSelect, SamplerCustomAdvanced, ModelPatchLoader, CLIPLoader_Any, VAEEncode, KSamplerSelect, BasicGuider, ReferenceLatent, DetailDaemonSamplerNode, ModelSamplingAuraFlow, SamplerCustom, UNETLoader_Any, ImitationHueNode, SetLatentNoiseMask, CLIPTextEncode, ImageScaleToTotalPixelsX, VAEEncode, ReferenceLatent, BasicScheduler, ReferenceLatent, ReferenceLatent, VAEEncode, VAEEncode, BasicGuider, EmptyFlux2LatentImage, ReActorFaceSwap, VAEEncode, Flux2Scheduler, VAELoader_Any, CFGNorm, InpaintCropImproved, SAM3Segment, AILab_QwenVL, BasicScheduler, ImageScaleToTotalPixelsX, VAEDecode, InpaintStitchImproved, VAEDecode, ImageScaleToTotalPixelsX, easy imageSize, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, VAELoader_Any, UNETLoader_Any, ZImageFunControlnet, Seed (rgthree), AIO_Preprocessor, easy imageSizeBySide, SamplerCustom, DetailDaemonSamplerNode, CFGNorm, BasicScheduler, ModelSamplingAuraFlow, VAEEncode, AILab_QwenVL, PreviewImage, easy cleanGpuUsed, DWPreprocessor, PreviewImage, ImageScaleToTotalPixelsX, ImageScaleToTotalPixelsX, VAEDecode, SamplerCustom, CLIPLoader_Any, CLIPLoader_Any, VAELoader_Any, RandomNoise, RandomNoise, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSamplerSelect, LoraLoaderModelOnly, CLIPTextEncode, LoadImage, LoadImage, UNETLoader_Any, LoraLoaderModelOnly, LoadImage, LoadImage, easy ifElse, ColorBalanceNode, PreviewImage, Seed (rgthree), CLIPTextEncode, SamplerCustomAdvanced, SaveImage, KSamplerSelect, easy ifElse, easy ifElse, easy ifElse]
patterns: []
missing: []
---

# 平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138.json

> 来源文件 `comfyui_library/workflows/平台全量/z-image-turbo-firered-image-edit-flux2-klein-电商泳装模特图生成：最终版_2046493082887131138.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `VAEDecode` ★核心
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelPatchLoader`
- `CLIPLoader_Any`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `DetailDaemonSamplerNode` ★核心
- `ModelSamplingAuraFlow`
- `SamplerCustom` ★核心
- `UNETLoader_Any` ★核心
- `ImitationHueNode`
- `SetLatentNoiseMask`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixelsX`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `BasicScheduler`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `EmptyFlux2LatentImage`
- `ReActorFaceSwap`
- `VAEEncode` ★核心
- `Flux2Scheduler`
- `VAELoader_Any`
- `CFGNorm`
- `InpaintCropImproved`
- `SAM3Segment`
- `AILab_QwenVL`
- `BasicScheduler`
- `ImageScaleToTotalPixelsX`
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixelsX`
- `easy imageSize`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `VAELoader_Any`
- `UNETLoader_Any` ★核心
- `ZImageFunControlnet`
- `Seed (rgthree)`
- `AIO_Preprocessor`
- `easy imageSizeBySide`
- `SamplerCustom` ★核心
- `DetailDaemonSamplerNode` ★核心
- `CFGNorm`
- `BasicScheduler`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `AILab_QwenVL`
- `PreviewImage`
- `easy cleanGpuUsed`
- `DWPreprocessor`
- `PreviewImage`
- `ImageScaleToTotalPixelsX`
- `ImageScaleToTotalPixelsX`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `CLIPLoader_Any`
- `CLIPLoader_Any`
- `VAELoader_Any`
- `RandomNoise`
- `RandomNoise`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader_Any` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `easy ifElse`
- `ColorBalanceNode`
- `PreviewImage`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `KSamplerSelect` ★核心
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`

## 知识

覆盖率 **92%**（86/93）

**有卡**：`VAEDecode`、`SplitSigmas`、`CLIPTextEncode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ModelPatchLoader`、`CLIPLoader_Any`、`VAEEncode`、`BasicGuider`、`ReferenceLatent`、`DetailDaemonSamplerNode`、`ModelSamplingAuraFlow`、`SamplerCustom`、`UNETLoader_Any`、`ImitationHueNode`、`SetLatentNoiseMask`、`ImageScaleToTotalPixelsX`、`BasicScheduler`、`EmptyFlux2LatentImage`、`ReActorFaceSwap`、`Flux2Scheduler`、`VAELoader_Any`、`CFGNorm`、`InpaintCropImproved`、`SAM3Segment`、`AILab_QwenVL`、`InpaintStitchImproved`、`easy imageSize`、`ZImageFunControlnet`、`Seed (rgthree)`、`AIO_Preprocessor`、`easy imageSizeBySide`、`easy cleanGpuUsed`、`DWPreprocessor`、`RandomNoise`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`LoadImage`、`ColorBalanceNode`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、ZImageFunControlnet、CFGNorm、DetailDaemonSamplerNode、KSamplerSelect
