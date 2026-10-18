---
key: 视频生成/图生视频/Wan2.2-替换视频人物_1987076407157305345.json
name: Wan2.2-替换视频人物_1987076407157305345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-替换视频人物_1987076407157305345.json
hash: b7067336f445eb24
coverage: 0.848485
learned_at: 2026-10-15 22:32:57
nodes: [WanVideoModelLoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetBlockSwap, CR Prompt Text, SetNode, WanVideoVAELoader, DownloadAndLoadSAM2Model, WanVideoSampler, WanVideoTextEncodeCached, Sam2Segmentation, GetNode, JWInteger, JWInteger, GetNode, WanVideoAnimateEmbeds, GetNode, PointsEditor, LoadImage, ImageResizeKJv2, WanVideoDecode, VHS_LoadVideo, SetNode, DrawMaskOnImage, BlockifyMask, GrowMask, VHS_VideoCombine, ImpactInt, SimpleMath+, LoadImage, VHS_VideoCombine, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-替换视频人物_1987076407157305345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987076407157305345.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `CR Prompt Text`
- `SetNode`
- `WanVideoVAELoader`
- `DownloadAndLoadSAM2Model`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `Sam2Segmentation`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `PointsEditor`
- `LoadImage`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `SetNode`
- `DrawMaskOnImage`
- `BlockifyMask`
- `GrowMask`
- `VHS_VideoCombine`
- `ImpactInt`
- `SimpleMath+`
- `LoadImage`
- `VHS_VideoCombine`
- `RHHiddenNodes`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`CR Prompt Text`、`WanVideoVAELoader`、`DownloadAndLoadSAM2Model`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`Sam2Segmentation`、`JWInteger`、`WanVideoAnimateEmbeds`、`PointsEditor`、`LoadImage`、`ImageResizeKJv2`、`WanVideoDecode`、`VHS_LoadVideo`、`DrawMaskOnImage`、`BlockifyMask`、`GrowMask`、`VHS_VideoCombine`、`ImpactInt`、`SimpleMath+`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti、CR Prompt Text
