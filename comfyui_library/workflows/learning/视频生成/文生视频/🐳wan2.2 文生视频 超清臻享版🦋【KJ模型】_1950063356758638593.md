---
key: 视频生成/文生视频/🐳wan2.2 文生视频 超清臻享版🦋【KJ模型】_1950063356758638593.json
name: 🐳wan2.2 文生视频 超清臻享版🦋【KJ模型】_1950063356758638593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950063356758638593.json
hash: 6329c4a17738264a
coverage: 0.966667
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, ImpactInt, ImpactInt, ImpactInt, CreateCFGScheduleFloatList, WanVideoDecode, MarkdownNote, Note Plus (mtb), WanVideoBlockSwap, SimpleMath+, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, GetImageSizeAndCount, WanVideoEmptyEmbeds, WanVideoSampler, CR Text, WanVideoSampler, WanVideoContextOptions, VHS_VideoCombine, INTConstant, INTConstant, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/🐳wan2.2 文生视频 超清臻享版🦋【KJ模型】_1950063356758638593.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950063356758638593.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `MarkdownNote`
- `Note Plus (mtb)`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `CR Text`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`ImpactInt`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`Note Plus (mtb)`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`GetImageSizeAndCount`、`WanVideoEmptyEmbeds`、`WanVideoSampler`、`CR Text`、`WanVideoContextOptions`、`VHS_VideoCombine`、`INTConstant`、`WanVideoTextEncode`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
