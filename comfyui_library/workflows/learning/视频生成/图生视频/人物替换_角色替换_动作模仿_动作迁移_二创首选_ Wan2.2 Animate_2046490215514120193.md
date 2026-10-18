---
key: 视频生成/图生视频/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2046490215514120193.json
name: 人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2046490215514120193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2046490215514120193.json
hash: d7d9565ca585e725
coverage: 0.589744
learned_at: 2026-10-15 22:36:59
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoInfo, SetNode, GetImageSizeAndCount, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoVAELoader, WanVideoSetBlockSwap, SetNode, SetNode, WanVideoLoraSelectMulti, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, WanVideoAnimateEmbeds, GetNode, GetNode, easy cleanGpuUsed, CR Text, WanVideoSampler, easy cleanGpuUsed, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, ImageConcanate, OnnxDetectionModelLoader, SeCModelLoader, SeCVideoSegmentation, InvertMask, MaskToImage, Reroute, LayerUtility: ImageBlend, DrawViTPose, easy cleanGpuUsed, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GrowMask, SetNode, GetNode, DrawMaskOnImage, easy cleanGpuUsed, ImageFromBatch+, PointsEditor, VHS_VideoCombine, SetNode, SetNode, INTConstant, INTConstant, INTConstant, LoadImage, VHS_LoadVideo, PreviewImage, JWInteger, ImageResizeKJv2, WanVideoModelLoader, WanVideoTextEncodeCached, PoseAndFaceDetection, SetNode, SetNode, BlockifyMask, VHS_VideoCombine, PreviewImage, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/人物替换_角色替换_动作模仿_动作迁移_二创首选_ Wan2.2 Animate_2046490215514120193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046490215514120193.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `GetImageSizeAndCount`
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
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CR Text`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `OnnxDetectionModelLoader`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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
- `GrowMask`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `ImageFromBatch+`
- `PointsEditor`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`
- `PreviewImage`
- `JWInteger`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `VHS_VideoCombine`
- `PreviewImage`
- `Note`

## 知识

覆盖率 **59%**（46/78）

**有卡**：`VHS_VideoInfo`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`CR Text`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`、`OnnxDetectionModelLoader`、`SeCModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`MaskToImage`、`LayerUtility: ImageBlend`、`DrawViTPose`、`VHS_VideoCombine`、`GrowMask`、`DrawMaskOnImage`、`ImageFromBatch+`、`PointsEditor`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`JWInteger`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`PoseAndFaceDetection`、`BlockifyMask`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
