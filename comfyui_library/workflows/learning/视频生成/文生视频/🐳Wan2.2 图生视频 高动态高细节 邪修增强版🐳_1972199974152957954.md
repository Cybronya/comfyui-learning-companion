---
key: 视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json
name: 🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json
hash: 2c53a35a50cf0376
coverage: 0.705882
learned_at: 2026-10-10 23:14:49
nodes: [INTConstant, UpscaleModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, ImpactInt, WanVideoSampler, WanVideoSampler, SimpleMath+, CreateCFGScheduleFloatList, WanVideoDecode, Seed (rgthree), GetNode, VHS_VideoCombine, MarkdownNote, Note Plus (mtb), SimpleMath+, WanVideoModelLoader, WanVideoModelLoader, ImpactInt, ImpactInt, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, WanVideoTorchCompileSettings, Fast Groups Bypasser (rgthree), WanVideoLoraSelectMulti, WanVideoVAELoader, ImageUpscaleWithModel, SetNode, CR Text, LoadImage]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, Note Plus (mtb), SimpleMath+, SimpleMath+, Seed (rgthree)]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `INTConstant`
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `ImpactInt`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `Seed (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note Plus (mtb)`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `WanVideoTorchCompileSettings`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `ImageUpscaleWithModel`
- `SetNode`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`INTConstant`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`ImpactInt`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`ImageUpscaleWithModel`、`LoadImage`

**缺卡**（6）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`Note Plus (mtb)`、`SimpleMath+`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
