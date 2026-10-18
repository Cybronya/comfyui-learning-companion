---
key: 视频生成/图生视频/SteadyDancer-自适应骨骼迁移 版本一 12.8_1997886234179567618.json
name: SteadyDancer-自适应骨骼迁移 版本一 12.8_1997886234179567618.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SteadyDancer-自适应骨骼迁移 版本一 12.8_1997886234179567618.json
hash: ae81135af4bd4860
coverage: 0.891892
learned_at: 2026-10-15 22:33:30
nodes: [WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, Anything Everywhere3, WanVideoClipVisionEncode, WanVideoDecode, ImageUpscaleWithModel, WanVideoSamplerFromSettings, WanVideoContextOptions, WanVideoClipVisionEncode, WanVideoSamplerSettings, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, WanVideoTextEncodeCached, UpscaleModelLoader, CLIPVisionLoader, WanVideoImageToVideoEncode, LoadImage, WanVideoEncode, GetImageRangeFromBatch, SDPoseOODLoader, WanVideoAddSteadyDancerEmbeds, RIFE VFI, SDPoseOODProcessor, AILab_ImageStitch, Note, VHS_LoadVideo, Note, VHS_VideoCombine, VHS_VideoCombine, ImageResize+, GetImageSizeAndCount, FastUnsharpSharpen, VHS_VideoCombine, AILab_ImageStitch]
patterns: []
missing: []
---

# 视频生成/图生视频/SteadyDancer-自适应骨骼迁移 版本一 12.8_1997886234179567618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997886234179567618.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `Anything Everywhere3`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `ImageUpscaleWithModel`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoContextOptions`
- `WanVideoClipVisionEncode`
- `WanVideoSamplerSettings` ★核心
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `UpscaleModelLoader`
- `CLIPVisionLoader`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `SDPoseOODLoader`
- `WanVideoAddSteadyDancerEmbeds`
- `RIFE VFI`
- `SDPoseOODProcessor`
- `AILab_ImageStitch`
- `Note`
- `VHS_LoadVideo`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResize+`
- `GetImageSizeAndCount`
- `FastUnsharpSharpen`
- `VHS_VideoCombine`
- `AILab_ImageStitch`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`ImageUpscaleWithModel`、`WanVideoSamplerFromSettings`、`WanVideoContextOptions`、`WanVideoSamplerSettings`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`UpscaleModelLoader`、`CLIPVisionLoader`、`WanVideoImageToVideoEncode`、`LoadImage`、`WanVideoEncode`、`GetImageRangeFromBatch`、`SDPoseOODLoader`、`WanVideoAddSteadyDancerEmbeds`、`RIFE VFI`、`SDPoseOODProcessor`、`AILab_ImageStitch`、`VHS_LoadVideo`、`VHS_VideoCombine`、`ImageResize+`、`GetImageSizeAndCount`、`FastUnsharpSharpen`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
