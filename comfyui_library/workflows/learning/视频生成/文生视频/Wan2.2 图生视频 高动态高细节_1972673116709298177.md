---
key: 视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json
name: Wan2.2 图生视频 高动态高细节_1972673116709298177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 图生视频 高动态高细节_1972673116709298177.json
hash: 24cfe7204196d665
coverage: 0.766667
learned_at: 2026-10-10 23:07:01
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, VHS_VideoCombine, GetNode, WanVideoSampler, Seed (rgthree), LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoVAELoader, Anything Everywhere, SetNode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, ImageScaleToMegapixels, UpscaleModelLoader, WanVideoDecode, LoadImage, ImpactInt, LoadImage, LoadImage, CR Text, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, SimpleMath+]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, Seed (rgthree)]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **77%**（23/30）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`WanVideoDecode`、`LoadImage`、`ImpactInt`

**缺卡**（4）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
