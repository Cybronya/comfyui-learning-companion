---
key: 视频生成/图生视频/wan2.2图生视频_2048784808272207873.json
name: wan2.2图生视频_2048784808272207873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频_2048784808272207873.json
hash: 2a4cb58696f17fdf
coverage: 0.525926
learned_at: 2026-10-15 22:37:11
nodes: [GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_GetImageCount, SetNode, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, VHS_VideoCombine, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, RIFEInterpolation, ImpactInt, GetNode, GetNode, WanImageToVideoSVIPro, DisableNoise, ScheduledCFGGuidance, SamplerCustomAdvanced, ScheduledCFGGuidance, SamplerCustomAdvanced, VAEDecode, RTXVideoSuperResolution, String Replace (mtb), GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, VAEEncode, GetNode, MathExpression|pysssss, ForLoopClose, ForLoopOpen, ImageBatchExtendWithOverlap, GetNode, GetNode, UNETLoader, UNETLoader, GetNode, GetNode, GetNode, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, easy showAnything, easy promptLine, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, SetNode, CLIPLoader, SetNode, llama_cpp_instruct_adv, PrimitiveStringMultiline, llama_cpp_model_loader, GetNode, GetNode, MathExpression|pysssss, SomethingToString, ShowText|pysssss, PrimitiveStringMultiline, SetNode, UnloadModel, easy showAnything, SetNode, ImpactInt, SetNode, SetNode, SetNode, SetNode, VAELoader, RandomNoise, UNETLoader, UNETLoader, PrimitiveStringMultiline, CLIPTextEncode, ScheduledCFGGuidance, WanImageToVideoSVIPro, ScheduledCFGGuidance, ImpactInt, MathExpression|pysssss, PainterVRAM, SetNode, DisableNoise, SamplerCustomAdvanced, RIFEInterpolation, RTXVideoSuperResolution, CLIPTextEncode, VAEEncode, SetNode, BasicScheduler, SplitSigmas, VAEDecode, easy showAnything, SamplerCustomAdvanced, SaveImage, easy promptLine, PrimitiveFloat, ImpactInt, MathExpression|pysssss, ImpactInt, GetNode, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveStringMultiline, MarkdownNote, DuckHideNode, KSamplerSelect, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2图生视频_2048784808272207873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048784808272207873.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（135 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_GetImageCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `RIFEInterpolation`
- `ImpactInt`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `DisableNoise`
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `ScheduledCFGGuidance`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RTXVideoSuperResolution`
- `String Replace (mtb)`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `MathExpression|pysssss`
- `ForLoopClose`
- `ForLoopOpen`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `easy promptLine`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `SetNode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `SomethingToString`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `SetNode`
- `UnloadModel`
- `easy showAnything`
- `SetNode`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `RandomNoise`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `ScheduledCFGGuidance`
- `WanImageToVideoSVIPro`
- `ScheduledCFGGuidance`
- `ImpactInt`
- `MathExpression|pysssss`
- `PainterVRAM`
- `SetNode`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `RIFEInterpolation`
- `RTXVideoSuperResolution`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SetNode`
- `BasicScheduler`
- `SplitSigmas`
- `VAEDecode` ★核心
- `easy showAnything`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `easy promptLine`
- `PrimitiveFloat`
- `ImpactInt`
- `MathExpression|pysssss`
- `ImpactInt`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `DuckHideNode`
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **53%**（71/135）

**有卡**：`VHS_GetImageCount`、`MathExpression|pysssss`、`VHS_VideoCombine`、`RIFEInterpolation`、`ImpactInt`、`WanImageToVideoSVIPro`、`DisableNoise`、`ScheduledCFGGuidance`、`SamplerCustomAdvanced`、`VAEDecode`、`RTXVideoSuperResolution`、`String Replace (mtb)`、`CLIPTextEncode`、`VAEEncode`、`ForLoopClose`、`ForLoopOpen`、`ImageBatchExtendWithOverlap`、`UNETLoader`、`easy promptLine`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`SomethingToString`、`UnloadModel`、`VAELoader`、`RandomNoise`、`PainterVRAM`、`BasicScheduler`、`SplitSigmas`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`DuckHideNode`、`KSamplerSelect`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect
