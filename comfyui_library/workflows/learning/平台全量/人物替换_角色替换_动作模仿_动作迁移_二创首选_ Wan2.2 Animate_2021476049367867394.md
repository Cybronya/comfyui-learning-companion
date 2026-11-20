---
key: 平台全量/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2021476049367867394.json
name: 人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2021476049367867394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2021476049367867394.json
hash: 2e0c3cae55d3133d
coverage: 0.567901
learned_at: 2026-11-14 01:37:56
nodes: [GetNode, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PointsEditor, ImageFromBatch+, Note, Reroute, Reroute, PreviewImage, INTConstant, INTConstant, INTConstant, SetNode, SetNode, VHS_VideoInfo, SetNode, GetImageSizeAndCount, PreviewImage, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetBlockSwap, SetNode, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, SetNode, JWInteger, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, easy cleanGpuUsed, CR Text, WanVideoTextEncodeCached, WanVideoSampler, easy cleanGpuUsed, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, ImageConcanate, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, InvertMask, MaskToImage, Reroute, LayerUtility: ImageBlend, DrawViTPose, easy cleanGpuUsed, SetNode, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GrowMask, BlockifyMask, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, ImageResizeKJv2, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2021476049367867394.json

> 来源文件 `comfyui_library/workflows/平台全量/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2021476049367867394.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（81 个）：
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PointsEditor`
- `ImageFromBatch+`
- `Note`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `JWInteger`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CR Text`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `InvertMask`
- `MaskToImage`
- `Reroute`
- `LayerUtility: ImageBlend`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`PointsEditor`、`ImageFromBatch+`、`INTConstant`、`VHS_VideoInfo`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`JWInteger`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`CR Text`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`SeCModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`DrawViTPose`、`VHS_VideoCombine`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
