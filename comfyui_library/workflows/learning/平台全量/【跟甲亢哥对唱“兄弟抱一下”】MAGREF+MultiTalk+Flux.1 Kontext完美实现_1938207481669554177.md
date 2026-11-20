---
key: 平台全量/【跟甲亢哥对唱“兄弟抱一下”】MAGREF+MultiTalk+Flux.1 Kontext完美实现_1938207481669554177.json
name: 【跟甲亢哥对唱“兄弟抱一下”】MAGREF+MultiTalk+Flux.1 Kontext完美实现_1938207481669554177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【跟甲亢哥对唱“兄弟抱一下”】MAGREF+MultiTalk+Flux.1 Kontext完美实现_1938207481669554177.json
hash: e6ac239fddf9450a
coverage: 0.788462
learned_at: 2026-11-14 01:25:31
nodes: [CLIPVisionLoader, WanVideoDecode, ImageConcatMulti, GetImageSize, ImageResizeKJ, WanVideoClipVisionEncode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJ, PreviewImage, WanVideoVAELoader, RMBG, SetNode, SetNode, AudioSeparation, SetNode, SetNode, Audio Duration (mtb), FloatConstant, MathExpression|pysssss, WanVideoModelLoader, LoadWanVideoT5TextEncoder, GetNode, WanVideoImageToVideoEncode, LoadAudio, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, GetNode, GetNode, GetNode, WanVideoApplyNAG, WanVideoEnhanceAVideo, WanVideoSampler, WanVideoTextEncodeSingle, VHS_VideoCombine, GetNode, GetNode, ImageConcanate, LoadImage, RMBG, LoadImage, WanVideoTextEncodeSingle, Bookmark (rgthree), Bookmark (rgthree), MultiTalkModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, Bookmark (rgthree), Bookmark (rgthree), Bookmark (rgthree), VHS_VideoCombine, Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/【跟甲亢哥对唱“兄弟抱一下”】MAGREF+MultiTalk+Flux.1 Kontext完美实现_1938207481669554177.json

> 来源文件 `comfyui_library/workflows/平台全量/【跟甲亢哥对唱“兄弟抱一下”】MAGREF+MultiTalk+Flux.1 Kontext完美实现_1938207481669554177.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（52 个）：
- `CLIPVisionLoader`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetImageSize`
- `ImageResizeKJ`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoVAELoader`
- `RMBG`
- `SetNode`
- `SetNode`
- `AudioSeparation`
- `SetNode`
- `SetNode`
- `Audio Duration (mtb)`
- `FloatConstant`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `LoadAudio`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoApplyNAG`
- `WanVideoEnhanceAVideo`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeSingle`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `LoadImage`
- `RMBG`
- `LoadImage`
- `WanVideoTextEncodeSingle`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `Bookmark (rgthree)`
- `VHS_VideoCombine`
- `Label (rgthree)`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`CLIPVisionLoader`、`WanVideoDecode`、`ImageConcatMulti`、`GetImageSize`、`ImageResizeKJ`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`RMBG`、`AudioSeparation`、`Audio Duration (mtb)`、`FloatConstant`、`MathExpression|pysssss`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`LoadAudio`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoApplyNAG`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoTextEncodeSingle`、`VHS_VideoCombine`、`ImageConcanate`、`LoadImage`、`Bookmark (rgthree)`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`Label (rgthree)`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
