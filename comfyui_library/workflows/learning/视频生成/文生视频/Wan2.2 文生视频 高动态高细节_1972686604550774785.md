---
key: 视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json
name: Wan2.2 文生视频 高动态高细节_1972686604550774785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json
hash: 485deb89aa8c889d
coverage: 0.884615
learned_at: 2026-10-10 23:07:03
nodes: [UpscaleModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSampler, WanVideoModelLoader, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoTextEncode, Seed (rgthree), LoadWanVideoT5TextEncoder, WanVideoVAELoader, CR Text, WanVideoEmptyEmbeds, SimpleMath+, ImpactInt, ImpactInt, LoadImage, ImageScaleToMegapixels, VHS_VideoCombine, ImpactInt, VHS_VideoCombine]
patterns: []
missing: [CR Text, SimpleMath+, Seed (rgthree)]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **88%**（23/26）

**有卡**：`UpscaleModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoEmptyEmbeds`、`ImpactInt`、`LoadImage`、`ImageScaleToMegapixels`、`VHS_VideoCombine`

**缺卡**（3）：`CR Text`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
