---
key: 视频生成/文生视频/首发stand-in文生视频+Infinitetalk对口型，wan4步快速出视频_1958345524309082113.json
name: 首发stand-in文生视频+Infinitetalk对口型，wan4步快速出视频_1958345524309082113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首发stand-in文生视频+Infinitetalk对口型，wan4步快速出视频_1958345524309082113.json
hash: b1e6d19cea4a2d87
coverage: 0.923077
learned_at: 2026-10-15 22:43:42
nodes: [WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoSLG, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, FaceProcessorLoader, ApplyFaceProcessor, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoTorchCompileSettings, PreviewImage, WanVideoLoraSelectMulti, WanVideoSampler, MultiTalkModelLoader, WanVideoDecode, WanVideoTextEncode, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, AudioSeparation, ShowText|pysssss, WanVideoEncode, PreviewAudio, WanVideoContextOptions, LoadImage, CR Text, LayerUtility: TextJoin, RH_Captioner, SimpleMath+, WanVideoEmptyEmbeds, AudioGetTempo, Int, Int, Int, AudioCrop, easy showAnything, LoadAudio, WanVideoAddStandInLatent, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/首发stand-in文生视频+Infinitetalk对口型，wan4步快速出视频_1958345524309082113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958345524309082113.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（39 个）：
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `PreviewImage`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `MultiTalkModelLoader`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `AudioSeparation`
- `ShowText|pysssss`
- `WanVideoEncode`
- `PreviewAudio`
- `WanVideoContextOptions`
- `LoadImage`
- `CR Text`
- `LayerUtility: TextJoin`
- `RH_Captioner`
- `SimpleMath+`
- `WanVideoEmptyEmbeds`
- `AudioGetTempo`
- `Int`
- `Int`
- `Int`
- `AudioCrop`
- `easy showAnything`
- `LoadAudio`
- `WanVideoAddStandInLatent`
- `VHS_VideoCombine`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`MultiTalkModelLoader`、`WanVideoDecode`、`WanVideoTextEncode`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`AudioSeparation`、`WanVideoEncode`、`PreviewAudio`、`WanVideoContextOptions`、`LoadImage`、`CR Text`、`LayerUtility: TextJoin`、`RH_Captioner`、`SimpleMath+`、`WanVideoEmptyEmbeds`、`AudioGetTempo`、`Int`、`AudioCrop`、`LoadAudio`、`WanVideoAddStandInLatent`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoAddStandInLatent、WanVideoEncode
