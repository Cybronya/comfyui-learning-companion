---
key: 视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json
name: (Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json
hash: b03f4705dd77a2fc
coverage: 0.602041
learned_at: 2026-10-15 22:32:19
nodes: [GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, Note, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoSetLoRAs, MarkdownNote, WanVideoEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, SetNode, WanVideoTextEncodeCached, PoseRetargetPromptHelper, Reroute, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, Note, WanVideoModelLoader, GetNode, easy showAnything, DownloadAndLoadSAM2Model, Sam2Segmentation, GetNode, PointsEditor, VHS_VideoCombine, easy showAnything, ACE_ImageFaceCrop, VHS_LoadVideo, ImageResizeKJv2, GetImageSizeAndCount, DrawViTPose, PoseAndFaceDetection, OnnxDetectionModelLoader, CLIPVisionLoader, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, SetNode, GetNode, easy showAnything, WanVideoAnimateEmbeds, GetNode, SetNode, WanVideoClipVisionEncode, SetNode, ImageResizeKJv2, ImageFromBatch, PreviewImage, PrimitiveInt, ImageConcanate, DrawMaskOnImage, SetNode, DrawMaskOnImage, JWInteger, JWInteger, SetNode, WanVideoSampler, JWInteger, LoadImage, easy showAnything, VHS_VideoInfo, CR Prompt Text, VHS_LoadVideo, ClothesSegment, WanVideoDecode, VHS_VideoCombine, PDIMAGE_LongerSize, ImageConcatMulti, JWInteger, Note, Note, Note, Note, VHS_VideoCombine, BlockifyMask, GrowMask, GetNode, EmptyImage, segformer_b2_clothes, SeCModelLoader, SeCVideoSegmentation, VHS_VideoCombine, WanVideoLoraSelectMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978363035192549378.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（98 个）：
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `WanVideoTextEncodeCached`
- `PoseRetargetPromptHelper`
- `Reroute`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `Note`
- `WanVideoModelLoader`
- `GetNode`
- `easy showAnything`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `easy showAnything`
- `ACE_ImageFaceCrop`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `ImageResizeKJv2`
- `ImageFromBatch`
- `PreviewImage`
- `PrimitiveInt`
- `ImageConcanate`
- `DrawMaskOnImage`
- `SetNode`
- `DrawMaskOnImage`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `WanVideoSampler` ★核心
- `JWInteger`
- `LoadImage`
- `easy showAnything`
- `VHS_VideoInfo`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `ClothesSegment`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `BlockifyMask`
- `GrowMask`
- `GetNode`
- `EmptyImage`
- `segformer_b2_clothes`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`

## 知识

覆盖率 **60%**（59/98）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`PoseRetargetPromptHelper`、`WanVideoUni3C_ControlnetLoader`、`VHS_VideoCombine`、`WanVideoModelLoader`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`PointsEditor`、`ACE_ImageFaceCrop`、`VHS_LoadVideo`、`ImageResizeKJv2`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`ImageFromBatch`、`ImageConcanate`、`DrawMaskOnImage`、`JWInteger`、`WanVideoSampler`、`LoadImage`、`VHS_VideoInfo`、`CR Prompt Text`、`ClothesSegment`、`WanVideoDecode`、`PDIMAGE_LongerSize`、`BlockifyMask`、`GrowMask`、`EmptyImage`、`segformer_b2_clothes`、`SeCModelLoader`、`SeCVideoSegmentation`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
