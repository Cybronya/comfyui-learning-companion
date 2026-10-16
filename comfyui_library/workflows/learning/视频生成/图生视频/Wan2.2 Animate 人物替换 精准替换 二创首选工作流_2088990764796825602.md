---
key: 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602.json
name: Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602.json
hash: 08eae57f87ef5efe
coverage: 0.518072
learned_at: 2026-10-16 21:43:35
nodes: [GetNode, GetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, LayerUtility: ImageBlend, SetNode, DrawMaskOnImage, GetNode, SetNode, Reroute, MaskToImage, SeCModelLoader, InvertMask, Reroute, GetImageSizeAndCount, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, SetNode, GetNode, PreviewImage, Reroute, Reroute, ImageConcanate, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, Reroute, WanVideoTextEncodeCached, SeCVideoSegmentation, INTConstant, SetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note, VHS_VideoCombine, CR Text, BlockifyMask, GrowMask, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoInfo, PreviewImage, GetNode, GetNode, VHS_VideoCombine, VHS_LoadVideo, LoadImage, GetNode, INTConstant, INTConstant, PointsEditor, WanVideoAnimateEmbeds, WanVideoDecode, MarkdownNote, PreviewImage, SetNode, Note, JWInteger, ImageFromBatch+, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（83 个）：
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `LayerUtility: ImageBlend`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `Reroute`
- `MaskToImage`
- `SeCModelLoader`
- `InvertMask`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoTextEncodeCached`
- `SeCVideoSegmentation`
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Note`
- `VHS_VideoCombine`
- `CR Text`
- `BlockifyMask`
- `GrowMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `VHS_VideoInfo`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `PointsEditor`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `MarkdownNote`
- `PreviewImage`
- `SetNode`
- `Note`
- `JWInteger`
- `ImageFromBatch+`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **52%**（43/83）

**有卡**：`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`InvertMask`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`ImageConcanate`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`INTConstant`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`CR Text`、`BlockifyMask`、`GrowMask`、`VHS_VideoInfo`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`JWInteger`、`ImageFromBatch+`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
