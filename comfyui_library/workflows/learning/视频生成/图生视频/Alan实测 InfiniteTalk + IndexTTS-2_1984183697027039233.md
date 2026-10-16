---
key: 视频生成/图生视频/Alan实测 InfiniteTalk + IndexTTS-2_1984183697027039233.json
name: Alan实测 InfiniteTalk + IndexTTS-2_1984183697027039233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1984183697027039233.json
hash: 823976ddc8dfbade
coverage: 0.8125
learned_at: 2026-10-15 22:32:47
nodes: [MultiTalkModelLoader, WanVideoVAELoader, WanVideoSampler, CLIPVisionLoader, PreviewImage, WanVideoClipVisionEncode, DownloadAndLoadWav2VecModel, WanVideoDecode, MultiTalkWav2VecEmbeds, SoundFlow_GetLength, RoundNode, MathExpression|pysssss, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, SaveAudio, IndexTTS2Run, PrimitiveString, WanVideoLoraSelect, Note, WanVideoModelLoader, ImageResizeKJv2, VHS_VideoCombine, WanVideoImageToVideoMultiTalk, LoadAudio, LoadAudio, Note, LoadImage, WanVideoTextEncode, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Alan实测 InfiniteTalk + IndexTTS-2_1984183697027039233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1984183697027039233.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（32 个）：
- `MultiTalkModelLoader`
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `PreviewImage`
- `WanVideoClipVisionEncode`
- `DownloadAndLoadWav2VecModel`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `SoundFlow_GetLength`
- `RoundNode`
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SaveAudio`
- `IndexTTS2Run`
- `PrimitiveString`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoImageToVideoMultiTalk`
- `LoadAudio`
- `LoadAudio`
- `Note`
- `LoadImage`
- `WanVideoTextEncode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`MultiTalkModelLoader`、`WanVideoVAELoader`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`SoundFlow_GetLength`、`RoundNode`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM V2`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`SaveAudio`、`IndexTTS2Run`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`LoadAudio`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
