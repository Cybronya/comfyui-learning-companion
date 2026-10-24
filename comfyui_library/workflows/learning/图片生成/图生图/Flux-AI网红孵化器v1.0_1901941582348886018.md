---
key: 图片生成/图生图/Flux-AI网红孵化器v1.0_1901941582348886018.json
name: Flux-AI网红孵化器v1.0_1901941582348886018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-AI网红孵化器v1.0_1901941582348886018.json
hash: 158f4e6d012f0186
coverage: 0.512195
learned_at: 2026-10-23 10:58:22
nodes: [GetNode, SetNode, Anything Everywhere, GetNode, GetNode, FluxGuidance, GetNode, GetNode, GetNode, RandomNoise, KSamplerSelect, GetNode, GetNode, CLIPTextEncode, GetNode, ImpactImageBatchToImageList, BasicGuider, VAEDecode, FaceDetailer, DeepTranslatorTextNode, GetNode, SetNode, ModelPassThrough, SetNode, Bookmark (rgthree), CLIPTextEncode, Note, Note, Note, Note, Note, SetNode, SetNode, DetailDaemonSamplerNode, SetNode, Any Switch (rgthree), Any Switch (rgthree), PrimitiveNode, ModelSamplingFlux, EmptySD3LatentImage, GetNode, BasicScheduler, SamplerCustomAdvanced, CLIPtionLoader, GetNode, Anything Everywhere, SaveImage, CLIPtionGenerate, PreviewImage, ReduxPromptStyler, Note, ImageScale, SAMLoader, UltralyticsDetectorProvider, INTConstant, SaveImage, PrimitiveNode, VAELoader, CLIPLoader, CLIPVisionLoader, StyleModelLoader, CLIPVisionLoader, LoraLoaderModelOnly, Get resolution [Crystools], SetNode, SetNode, LoadImage, Fast Groups Bypasser (rgthree), ShowText|pysssss, Seed (rgthree), FluxAttentionSeeker+, DualCLIPLoader, GetNode, SetNode, Bookmark (rgthree), Bookmark (rgthree), MarkdownNote, Fast Groups Bypasser (rgthree), CR Text, LoraLoaderModelOnly, CheckpointLoaderSimple, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "麦橘超然majicFlus_v1_liblib.safetensors"}
---

# 图片生成/图生图/Flux-AI网红孵化器v1.0_1901941582348886018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-AI网红孵化器v1.0_1901941582348886018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `GetNode`
- `SetNode`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `FluxGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImpactImageBatchToImageList`
- `BasicGuider`
- `VAEDecode` ★核心
- `FaceDetailer`
- `DeepTranslatorTextNode`
- `GetNode`
- `SetNode`
- `ModelPassThrough`
- `SetNode`
- `Bookmark (rgthree)`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `DetailDaemonSamplerNode` ★核心
- `SetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `PrimitiveNode`
- `ModelSamplingFlux`
- `EmptySD3LatentImage`
- `GetNode`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `CLIPtionLoader`
- `GetNode`
- `Anything Everywhere`
- `SaveImage`
- `CLIPtionGenerate`
- `PreviewImage`
- `ReduxPromptStyler`
- `Note`
- `ImageScale`
- `SAMLoader`
- `UltralyticsDetectorProvider`
- `INTConstant`
- `SaveImage`
- `PrimitiveNode`
- `VAELoader`
- `CLIPLoader`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `Get resolution [Crystools]`
- `SetNode`
- `SetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `Seed (rgthree)`
- `FluxAttentionSeeker+`
- `DualCLIPLoader`
- `GetNode`
- `SetNode`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`

## 关键参数

- `checkpoint` = `麦橘超然majicFlus_v1_liblib.safetensors`

## 知识

覆盖率 **51%**（42/82）

**有卡**：`FluxGuidance`、`RandomNoise`、`KSamplerSelect`、`CLIPTextEncode`、`ImpactImageBatchToImageList`、`BasicGuider`、`VAEDecode`、`FaceDetailer`、`DeepTranslatorTextNode`、`ModelPassThrough`、`Bookmark (rgthree)`、`DetailDaemonSamplerNode`、`ModelSamplingFlux`、`EmptySD3LatentImage`、`BasicScheduler`、`SamplerCustomAdvanced`、`CLIPtionLoader`、`SaveImage`、`CLIPtionGenerate`、`ReduxPromptStyler`、`ImageScale`、`SAMLoader`、`UltralyticsDetectorProvider`、`INTConstant`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`StyleModelLoader`、`LoraLoaderModelOnly`、`Get resolution [Crystools]`、`LoadImage`、`Seed (rgthree)`、`FluxAttentionSeeker+`、`DualCLIPLoader`、`CR Text`、`CheckpointLoaderSimple`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、DetailDaemonSamplerNode
