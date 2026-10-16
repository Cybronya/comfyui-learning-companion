---
key: 视频生成/图生视频/SteadyDancer-自适应骨骼迁移-版本二 12.11_1998823321796009986.json
name: SteadyDancer-自适应骨骼迁移-版本二 12.11_1998823321796009986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998823321796009986.json
hash: 81255030b7aa01a9
coverage: 0.888889
learned_at: 2026-10-15 22:33:34
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, ImageUpscaleWithModel, WanVideoClipVisionEncode, WanVideoEncode, WanVideoAddSteadyDancerEmbeds, Anything Everywhere3, GetImageRangeFromBatch, WanVideoDecode, UpscaleModelLoader, VHS_VideoCombine, ImageResize+, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, OnnxDetectionModelLoader, WanVideoContextOptions, LayerColor: ColorAdapter, WanVideoTextEncodeCached, GetImageSizeAndCount, WanVideoImageToVideoEncode, WanVideoSamplerFromSettings, VHS_VideoCombine, WanVideoSamplerSettings, FastUnsharpSharpen, RIFE VFI, AILab_ImageStitch, MarkdownNote, MarkdownNote, MarkdownNote, PoseDetectionOneToAllAnimation, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/SteadyDancer-自适应骨骼迁移-版本二 12.11_1998823321796009986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998823321796009986.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `ImageUpscaleWithModel`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `WanVideoAddSteadyDancerEmbeds`
- `Anything Everywhere3`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `ImageResize+`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `OnnxDetectionModelLoader`
- `WanVideoContextOptions`
- `LayerColor: ColorAdapter`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `WanVideoImageToVideoEncode`
- `WanVideoSamplerFromSettings` ★核心
- `VHS_VideoCombine`
- `WanVideoSamplerSettings` ★核心
- `FastUnsharpSharpen`
- `RIFE VFI`
- `AILab_ImageStitch`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PoseDetectionOneToAllAnimation`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageUpscaleWithModel`、`WanVideoClipVisionEncode`、`WanVideoEncode`、`WanVideoAddSteadyDancerEmbeds`、`GetImageRangeFromBatch`、`WanVideoDecode`、`UpscaleModelLoader`、`VHS_VideoCombine`、`ImageResize+`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`OnnxDetectionModelLoader`、`WanVideoContextOptions`、`LayerColor: ColorAdapter`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`FastUnsharpSharpen`、`RIFE VFI`、`AILab_ImageStitch`、`PoseDetectionOneToAllAnimation`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
