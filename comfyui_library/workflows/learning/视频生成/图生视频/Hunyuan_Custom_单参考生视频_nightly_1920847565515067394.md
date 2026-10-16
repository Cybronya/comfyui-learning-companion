---
key: 视频生成/图生视频/Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json
name: Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1920847565515067394.json
hash: 080c0ac6f21aa0ff
coverage: 0.942857
learned_at: 2026-10-15 22:29:43
nodes: [GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, ImageConcatMulti, HyVideoTextEmbedBridge, HyVideoBlockSwap, LayerMask: TransparentBackgroundUltra, CLIPVisionLoader, CLIPVisionEncode, TextEncodeHunyuanVideo_ImageToVideo, Note, HyVideoVAELoader, HyVideoTorchCompileSettings, HyVideoDecode, DualCLIPLoader, PreviewImage, Image Crop Face, Images to RGB, LoadImage, VHS_VideoCombine, VHS_VideoCombine, LoadImage, Image Crop Face, LayerMask: TransparentBackgroundUltra, LayerUtility: ImageRemoveAlpha, ImageConcanate, LayerUtility: ImageRemoveAlpha, ImageResizeKJv2, TextEncodeHunyuanVideo_ImageToVideo, HyVideoModelLoader, HyVideoEncode, HyVideoTeaCache, HunyuanVideoSLG, HyVideoSampler, HunyuanVideoFresca, LayerUtility: TextBox]
patterns: []
missing: []
---

# 视频生成/图生视频/Hunyuan_Custom_单参考生视频_nightly_1920847565515067394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1920847565515067394.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `ImageConcatMulti`
- `HyVideoTextEmbedBridge`
- `HyVideoBlockSwap`
- `LayerMask: TransparentBackgroundUltra`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `Note`
- `HyVideoVAELoader`
- `HyVideoTorchCompileSettings`
- `HyVideoDecode`
- `DualCLIPLoader`
- `PreviewImage`
- `Image Crop Face`
- `Images to RGB`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `Image Crop Face`
- `LayerMask: TransparentBackgroundUltra`
- `LayerUtility: ImageRemoveAlpha`
- `ImageConcanate`
- `LayerUtility: ImageRemoveAlpha`
- `ImageResizeKJv2`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `HyVideoModelLoader`
- `HyVideoEncode`
- `HyVideoTeaCache`
- `HunyuanVideoSLG`
- `HyVideoSampler` ★核心
- `HunyuanVideoFresca`
- `LayerUtility: TextBox`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`ImageConcatMulti`、`HyVideoTextEmbedBridge`、`HyVideoBlockSwap`、`LayerMask: TransparentBackgroundUltra`、`CLIPVisionLoader`、`CLIPVisionEncode`、`TextEncodeHunyuanVideo_ImageToVideo`、`HyVideoVAELoader`、`HyVideoTorchCompileSettings`、`HyVideoDecode`、`DualCLIPLoader`、`Image Crop Face`、`Images to RGB`、`LoadImage`、`VHS_VideoCombine`、`LayerUtility: ImageRemoveAlpha`、`ImageConcanate`、`ImageResizeKJv2`、`HyVideoModelLoader`、`HyVideoEncode`、`HyVideoTeaCache`、`HunyuanVideoSLG`、`HyVideoSampler`、`HunyuanVideoFresca`、`LayerUtility: TextBox`

**用到的条目**：LoadImage、HyVideoSampler、CLIPVisionEncode、TextEncodeHunyuanVideo_ImageToVideo、HyVideoDecode、HyVideoVAELoader、HyVideoEncode、CLIPVisionLoader
