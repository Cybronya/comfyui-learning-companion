---
key: 平台全量/-修改参数---人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2028776061948923905.json
name: -修改参数---人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2028776061948923905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/-修改参数---人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2028776061948923905.json
hash: b83c8f4bb96f11f0
coverage: 0.567901
learned_at: 2026-11-14 00:09:20
nodes: [GetNode, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch+, Note, Reroute, Reroute, PreviewImage, INTConstant, INTConstant, INTConstant, SetNode, SetNode, VHS_VideoInfo, SetNode, GetImageSizeAndCount, PreviewImage, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetBlockSwap, SetNode, SetNode, WanVideoLoraSelectMulti, SetNode, JWInteger, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, easy cleanGpuUsed, CR Text, easy cleanGpuUsed, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, ImageConcanate, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, InvertMask, MaskToImage, Reroute, LayerUtility: ImageBlend, DrawViTPose, easy cleanGpuUsed, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, BlockifyMask, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, SetNode, ImageResizeKJv2, LoadImage, VHS_VideoCombine, VHS_LoadVideo, WanVideoTextEncodeCached, SeCVideoSegmentation, SetNode, GrowMask, PointsEditor, WanVideoModelLoader, WanVideoAnimateEmbeds, WanVideoSampler]
patterns: []
missing: []
---

# 平台全量/-修改参数---人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2028776061948923905.json

> 来源文件 `comfyui_library/workflows/平台全量/-修改参数---人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2028776061948923905.json`

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
- `WanVideoLoraSelectMulti`
- `SetNode`
- `JWInteger`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CR Text`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `InvertMask`
- `MaskToImage`
- `Reroute`
- `LayerUtility: ImageBlend`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `SetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `SetNode`
- `GrowMask`
- `PointsEditor`
- `WanVideoModelLoader`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **57%**（46/81）

**有卡**：`ImageFromBatch+`、`INTConstant`、`VHS_VideoInfo`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`JWInteger`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`CR Text`、`WanVideoDecode`、`ImageConcanate`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`SeCModelLoader`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`DrawViTPose`、`VHS_VideoCombine`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`LoadImage`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`GrowMask`、`PointsEditor`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
