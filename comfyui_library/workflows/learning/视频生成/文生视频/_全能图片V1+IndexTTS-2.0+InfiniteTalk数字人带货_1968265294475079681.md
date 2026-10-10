---
key: 视频生成/文生视频/_全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json
name: _全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/_全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json
hash: b369399223ef73f3
coverage: 0.909091
learned_at: 2026-10-10 23:08:26
nodes: [LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, CLIPVisionLoader, AudioCrop, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTextEncode, MultiTalkWav2VecEmbeds, WanVideoImageToVideoMultiTalk, MultiTalkModelLoader, WanVideoLoraSelect, LoadImage, RH_Translator, ImageResizeKJv2, WanVideoDecode, DownloadAndLoadWav2VecModel, LayerUtility: PurgeVRAM V2, AudioSeparation, RH_Nano_Banana_Image2Image, VHS_VideoCombine, MathExpression|pysssss, SoundFlow_GetLength, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, JWStringMultiline, IndexTTS2Run, String Literal, LoadImage, PreviewAudio]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss, String Literal]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/_全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/_全能图片V1+IndexTTS-2.0+InfiniteTalk数字人带货_1968265294475079681.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `AudioCrop`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `LoadImage`
- `RH_Translator`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: PurgeVRAM V2`
- `AudioSeparation`
- `RH_Nano_Banana_Image2Image`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `SoundFlow_GetLength`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `JWStringMultiline`
- `IndexTTS2Run`
- `String Literal`
- `LoadImage`
- `PreviewAudio`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`AudioCrop`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`LoadImage`、`RH_Translator`、`ImageResizeKJv2`、`WanVideoDecode`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`RH_Nano_Banana_Image2Image`、`VHS_VideoCombine`、`SoundFlow_GetLength`、`LoadAudio`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`JWStringMultiline`、`IndexTTS2Run`、`PreviewAudio`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
