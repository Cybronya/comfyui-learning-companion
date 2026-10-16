---
key: 视频生成/图生视频/Wan2.1 FusionX ｜ Self-Forcing 极速图生视频_1935274607635267585.json
name: Wan2.1 FusionX ｜ Self-Forcing 极速图生视频_1935274607635267585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935274607635267585.json
hash: db0907e188668237
coverage: 0.847826
learned_at: 2026-10-15 22:30:21
nodes: [WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadImage, Int, Int, Number to Float, ImageListToImageBatch, WanVideoSampler, GetImageRangeFromBatch, SaveImage, PreviewImage, Logic Boolean, easy ifElse, Image Aspect Ratio, ImageFromBatch+, UpscaleModelLoader, WanVideoSLG, WanVideoExperimentalArgs, MarkdownNote, Fast Groups Bypasser (rgthree), easy ifElse, ImageUpscaleWithModel, VHS_VideoCombine, FILM VFI, GetImageRangeFromBatch, SaveImage, PreviewImage, ImageScale, VHS_VideoCombine, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoLoraSelect, Fast Bypasser (rgthree), WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, easy int, PreviewImage, WanVideoBlockSwap, easy int, VHS_VideoCombine, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 FusionX ｜ Self-Forcing 极速图生视频_1935274607635267585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935274607635267585.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadImage`
- `Int`
- `Int`
- `Number to Float`
- `ImageListToImageBatch`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `SaveImage`
- `PreviewImage`
- `Logic Boolean`
- `easy ifElse`
- `Image Aspect Ratio`
- `ImageFromBatch+`
- `UpscaleModelLoader`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `easy ifElse`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `FILM VFI`
- `GetImageRangeFromBatch`
- `SaveImage`
- `PreviewImage`
- `ImageScale`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoLoraSelect`
- `Fast Bypasser (rgthree)`
- `WanVideoLoraSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `PreviewImage`
- `WanVideoBlockSwap`
- `easy int`
- `VHS_VideoCombine`
- `WanVideoTextEncode`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadImage`、`Int`、`Number to Float`、`ImageListToImageBatch`、`WanVideoSampler`、`GetImageRangeFromBatch`、`SaveImage`、`Logic Boolean`、`Image Aspect Ratio`、`ImageFromBatch+`、`UpscaleModelLoader`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`FILM VFI`、`ImageScale`、`WanVideoEnhanceAVideo`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`Fast Bypasser (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`WanVideoBlockSwap`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
