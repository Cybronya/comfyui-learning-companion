---
key: 平台全量/wanvideo_1_3B_UniLumos_relight_1988089034918531073.json
name: wanvideo_1_3B_UniLumos_relight_1988089034918531073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_1_3B_UniLumos_relight_1988089034918531073.json
hash: 8d9a0d4a8bd625e6
coverage: 0.9
learned_at: 2026-11-14 01:20:09
nodes: [Note, VHS_LoadVideo, WanVideoSetLoRAs, WanVideoModelLoader, MarkdownNote, MarkdownNote, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, ImageResizeKJv2, TransparentBGSession+, ImageRemoveBackground+, InvertMask, DrawMaskOnImage, WanVideoEncode, ImageResizeKJv2, DrawGaussianNoiseOnImage, WanVideoEncode, WanVideoUniLumosEmbeds, WanVideoSampler]
patterns: []
missing: []
---

# 平台全量/wanvideo_1_3B_UniLumos_relight_1988089034918531073.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_1_3B_UniLumos_relight_1988089034918531073.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `Note`
- `VHS_LoadVideo`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `InvertMask`
- `DrawMaskOnImage`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `DrawGaussianNoiseOnImage`
- `WanVideoEncode`
- `WanVideoUniLumosEmbeds`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **90%**（27/30）

**有卡**：`VHS_LoadVideo`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`ImageConcatMulti`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`ImageResizeKJv2`、`TransparentBGSession+`、`ImageRemoveBackground+`、`InvertMask`、`DrawMaskOnImage`、`WanVideoEncode`、`DrawGaussianNoiseOnImage`、`WanVideoUniLumosEmbeds`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
