---
key: 视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json
name: 🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json
hash: 033a686fed86a2c4
coverage: 0.878788
learned_at: 2026-10-15 22:49:13
nodes: [INTConstant, UpscaleModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoModelLoader, ImpactInt, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, SimpleMath+, CreateCFGScheduleFloatList, WanVideoDecode, ImpactInt, ImpactInt, SimpleMath+, ImpactInt, Seed (rgthree), SetNode, GetNode, VHS_VideoCombine, MarkdownNote, Note Plus (mtb), Fast Groups Bypasser (rgthree), VHS_VideoCombine, WanVideoVAELoader, WanVideoLoraSelectMulti, CR Text, ImageUpscaleWithModel]
patterns: []
missing: []
---

# 视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `INTConstant`
- `UpscaleModelLoader`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `ImpactInt`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `ImpactInt`
- `ImpactInt`
- `SimpleMath+`
- `ImpactInt`
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note Plus (mtb)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `CR Text`
- `ImageUpscaleWithModel`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`INTConstant`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`ImpactInt`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`Seed (rgthree)`、`VHS_VideoCombine`、`Note Plus (mtb)`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`CR Text`、`ImageUpscaleWithModel`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti
