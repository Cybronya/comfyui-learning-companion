---
key: 平台全量/Wan2.2_Animate_人物替换_精准替换_二创首选_2117402267803541505.json
name: Wan2.2_Animate_人物替换_精准替换_二创首选_2117402267803541505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2_Animate_人物替换_精准替换_二创首选_2117402267803541505.json
hash: 1f085ad524692b3e
coverage: 0.518072
learned_at: 2026-11-14 01:06:14
nodes: [GetNode, WanVideoDecode, GetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, LayerUtility: ImageBlend, SetNode, DrawMaskOnImage, GetNode, SetNode, Reroute, MaskToImage, SeCModelLoader, InvertMask, Reroute, GetImageSizeAndCount, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoClipVisionEncode, WanVideoSampler, SetNode, GetNode, SetNode, ImageFromBatch+, PreviewImage, PreviewImage, Reroute, Reroute, ImageConcanate, VHS_VideoCombine, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, Reroute, WanVideoTextEncodeCached, SeCVideoSegmentation, INTConstant, INTConstant, SetNode, SetNode, WanVideoVAELoader, SetNode, WanVideoSetLoRAs, GetNode, LoadImage, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Note, VHS_VideoCombine, CR Text, JWInteger, PointsEditor, BlockifyMask, GrowMask, Note, Note, WanVideoAnimateEmbeds, INTConstant, VHS_LoadVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetImageSizeAndCount, VHS_VideoInfo, PreviewImage, GetNode, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2_Animate_人物替换_精准替换_二创首选_2117402267803541505.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2_Animate_人物替换_精准替换_二创首选_2117402267803541505.json`

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
- `LoadImage`
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
- `VHS_LoadVideo`
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

## 知识

覆盖率 **52%**（43/83）

**有卡**：`WanVideoDecode`、`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`InvertMask`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`ImageFromBatch+`、`ImageConcanate`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`SeCVideoSegmentation`、`INTConstant`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoLoraSelectMulti`、`CR Text`、`JWInteger`、`PointsEditor`、`BlockifyMask`、`GrowMask`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`VHS_VideoInfo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
