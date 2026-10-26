---
key: 数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json
name: LLM+InfiniteTalk+IndexTTS_1962434815804968962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json
hash: 2178712aa16de879
coverage: 0.939394
learned_at: 2026-10-26 01:55:40
nodes: [WanVideoBlockSwap, Audio Duration (mtb), AudioCrop, Int, AudioSeparation, ToInt, SimpleMath+, easy showAnything, WanVideoDecode, MultiTalkWav2VecEmbeds, WanVideoImageToVideoMultiTalk, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadWanVideoT5TextEncoder, DownloadAndLoadWav2VecModel, CLIPVisionLoader, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, ShowText, LLMLoader, VHS_VideoCombine, WanVideoTextEncode, IndexTTSRun, LoadAudio, PreviewAudio, LLMSampler, PrimitiveStringMultiline, LoadImage, WanVideoSampler, WanVideoModelLoader]
patterns: []
missing: []
---

# 数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LLM+InfiniteTalk+IndexTTS_1962434815804968962.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoBlockSwap`
- `Audio Duration (mtb)`
- `AudioCrop`
- `Int`
- `AudioSeparation`
- `ToInt`
- `SimpleMath+`
- `easy showAnything`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `DownloadAndLoadWav2VecModel`
- `CLIPVisionLoader`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `ShowText`
- `LLMLoader`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `IndexTTSRun`
- `LoadAudio`
- `PreviewAudio`
- `LLMSampler` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoBlockSwap`、`Audio Duration (mtb)`、`AudioCrop`、`Int`、`AudioSeparation`、`ToInt`、`SimpleMath+`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`ShowText`、`LLMLoader`、`VHS_VideoCombine`、`WanVideoTextEncode`、`IndexTTSRun`、`LoadAudio`、`PreviewAudio`、`LLMSampler`、`LoadImage`、`WanVideoSampler`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LLMSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
