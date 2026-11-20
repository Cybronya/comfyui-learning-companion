---
key: 平台全量/【遇见AI】wan2.1 MiniMaxRemover视频元素去除，可以去除物体，水印，字幕_2075874284672737282.json
name: 【遇见AI】wan2.1 MiniMaxRemover视频元素去除，可以去除物体，水印，字幕_2075874284672737282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【遇见AI】wan2.1 MiniMaxRemover视频元素去除，可以去除物体，水印，字幕_2075874284672737282.json
hash: f4ba7bc9dc0eed4f
coverage: 0.971429
learned_at: 2026-11-14 01:25:38
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoBlockSwap, WanVideoExperimentalArgs, ImageCompositeMasked, WanVideoSampler, MaskToImage, SolidMask, WanVideoMiniMaxRemoverEmbeds, MaskToImage, WanVideoLoraSelect, GrowMaskWithBlur, WanVideoEncode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, LoadImage, LoadImage, SAM3_Detect, ImageResizeKJv2, MaskPreview+, VHS_VideoCombine, CLIPTextEncode, PointsEditor, VHS_LoadVideo, CheckpointLoaderSimple, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoVAELoader]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 平台全量/【遇见AI】wan2.1 MiniMaxRemover视频元素去除，可以去除物体，水印，字幕_2075874284672737282.json

> 来源文件 `comfyui_library/workflows/平台全量/【遇见AI】wan2.1 MiniMaxRemover视频元素去除，可以去除物体，水印，字幕_2075874284672737282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（35 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoExperimentalArgs`
- `ImageCompositeMasked`
- `WanVideoSampler` ★核心
- `MaskToImage`
- `SolidMask`
- `WanVideoMiniMaxRemoverEmbeds`
- `MaskToImage`
- `WanVideoLoraSelect`
- `GrowMaskWithBlur`
- `WanVideoEncode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `SAM3_Detect`
- `ImageResizeKJv2`
- `MaskPreview+`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PointsEditor`
- `VHS_LoadVideo`
- `CheckpointLoaderSimple` ★核心
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoExperimentalArgs`、`ImageCompositeMasked`、`WanVideoSampler`、`MaskToImage`、`SolidMask`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoLoraSelect`、`GrowMaskWithBlur`、`WanVideoEncode`、`VHS_VideoCombine`、`LoadImage`、`SAM3_Detect`、`ImageResizeKJv2`、`MaskPreview+`、`CLIPTextEncode`、`PointsEditor`、`VHS_LoadVideo`、`CheckpointLoaderSimple`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
