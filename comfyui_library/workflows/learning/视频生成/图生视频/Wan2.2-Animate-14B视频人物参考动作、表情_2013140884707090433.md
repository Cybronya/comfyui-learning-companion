---
key: 视频生成/图生视频/Wan2.2-Animate-14B视频人物参考动作、表情_2013140884707090433.json
name: Wan2.2-Animate-14B视频人物参考动作、表情_2013140884707090433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-14B视频人物参考动作、表情_2013140884707090433.json
hash: c8e99fffcb6af546
coverage: 0.918919
learned_at: 2026-10-15 22:34:29
nodes: [WanVideoDecode, WanVideoSetBlockSwap, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, easy showAnything, GetImageSizeAndCount, VHS_VideoCombine, DrawViTPose, WanVideoBlockSwap, WanVideoSampler, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, easy int, easy int, Evaluate Integers, WanVideoSetLoRAs, WanVideoVAELoader, CLIPVisionLoader, WanVideoTextEncodeCached, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoContextOptions, WanVideoClipVisionEncode, easy int, ImageConcatMulti, ImageConcatMulti, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoInfoLoaded, Evaluate Integers, WanVideoAnimateEmbeds, LayerUtility: ImageMaskScaleAsV2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate-14B视频人物参考动作、表情_2013140884707090433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2013140884707090433.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `easy showAnything`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `DrawViTPose`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `Evaluate Integers`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoContextOptions`
- `WanVideoClipVisionEncode`
- `easy int`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `Evaluate Integers`
- `WanVideoAnimateEmbeds`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`WanVideoDecode`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`DrawViTPose`、`WanVideoBlockSwap`、`WanVideoSampler`、`LayerUtility: PurgeVRAM V2`、`easy int`、`Evaluate Integers`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoContextOptions`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`VHS_VideoInfoLoaded`、`WanVideoAnimateEmbeds`、`LayerUtility: ImageMaskScaleAsV2`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
