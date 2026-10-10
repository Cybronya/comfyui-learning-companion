---
key: 视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json
name: 🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json
hash: 033a686fed86a2c4
coverage: 0.727273
learned_at: 2026-10-10 23:14:50
nodes: [INTConstant, UpscaleModelLoader, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoModelLoader, ImpactInt, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoSampler, SimpleMath+, CreateCFGScheduleFloatList, WanVideoDecode, ImpactInt, ImpactInt, SimpleMath+, ImpactInt, Seed (rgthree), SetNode, GetNode, VHS_VideoCombine, MarkdownNote, Note Plus (mtb), Fast Groups Bypasser (rgthree), VHS_VideoCombine, WanVideoVAELoader, WanVideoLoraSelectMulti, CR Text, ImageUpscaleWithModel]
patterns: []
missing: [CR Text, Note Plus (mtb), SimpleMath+, SimpleMath+, Seed (rgthree)]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **73%**（24/33）

**有卡**：`INTConstant`、`UpscaleModelLoader`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`ImpactInt`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`ImageUpscaleWithModel`

**缺卡**（5）：`CR Text`、`Note Plus (mtb)`、`SimpleMath+`、`SimpleMath+`、`Seed (rgthree)`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelectMulti、ImageUpscaleWithModel

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
