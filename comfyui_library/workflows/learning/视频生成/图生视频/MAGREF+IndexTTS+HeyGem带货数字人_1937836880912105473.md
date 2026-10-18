---
key: 视频生成/图生视频/MAGREF+IndexTTS+HeyGem带货数字人_1937836880912105473.json
name: MAGREF+IndexTTS+HeyGem带货数字人_1937836880912105473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MAGREF+IndexTTS+HeyGem带货数字人_1937836880912105473.json
hash: 738e9cc9bc5f1efb
coverage: 0.960784
learned_at: 2026-10-15 22:30:30
nodes: [String Literal, ImageResizeKJ, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, ImageResizeKJ, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoTextEncode, WanVideoTeaCache, WanVideoSLG, WanVideoEnhanceAVideo, CLIPVisionLoader, WanVideoModelLoader, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, InspyrenetRembg, InspyrenetRembg, INTConstant, INTConstant, WanVideoVAELoader, WanVideoBlockSwap, WanVideoLoraSelect, ImagePadKJ, ImagePadKJ, WanVideoSampler, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, Seed Everywhere, VHS_VideoCombine, CreateVideo, LoadImage, KepStringLiteral, LayerUtility: PurgeVRAM V2, GetImageSize, WanVideoImageToVideoEncode, WanVideoDecode, IndexTTSRun, D_VideoLengthAdjuster, LoadImage, RH_HeyGemNode, ImageConcatMulti, ImageResizeKJv2, PreviewAudio, LoadAudio, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/MAGREF+IndexTTS+HeyGem带货数字人_1937836880912105473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1937836880912105473.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（51 个）：
- `String Literal`
- `ImageResizeKJ`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `ImageResizeKJ`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTextEncode`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `InspyrenetRembg`
- `InspyrenetRembg`
- `INTConstant`
- `INTConstant`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `ImagePadKJ`
- `ImagePadKJ`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `Seed Everywhere`
- `VHS_VideoCombine`
- `CreateVideo`
- `LoadImage`
- `KepStringLiteral`
- `LayerUtility: PurgeVRAM V2`
- `GetImageSize`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `IndexTTSRun`
- `D_VideoLengthAdjuster`
- `LoadImage`
- `RH_HeyGemNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `PreviewAudio`
- `LoadAudio`
- `SaveVideo`

## 知识

覆盖率 **96%**（49/51）

**有卡**：`String Literal`、`ImageResizeKJ`、`GetImageSize`、`Image Blank`、`ImageCompositeMasked`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncode`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`InspyrenetRembg`、`INTConstant`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`ImagePadKJ`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`Seed Everywhere`、`VHS_VideoCombine`、`CreateVideo`、`LoadImage`、`KepStringLiteral`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`IndexTTSRun`、`D_VideoLengthAdjuster`、`RH_HeyGemNode`、`ImageConcatMulti`、`ImageResizeKJv2`、`PreviewAudio`、`LoadAudio`、`SaveVideo`

**用到的条目**：LoadImage、WanVideoSampler、Seed Everywhere、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
