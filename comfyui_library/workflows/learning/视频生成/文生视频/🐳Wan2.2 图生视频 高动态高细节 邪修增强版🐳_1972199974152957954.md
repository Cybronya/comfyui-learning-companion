---
key: 视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json
name: 🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🐳Wan2.2 图生视频 高动态高细节 邪修增强版🐳_1972199974152957954.json
hash: 2c53a35a50cf0376
coverage: 0.882353
learned_at: 2026-10-15 22:49:13
nodes: [INTConstant, UpscaleModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, ImpactInt, WanVideoSampler, WanVideoSampler, SimpleMath+, CreateCFGScheduleFloatList, WanVideoDecode, Seed (rgthree), GetNode, VHS_VideoCombine, MarkdownNote, Note Plus (mtb), SimpleMath+, WanVideoModelLoader, WanVideoModelLoader, ImpactInt, ImpactInt, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, WanVideoTorchCompileSettings, Fast Groups Bypasser (rgthree), WanVideoLoraSelectMulti, WanVideoVAELoader, ImageUpscaleWithModel, SetNode, CR Text, LoadImage]
patterns: []
missing: []
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

覆盖率 **88%**（30/34）

**有卡**：`INTConstant`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`ImpactInt`、`WanVideoSampler`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`Seed (rgthree)`、`VHS_VideoCombine`、`Note Plus (mtb)`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`ImageUpscaleWithModel`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
