---
key: 视频生成/图生视频/AI指导wan2.1图生视频_1977940340936167425.json
name: AI指导wan2.1图生视频_1977940340936167425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI指导wan2.1图生视频_1977940340936167425.json
hash: f29030a04766611e
coverage: 1
learned_at: 2026-10-15 22:32:16
nodes: [CLIPVisionLoader, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM V2, WanVideoVAELoader, WanVideoTextEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoSLG, WanVideoBlockSwap, WanVideoImageToVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, WanVideoSampler, UpscaleModelLoader, UpscaleModelLoader, UpscaleModelLoader, ImageUpscaleWithModelBatched, Int, JWInteger, LoadImage, WanVideoDecode, LazySwitchKJ, easy anythingIndexSwitch, NumberClamp, JWInteger, MultiplyNode, Text Multiline, VHS_VideoCombine, DF_Int_to_Float, ImpactInt, Int, Int, ImpactInt, sanmi IntToBOOLEAN]
patterns: []
missing: []
---

# 视频生成/图生视频/AI指导wan2.1图生视频_1977940340936167425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977940340936167425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Text Multiline`
- `WanVideoSampler` ★核心
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `ImageUpscaleWithModelBatched`
- `Int`
- `JWInteger`
- `LoadImage`
- `WanVideoDecode`
- `LazySwitchKJ`
- `easy anythingIndexSwitch`
- `NumberClamp`
- `JWInteger`
- `MultiplyNode`
- `Text Multiline`
- `VHS_VideoCombine`
- `DF_Int_to_Float`
- `ImpactInt`
- `Int`
- `Int`
- `ImpactInt`
- `sanmi IntToBOOLEAN`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM V2`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoSLG`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`、`WanVideoSampler`、`UpscaleModelLoader`、`ImageUpscaleWithModelBatched`、`Int`、`JWInteger`、`LoadImage`、`WanVideoDecode`、`LazySwitchKJ`、`easy anythingIndexSwitch`、`NumberClamp`、`MultiplyNode`、`VHS_VideoCombine`、`DF_Int_to_Float`、`ImpactInt`、`sanmi IntToBOOLEAN`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
