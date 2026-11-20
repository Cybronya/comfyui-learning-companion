---
key: 平台全量/Wan2.2 -Animate 人物替换-视频二创_2056294860973498370.json
name: Wan2.2 -Animate 人物替换-视频二创_2056294860973498370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 -Animate 人物替换-视频二创_2056294860973498370.json
hash: 46d4a3e448d5e138
coverage: 0.87234
learned_at: 2026-11-14 01:04:49
nodes: [MaskToImage, BlockifyMask, CR Text, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, GetImageSizeAndCount, PreviewImage, Note, Note, PointsEditor, ImageFromBatch+, JWInteger, PreviewImage, DrawViTPose, OnnxDetectionModelLoader, PoseAndFaceDetection, GrowMask, SeCVideoSegmentation, InvertMask, PreviewImage, LayerUtility: ImageBlend, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, CM_IntToFloat, SeCModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoDecode, WanVideoTextEncodeCached, CLIPVisionLoader, VHS_VideoCombine, VHS_LoadVideo, INTConstant, LoadImage, INTConstant, INTConstant]
patterns: []
missing: []
---

# 平台全量/Wan2.2 -Animate 人物替换-视频二创_2056294860973498370.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 -Animate 人物替换-视频二创_2056294860973498370.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（47 个）：
- `MaskToImage`
- `BlockifyMask`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `GetImageSizeAndCount`
- `PreviewImage`
- `Note`
- `Note`
- `PointsEditor`
- `ImageFromBatch+`
- `JWInteger`
- `PreviewImage`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GrowMask`
- `SeCVideoSegmentation`
- `InvertMask`
- `PreviewImage`
- `LayerUtility: ImageBlend`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `CM_IntToFloat`
- `SeCModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`MaskToImage`、`BlockifyMask`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`PointsEditor`、`ImageFromBatch+`、`JWInteger`、`DrawViTPose`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GrowMask`、`SeCVideoSegmentation`、`InvertMask`、`LayerUtility: ImageBlend`、`VHS_VideoCombine`、`DrawMaskOnImage`、`CM_IntToFloat`、`SeCModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`VHS_LoadVideo`、`INTConstant`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
