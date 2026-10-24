---
key: 图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json
name: Wan2.2 Animate sec自动抠像人物替换_2057002999330988034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json
hash: 014450b361c44c00
coverage: 0.945946
learned_at: 2026-10-23 11:27:57
nodes: [PDIMAGE_LongerSize, ImageConcatMulti, JWInteger, WanVideoSampler, WanVideoAnimateEmbeds, DrawMaskOnImage, DrawViTPose, WanVideoVAELoader, WanVideoClipVisionEncode, BlockifyMask, ImageResizeKJv2, EmptyImage, GrowMask, SeCVideoSegmentation, SeCModelLoader, ClothesSegment, ImageFromBatch, PrimitiveInt, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelectMulti, CLIPVisionLoader, PoseAndFaceDetection, OnnxDetectionModelLoader, LoadImage, VHS_LoadVideo, PreviewImage, ACE_ImageFaceCrop, WanVideoDecode, JWInteger, JWInteger, JWInteger, VHS_VideoCombine, VHS_VideoCombine, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `PDIMAGE_LongerSize`
- `ImageConcatMulti`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `DrawMaskOnImage`
- `DrawViTPose`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `BlockifyMask`
- `ImageResizeKJv2`
- `EmptyImage`
- `GrowMask`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `ClothesSegment`
- `ImageFromBatch`
- `PrimitiveInt`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `PreviewImage`
- `ACE_ImageFaceCrop`
- `WanVideoDecode`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`PDIMAGE_LongerSize`、`ImageConcatMulti`、`JWInteger`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`DrawViTPose`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`BlockifyMask`、`ImageResizeKJv2`、`EmptyImage`、`GrowMask`、`SeCVideoSegmentation`、`SeCModelLoader`、`ClothesSegment`、`ImageFromBatch`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`LoadImage`、`VHS_LoadVideo`、`ACE_ImageFaceCrop`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
