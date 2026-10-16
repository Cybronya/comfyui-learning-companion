---
key: 视频生成/图生视频/Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json
name: Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999310460828647425.json
hash: bb4c5e7096c31803
coverage: 0.823529
learned_at: 2026-10-15 22:33:36
nodes: [GetNode, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, WanVideoDecode, WanVideoWanDrawWanMoveTracks, ImageConcanate, SimpleMath+, Primitive integer [Crystools], WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTextEncode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, WanVideoVAELoader, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoAddWanMoveTracks, WanVideoSampler, FL_PathAnimator, Primitive integer [Crystools], Primitive integer [Crystools], VHS_VideoCombine, VHS_VideoCombine, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wanmove+Fill Nodes 动与静轨迹控制 【 1.0 】_1999310460828647425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999310460828647425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `GetNode`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `WanVideoDecode`
- `WanVideoWanDrawWanMoveTracks`
- `ImageConcanate`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoAddWanMoveTracks`
- `WanVideoSampler` ★核心
- `FL_PathAnimator`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`WanVideoDecode`、`WanVideoWanDrawWanMoveTracks`、`ImageConcanate`、`Primitive integer [Crystools]`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoAddWanMoveTracks`、`WanVideoSampler`、`FL_PathAnimator`、`VHS_VideoCombine`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
