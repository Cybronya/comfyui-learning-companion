---
key: 视频生成/图生视频/wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json
name: wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967815071856472066.json
hash: 385e1be50419c652
coverage: 0.974359
learned_at: 2026-10-15 22:31:43
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, ImpactInt, WanVideoTextEncode, WanVideoVACEStartToEndFrame, WanVideoVACEEncode, INTConstant, CreateCFGScheduleFloatList, INTConstant, WanVideoDecode, ColorMatch, ImageConcatMulti, ImageConcatMulti, ImageResizeKJv2, ImageResizeKJv2, MarkdownNote, Note Plus (mtb), SimpleMath+, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, ImpactInt, ImpactInt, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2官方 VACE 首尾帧 KJ流_1967815071856472066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967815071856472066.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `ImpactInt`
- `WanVideoTextEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEEncode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoDecode`
- `ColorMatch`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `MarkdownNote`
- `Note Plus (mtb)`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `ImpactInt`
- `ImpactInt`
- `CR Text`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`ImpactInt`、`WanVideoTextEncode`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`ColorMatch`、`ImageConcatMulti`、`ImageResizeKJv2`、`Note Plus (mtb)`、`SimpleMath+`、`WanVideoSampler`、`VHS_VideoCombine`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
