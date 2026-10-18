---
key: 视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json
name: wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json
hash: 6d152c3defb563cb
coverage: 0.973684
learned_at: 2026-10-15 22:31:43
nodes: [WanVideoSetBlockSwap, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoVACEEncode, ImageResizeKJv2, VHS_VideoInfo, DWPreprocessor, SimpleMath+, INTConstant, WanVideoTextEncode, WanVideoSampler, WanVideoSampler, WanVideoDecode, ImageConcatMulti, ImageResizeKJv2, MarkdownNote, Note Plus (mtb), VHS_VideoCombine, LoadImage, VHS_LoadVideo, WanVideoVAELoader, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, easy int, easy int, CR Text, easy int, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2官方 VACE 人物姿态迁移 KJ流【推荐】_1967834051866406914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967834051866406914.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoVACEEncode`
- `ImageResizeKJv2`
- `VHS_VideoInfo`
- `DWPreprocessor`
- `SimpleMath+`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `MarkdownNote`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy int`
- `easy int`
- `CR Text`
- `easy int`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoVACEEncode`、`ImageResizeKJv2`、`VHS_VideoInfo`、`DWPreprocessor`、`SimpleMath+`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`Note Plus (mtb)`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`easy int`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
