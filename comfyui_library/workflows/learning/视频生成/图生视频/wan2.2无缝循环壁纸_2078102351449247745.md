---
key: 视频生成/图生视频/wan2.2无缝循环壁纸_2078102351449247745.json
name: wan2.2无缝循环壁纸_2078102351449247745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078102351449247745.json
hash: 32f597faf3c91fb9
coverage: 0.438298
learned_at: 2026-10-15 22:41:49
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, VAELoader, GetNode, SetNode, CLIPVisionLoader, ModelSamplingSD3, SetNode, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, KSamplerAdvanced, SetNode, CLIPVisionEncode, CLIPLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, ImageResizeKJv2, ColorMatch, WanFirstLastFrameToVideo, VAEEncode, GetNode, WanImageToVideoSVIPro, SetNode, SetNode, CLIPTextEncode, KSamplerAdvanced, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, WanImageToVideoSVIPro, VHS_VideoCombine, SetNode, SetNode, GetNode, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, GetNode, SetNode, GetNode, GetNode, GetNode, WanImageToVideoSVIPro, KSamplerAdvanced, GetNode, GetNode, KSamplerAdvanced, ImageBatchExtendWithOverlap, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, VAEDecode, GetNode, VAEEncode, GetNode, VAEDecode, GetNode, VAEEncode, GetNode, VAEDecode, GetNode, VAEEncode, VAEDecode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, GetNode, GetNode, KSamplerAdvanced, KSamplerAdvanced, SetNode, KSamplerAdvanced, TrimBatchEnds, ColorMatch, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, ImageFromBatch+, MarkdownNote, CLIPVisionEncode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, easy anythingIndexSwitch, GetNode, GetNode, GetNode, GetNode, GetNode, easy anythingIndexSwitch, Split String, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, CLIPTextEncode, GetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, Int, Int, Int, Int, INTConstant, Float, Seed (rgthree), ComfyMathExpression, SetNode, AssembleLoopFrames, PrepareLoopFrames, RIFE VFI, VHS_VideoCombine, ImageBatchExtendWithOverlap, MarkdownNote, RIFE_VFI_Advanced, INTConstant, PreviewImage, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, UNETLoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, INTConstant, GetNode, LayerUtility: PurgeVRAM V2, Float to Int, DuckHideNode, SaveImage, VHS_VideoCombine, CLIPTextEncode, CR Text, LoadImage, Fast Groups Bypasser (rgthree), Int]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2无缝循环壁纸_2078102351449247745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078102351449247745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（235 个）：
- `SetNode`
- `SetNode`
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
- `VAEDecode` ★核心
- `VAELoader`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `SetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `CLIPVisionEncode`
- `CLIPLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ImageResizeKJv2`
- `ColorMatch`
- `WanFirstLastFrameToVideo`
- `VAEEncode` ★核心
- `GetNode`
- `WanImageToVideoSVIPro`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanImageToVideoSVIPro`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `ImageBatchExtendWithOverlap`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
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
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `KSamplerAdvanced` ★核心
- `TrimBatchEnds`
- `ColorMatch`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `ImageFromBatch+`
- `MarkdownNote`
- `CLIPVisionEncode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy anythingIndexSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy anythingIndexSwitch`
- `Split String`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `Int`
- `Int`
- `Int`
- `Int`
- `INTConstant`
- `Float`
- `Seed (rgthree)`
- `ComfyMathExpression`
- `SetNode`
- `AssembleLoopFrames`
- `PrepareLoopFrames`
- `RIFE VFI`
- `VHS_VideoCombine`
- `ImageBatchExtendWithOverlap`
- `MarkdownNote`
- `RIFE_VFI_Advanced`
- `INTConstant`
- `PreviewImage`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `Float to Int`
- `DuckHideNode`
- `SaveImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CR Text`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **44%**（103/235）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPVisionLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`CLIPVisionEncode`、`CLIPLoader`、`ModelPatchTorchSettings`、`ImageResizeKJv2`、`ColorMatch`、`WanFirstLastFrameToVideo`、`VAEEncode`、`WanImageToVideoSVIPro`、`CLIPTextEncode`、`VHS_VideoCombine`、`ImageBatchExtendWithOverlap`、`TrimBatchEnds`、`ImageFromBatch+`、`easy anythingIndexSwitch`、`Split String`、`INTConstant`、`Int`、`Float`、`Seed (rgthree)`、`ComfyMathExpression`、`AssembleLoopFrames`、`PrepareLoopFrames`、`RIFE VFI`、`RIFE_VFI_Advanced`、`UNETLoader`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM V2`、`Float to Int`、`DuckHideNode`、`SaveImage`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
