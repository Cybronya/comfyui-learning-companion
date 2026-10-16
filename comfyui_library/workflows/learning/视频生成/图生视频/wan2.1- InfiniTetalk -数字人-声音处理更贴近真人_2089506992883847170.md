---
key: 视频生成/图生视频/wan2.1- InfiniTetalk -数字人-声音处理更贴近真人_2089506992883847170.json
name: wan2.1- InfiniTetalk -数字人-声音处理更贴近真人_2089506992883847170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1- InfiniTetalk -数字人-声音处理更贴近真人_2089506992883847170.json
hash: e43ca44b06461d36
coverage: 1
learned_at: 2026-10-16 22:02:21
nodes: [TDQwen3TTSModelLoader, PreviewAudio, SaveAudioAdvanced, Qwen3TTSCustomVoice, VHS_VideoCombine, SeedVR2BlockSwap, SeedVR2ExtraArgs, ImageScaleToTotalPixels, MultiTalkWav2VecEmbeds, SeedVR2, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, Audio Duration (mtb), MathExpression|pysssss, DownloadAndLoadWav2VecModel, MathExpression|pysssss, AudioCombine, AudioCombine, PreviewAudio, SeedVCRun, AudioSeparation, AudioCrop, AudioCombine, CLIPVisionLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, MultiTalkModelLoader, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoMultiTalk, WanVideoDecode, VHS_VideoCombine, WanVideoSampler, GetImageRangeFromBatch, WanVideoClipVisionEncode, WanVideoTextEncode, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1- InfiniTetalk -数字人-声音处理更贴近真人_2089506992883847170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/wan2.1- InfiniTetalk -数字人-声音处理更贴近真人_2089506992883847170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `TDQwen3TTSModelLoader`
- `PreviewAudio`
- `SaveAudioAdvanced`
- `Qwen3TTSCustomVoice`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `ImageScaleToTotalPixels`
- `MultiTalkWav2VecEmbeds`
- `SeedVR2`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `DownloadAndLoadWav2VecModel`
- `MathExpression|pysssss`
- `AudioCombine`
- `AudioCombine`
- `PreviewAudio`
- `SeedVCRun`
- `AudioSeparation`
- `AudioCrop`
- `AudioCombine`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncode`
- `LoadAudio`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`TDQwen3TTSModelLoader`、`PreviewAudio`、`SaveAudioAdvanced`、`Qwen3TTSCustomVoice`、`VHS_VideoCombine`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`ImageScaleToTotalPixels`、`MultiTalkWav2VecEmbeds`、`SeedVR2`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`DownloadAndLoadWav2VecModel`、`AudioCombine`、`SeedVCRun`、`AudioSeparation`、`AudioCrop`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoMultiTalk`、`WanVideoDecode`、`WanVideoSampler`、`GetImageRangeFromBatch`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`LoadAudio`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs、WanVideoSampler、SeedVCRun、LoadWanVideoT5TextEncoder、WanVideoDecode
