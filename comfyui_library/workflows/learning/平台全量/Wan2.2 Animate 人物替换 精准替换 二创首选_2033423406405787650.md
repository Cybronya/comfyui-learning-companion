---
key: 平台全量/Wan2.2 Animate 人物替换 精准替换 二创首选_2033423406405787650.json
name: Wan2.2 Animate 人物替换 精准替换 二创首选_2033423406405787650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 人物替换 精准替换 二创首选_2033423406405787650.json
hash: 539883ad1ead6fc1
coverage: 0.529412
learned_at: 2026-11-14 01:04:54
nodes: [GetNode, WanVideoDecode, CLIPVisionLoader, Reroute, MaskToImage, SeCModelLoader, Reroute, GetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, SetNode, Reroute, Reroute, SeCVideoSegmentation, SetNode, SetNode, WanVideoVAELoader, SetNode, CR Text, Note, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, VHS_VideoCombine, WanVideoAnimateEmbeds, DrawViTPose, WanVideoModelLoader, GetNode, LayerUtility: ImageBlend, InvertMask, WanVideoSetLoRAs, PreviewImage, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeCached, VHS_VideoCombine, Note, PreviewImage, Reroute, PreviewImage, SetNode, BlockifyMask, GetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetImageSizeAndCount, SetNode, Note, PreviewImage, OnnxDetectionModelLoader, INTConstant, INTConstant, WanVideoLoraSelect, ImageConcanate, WanVideoLoraSelect, GrowMask, JWInteger, VHS_VideoInfo, ImageFromBatch+, WanVideoClipVisionEncode, WanVideoLoraSelectMulti, GetNode, VHS_VideoCombine, ImageResizeKJv2, VHS_LoadVideo, LoadImage, WanVideoLoraSelectMulti, PointsEditor, INTConstant]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 人物替换 精准替换 二创首选_2033423406405787650.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 人物替换 精准替换 二创首选_2033423406405787650.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（85 个）：
- `GetNode`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `Reroute`
- `MaskToImage`
- `SeCModelLoader`
- `Reroute`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `SetNode`
- `Reroute`
- `Reroute`
- `SeCVideoSegmentation`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `CR Text`
- `Note`
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
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `DrawViTPose`
- `WanVideoModelLoader`
- `GetNode`
- `LayerUtility: ImageBlend`
- `InvertMask`
- `WanVideoSetLoRAs`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `Note`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `Note`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `ImageConcanate`
- `WanVideoLoraSelect`
- `GrowMask`
- `JWInteger`
- `VHS_VideoInfo`
- `ImageFromBatch+`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `PointsEditor`
- `INTConstant`

## 知识

覆盖率 **53%**（45/85）

**有卡**：`WanVideoDecode`、`CLIPVisionLoader`、`MaskToImage`、`SeCModelLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`SeCVideoSegmentation`、`WanVideoVAELoader`、`CR Text`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`DrawViTPose`、`WanVideoModelLoader`、`LayerUtility: ImageBlend`、`InvertMask`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`BlockifyMask`、`DrawMaskOnImage`、`OnnxDetectionModelLoader`、`INTConstant`、`WanVideoLoraSelect`、`ImageConcanate`、`GrowMask`、`JWInteger`、`VHS_VideoInfo`、`ImageFromBatch+`、`WanVideoClipVisionEncode`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、WanVideoLoraSelectMulti
