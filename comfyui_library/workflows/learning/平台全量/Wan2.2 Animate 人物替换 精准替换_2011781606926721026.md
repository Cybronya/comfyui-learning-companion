---
key: 平台全量/Wan2.2 Animate 人物替换 精准替换_2011781606926721026.json
name: Wan2.2 Animate 人物替换 精准替换_2011781606926721026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 人物替换 精准替换_2011781606926721026.json
hash: 9ee192353c287b98
coverage: 0.536585
learned_at: 2026-11-14 01:04:57
nodes: [GetNode, VHS_VideoCombine, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, PoseAndFaceDetection, LayerUtility: ImageBlend, GetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, SetNode, Reroute, MaskToImage, SeCModelLoader, InvertMask, Reroute, VHS_VideoCombine, SetNode, ImageFromBatch+, PreviewImage, PreviewImage, Reroute, Reroute, VHS_VideoCombine, Reroute, SeCVideoSegmentation, INTConstant, INTConstant, SetNode, SetNode, PreviewImage, GetNode, GetNode, Note, VHS_VideoCombine, CR Text, JWInteger, PointsEditor, BlockifyMask, GrowMask, SetNode, INTConstant, SetNode, SetNode, LoadImage, MarkdownNote, WanVideoModelLoader, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, WanVideoLoraSelectMulti, SetNode, SetNode, VHS_VideoInfo, GetImageSizeAndCount, ImageResizeKJv2, SetNode, PreviewImage, LoadImage, VHS_LoadVideo, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, GetNode, WanVideoSampler, WanVideoDecode, GetNode, GetImageSizeAndCount, GetNode, ImageConcanate, VHS_VideoCombine, Note, Note]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 人物替换 精准替换_2011781606926721026.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 人物替换 精准替换_2011781606926721026.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（82 个）：
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `LayerUtility: ImageBlend`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `MaskToImage`
- `SeCModelLoader`
- `InvertMask`
- `Reroute`
- `VHS_VideoCombine`
- `SetNode`
- `ImageFromBatch+`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `SeCVideoSegmentation`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `CR Text`
- `JWInteger`
- `PointsEditor`
- `BlockifyMask`
- `GrowMask`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `LoadImage`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `Note`
- `Note`

## 知识

覆盖率 **54%**（44/82）

**有卡**：`VHS_VideoCombine`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`InvertMask`、`ImageFromBatch+`、`SeCVideoSegmentation`、`INTConstant`、`CR Text`、`JWInteger`、`PointsEditor`、`BlockifyMask`、`GrowMask`、`LoadImage`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`VHS_VideoInfo`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcanate`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
