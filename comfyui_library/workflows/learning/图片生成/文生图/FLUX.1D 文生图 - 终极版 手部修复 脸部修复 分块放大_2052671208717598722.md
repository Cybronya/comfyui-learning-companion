---
key: 图片生成/文生图/FLUX.1D 文生图 - 终极版 手部修复 脸部修复 分块放大_2052671208717598722.json
name: FLUX.1D 文生图 - 终极版 手部修复 脸部修复 分块放大_2052671208717598722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1D 文生图 - 终极版 手部修复 脸部修复 分块放大_2052671208717598722.json
hash: 64f54d1848d34180
coverage: 0.424658
learned_at: 2026-10-21 02:51:48
nodes: [MaskToImage, PreviewImage, Note, Note, SAMLoader, LatentUpscaleBy, RandomNoise, BasicScheduler, SetNode, SetNode, SamplerCustomAdvanced, SetNode, SetNode, VAEDecode, GetNode, GetNode, Reroute, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, UltimateSDUpscaleNoUpscale, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, MarkdownNote, MarkdownNote, GetNode, SetNode, KSamplerSelect, CLIPTextEncode, SetNode, GetNode, RandomNoise, KSamplerSelect, CLIPTextEncodeFlux, ModelSamplingFlux, VAEDecode, DetailDaemonSamplerNode, GetNode, Note, GetNode, GetNode, SaveImage, GetNode, SaveImage, GetNode, SaveImage, GetNode, SaveImage, PreviewImage, GetNode, SaveImage, MaskToImage, PreviewImage, Note, Note, SAMLoader, GetNode, GetNode, GetNode, GetNode, SaveImage, MaskToImage, PreviewImage, Note, Note, SAMLoader, GetNode, GetNode, GetNode, GetNode, SaveImage, FaceDetailer, UltralyticsDetectorProvider, Lora Loader, Lora Loader, Lora Loader, CLIPTextEncode, CLIPTextEncode, Note, ImpactWildcardProcessor, Note, ControlNetLoader, GetNode, GetNode, GetNode, GetNode, BasicScheduler, LoadImage, Label (rgthree), SetUnionControlNetType, SetUnionControlNetType, AIO_Preprocessor, ControlNetLoader, Note, MarkdownNote, SetNode, Note, GetNode, GetNode, GetNode, GetNode, Note, ControlNetApplyAdvanced, BasicGuider, GetNode, GetNode, MarkdownNote, SetNode, GetNode, SetNode, SamplerCustomAdvanced, SetNode, GetNode, GetNode, Reroute, Reroute, FaceDetailer, FaceDetailer, Reroute, ControlNetApplyAdvanced, Reroute, PreviewImage, MarkdownNote, CannyEdgePreprocessor, SDXL Empty Latent Image (rgthree), ImageResizeKJv2, Fast Groups Bypasser (rgthree), ImageResizeKJv2, Note, VAELoader, UltimateSDUpscale, UpscaleModelLoader, UltralyticsDetectorProvider, UltralyticsDetectorProvider, UNETLoader, DualCLIPLoader, Lora Loader Stack (rgthree), MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.4000000000000001}
---

# 图片生成/文生图/FLUX.1D 文生图 - 终极版 手部修复 脸部修复 分块放大_2052671208717598722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1D 文生图 - 终极版 手部修复 脸部修复 分块放大_2052671208717598722.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `MaskToImage`
- `PreviewImage`
- `Note`
- `Note`
- `SAMLoader`
- `LatentUpscaleBy`
- `RandomNoise`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `UltimateSDUpscaleNoUpscale`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPTextEncodeFlux` ★核心
- `ModelSamplingFlux`
- `VAEDecode` ★核心
- `DetailDaemonSamplerNode` ★核心
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `PreviewImage`
- `GetNode`
- `SaveImage`
- `MaskToImage`
- `PreviewImage`
- `Note`
- `Note`
- `SAMLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `MaskToImage`
- `PreviewImage`
- `Note`
- `Note`
- `SAMLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `FaceDetailer`
- `UltralyticsDetectorProvider`
- `Lora Loader`
- `Lora Loader`
- `Lora Loader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `ImpactWildcardProcessor`
- `Note`
- `ControlNetLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `LoadImage`
- `Label (rgthree)`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `Note`
- `MarkdownNote`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `ControlNetApplyAdvanced` ★核心
- `BasicGuider`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `FaceDetailer`
- `FaceDetailer`
- `Reroute`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `PreviewImage`
- `MarkdownNote`
- `CannyEdgePreprocessor`
- `SDXL Empty Latent Image (rgthree)`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `Note`
- `VAELoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Lora Loader Stack (rgthree)`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `controlnet_strength` = `0.4000000000000001`

## 知识

覆盖率 **42%**（62/146）

**有卡**：`MaskToImage`、`SAMLoader`、`LatentUpscaleBy`、`RandomNoise`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`UltimateSDUpscaleNoUpscale`、`CLIPTextEncode`、`KSamplerSelect`、`CLIPTextEncodeFlux`、`ModelSamplingFlux`、`DetailDaemonSamplerNode`、`SaveImage`、`FaceDetailer`、`UltralyticsDetectorProvider`、`Lora Loader`、`ImpactWildcardProcessor`、`ControlNetLoader`、`LoadImage`、`Label (rgthree)`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ControlNetApplyAdvanced`、`BasicGuider`、`CannyEdgePreprocessor`、`SDXL Empty Latent Image (rgthree)`、`ImageResizeKJv2`、`VAELoader`、`UltimateSDUpscale`、`UpscaleModelLoader`、`UNETLoader`、`DualCLIPLoader`、`Lora Loader Stack (rgthree)`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType
