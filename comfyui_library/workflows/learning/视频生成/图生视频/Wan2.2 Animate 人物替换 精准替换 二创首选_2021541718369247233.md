---
key: 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选_2021541718369247233.json
name: Wan2.2 Animate 人物替换 精准替换 二创首选_2021541718369247233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2021541718369247233.json
hash: 8cddc3c6de43760f
coverage: 0.518072
learned_at: 2026-10-15 22:35:08
nodes: [GetNode, WanVideoDecode, GetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, LayerUtility: ImageBlend, SetNode, DrawMaskOnImage, GetNode, SetNode, Reroute, MaskToImage, SeCModelLoader, InvertMask, Reroute, GetImageSizeAndCount, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoSampler, SetNode, GetNode, SetNode, ImageFromBatch+, PreviewImage, PreviewImage, Reroute, Reroute, ImageConcanate, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, Reroute, WanVideoTextEncodeCached, SeCVideoSegmentation, INTConstant, INTConstant, SetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, GetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note, VHS_VideoCombine, CR Text, JWInteger, PointsEditor, BlockifyMask, GrowMask, Note, Note, WanVideoAnimateEmbeds, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoInfo, PreviewImage, GetNode, GetNode, VHS_VideoCombine, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选_2021541718369247233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2021541718369247233.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（83 个）：
- `GetNode`
- `WanVideoDecode`
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
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageFromBatch+`
- `PreviewImage`
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
- `JWInteger`
- `PointsEditor`
- `BlockifyMask`
- `GrowMask`
- `Note`
- `Note`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `GetNode`
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
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **52%**（43/83）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`InvertMask`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`ImageFromBatch+`、`ImageConcanate`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`INTConstant`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`CR Text`、`JWInteger`、`PointsEditor`、`BlockifyMask`、`GrowMask`、`WanVideoAnimateEmbeds`、`VHS_VideoInfo`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
