---
key: 视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json
name: Wan2.2 文生视频 高动态高细节_1972686604550774785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json
hash: 485deb89aa8c889d
coverage: 1
learned_at: 2026-10-15 22:47:11
nodes: [UpscaleModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoTextEncode, Seed (rgthree), LoadWanVideoT5TextEncoder, WanVideoVAELoader, CR Text, WanVideoEmptyEmbeds, SimpleMath+, ImpactInt, ImpactInt, LoadImage, ImageScaleToMegapixels, VHS_VideoCombine, ImpactInt, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoTextEncode`
- `Seed (rgthree)`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `CR Text`
- `WanVideoEmptyEmbeds`
- `SimpleMath+`
- `ImpactInt`
- `ImpactInt`
- `LoadImage`
- `ImageScaleToMegapixels`
- `VHS_VideoCombine`
- `ImpactInt`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`UpscaleModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`Seed (rgthree)`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CR Text`、`WanVideoEmptyEmbeds`、`SimpleMath+`、`ImpactInt`、`LoadImage`、`ImageScaleToMegapixels`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
