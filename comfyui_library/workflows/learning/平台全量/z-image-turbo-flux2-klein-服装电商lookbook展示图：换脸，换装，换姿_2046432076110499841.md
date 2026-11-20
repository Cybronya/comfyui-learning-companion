---
key: 平台全量/z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841.json
name: z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841.json
hash: a19b2205d4968152
coverage: 0.878049
learned_at: 2026-11-14 01:20:35
nodes: [KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, SamplerCustomAdvanced, SamplerCustomAdvanced, BasicGuider, ReferenceLatent, ReferenceLatent, Anything Everywhere3, CLIPLoader_Any, VAELoader_Any, Reroute, SplitSigmas, CLIPTextEncode, KSamplerSelect, VAEEncode, DetailDaemonSamplerNode, ModelSamplingAuraFlow, SamplerCustom, UNETLoader_Any, CLIPTextEncode, BasicScheduler, CFGNorm, AILab_QwenVL, SetLatentNoiseMask, LoraLoaderModelOnly, SamplerCustomAdvanced, ImageScaleToTotalPixelsX, VAEDecode, RandomNoise, KSamplerSelect, ReferenceLatent, VAEEncode, KSamplerSelect, BasicScheduler, ImageScaleToTotalPixelsX, SamplerCustom, VAEDecode, VAELoader_Any, VAEEncode, VAEDecode, InpaintCropImproved, BasicScheduler, InpaintStitchImproved, ReActorFaceSwap, ImageScaleToTotalPixelsX, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, ImageScaleToTotalPixelsX, DWPreprocessor, RandomNoise, easy cleanGpuUsed, LoadImage, LoadImage, PreviewImage, PreviewImage, VAEEncode, easy ifElse, easy ifElse, Note, CLIPLoader_Any, VAEDecode, SaveImage, PreviewImage, UNETLoader_Any, SAM3Segment, LoadImage, easy ifElse, RandomNoise, Seed (rgthree), LoadImage, easy positive, easy ifElse, VAEEncode, VAEEncode, ReferenceLatent, BasicScheduler, BasicGuider]
patterns: []
missing: []
---

# 平台全量/z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841.json

> 来源文件 `comfyui_library/workflows/平台全量/z-image-turbo-flux2-klein-服装电商lookbook展示图：换脸，换装，换姿_2046432076110499841.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `ReferenceLatent`
- `Anything Everywhere3`
- `CLIPLoader_Any`
- `VAELoader_Any`
- `Reroute`
- `SplitSigmas`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `VAEEncode` ★核心
- `DetailDaemonSamplerNode` ★核心
- `ModelSamplingAuraFlow`
- `SamplerCustom` ★核心
- `UNETLoader_Any` ★核心
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `CFGNorm`
- `AILab_QwenVL`
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixelsX`
- `VAEDecode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ImageScaleToTotalPixelsX`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `VAELoader_Any`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `InpaintCropImproved`
- `BasicScheduler`
- `InpaintStitchImproved`
- `ReActorFaceSwap`
- `ImageScaleToTotalPixelsX`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixelsX`
- `DWPreprocessor`
- `RandomNoise`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `VAEEncode` ★核心
- `easy ifElse`
- `easy ifElse`
- `Note`
- `CLIPLoader_Any`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `UNETLoader_Any` ★核心
- `SAM3Segment`
- `LoadImage`
- `easy ifElse`
- `RandomNoise`
- `Seed (rgthree)`
- `LoadImage`
- `easy positive`
- `easy ifElse`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `BasicScheduler`
- `BasicGuider`

## 知识

覆盖率 **88%**（72/82）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ReferenceLatent`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustomAdvanced`、`CLIPLoader_Any`、`VAELoader_Any`、`SplitSigmas`、`CLIPTextEncode`、`DetailDaemonSamplerNode`、`ModelSamplingAuraFlow`、`SamplerCustom`、`UNETLoader_Any`、`BasicScheduler`、`CFGNorm`、`AILab_QwenVL`、`SetLatentNoiseMask`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixelsX`、`VAEDecode`、`RandomNoise`、`InpaintCropImproved`、`InpaintStitchImproved`、`ReActorFaceSwap`、`DWPreprocessor`、`easy cleanGpuUsed`、`LoadImage`、`SaveImage`、`SAM3Segment`、`Seed (rgthree)`、`easy positive`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGNorm、DetailDaemonSamplerNode、KSamplerSelect、SamplerCustom
