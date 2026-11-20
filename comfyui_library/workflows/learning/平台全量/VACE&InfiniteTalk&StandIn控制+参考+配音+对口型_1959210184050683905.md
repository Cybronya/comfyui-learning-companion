---
key: 平台全量/VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905.json
name: VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905.json
hash: f46b51e26bf91430
coverage: 0.790698
learned_at: 2026-11-14 01:02:26
nodes: [Note, Note, WanVideoSetBlockSwap, WanVideoBlockSwap, Note, WanVideoSetLoRAs, WanVideoLoraSelect, MarkdownNote, MarkdownNote, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, easy showAnything, easy showAnything, easy showAnything, ImageConcatMulti, WanVideoDecode, MultiTalkModelLoader, WanVideoVACEModelSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, ApplyFaceProcessor, PreviewImage, FaceProcessorLoader, WanVideoEncode, WanVideoAddStandInLatent, AudioCrop, AudioSeparation, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, WanVideoSampler, WanVideoVAELoader, WanVideoVACEEncode, GetImageSize+, DWPreprocessor, LoadImage, LoadAudio, WanVideoModelLoader, VHS_LoadVideo, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905.json

> 来源文件 `comfyui_library/workflows/平台全量/VACE&InfiniteTalk&StandIn控制+参考+配音+对口型_1959210184050683905.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（43 个）：
- `Note`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ImageConcatMulti`
- `WanVideoDecode`
- `MultiTalkModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `ApplyFaceProcessor`
- `PreviewImage`
- `FaceProcessorLoader`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `AudioCrop`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `GetImageSize+`
- `DWPreprocessor`
- `LoadImage`
- `LoadAudio`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `ImageResizeKJv2`

## 知识

覆盖率 **79%**（34/43）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`ImageConcatMulti`、`WanVideoDecode`、`MultiTalkModelLoader`、`WanVideoVACEModelSelect`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`WanVideoVAELoader`、`ApplyFaceProcessor`、`FaceProcessorLoader`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`AudioCrop`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoSampler`、`WanVideoVACEEncode`、`GetImageSize+`、`DWPreprocessor`、`LoadImage`、`LoadAudio`、`WanVideoModelLoader`、`VHS_LoadVideo`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVACEEncode
