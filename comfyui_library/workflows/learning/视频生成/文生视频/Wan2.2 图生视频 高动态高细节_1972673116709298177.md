---
key: 视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json
name: Wan2.2 图生视频 高动态高细节_1972673116709298177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json
hash: 24cfe7204196d665
coverage: 0.9
learned_at: 2026-10-15 22:47:11
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, VHS_VideoCombine, GetNode, WanVideoSampler, Seed (rgthree), LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoVAELoader, Anything Everywhere, SetNode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, ImageScaleToMegapixels, UpscaleModelLoader, WanVideoDecode, LoadImage, ImpactInt, LoadImage, LoadImage, CR Text, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSampler` ★核心
- `Seed (rgthree)`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `Anything Everywhere`
- `SetNode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `WanVideoDecode`
- `LoadImage`
- `ImpactInt`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `SimpleMath+`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`Seed (rgthree)`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`WanVideoDecode`、`LoadImage`、`ImpactInt`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
