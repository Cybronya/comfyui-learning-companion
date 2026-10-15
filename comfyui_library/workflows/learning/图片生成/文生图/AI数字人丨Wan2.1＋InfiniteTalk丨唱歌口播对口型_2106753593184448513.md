---
key: 图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json
name: AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json
hash: c33a84d9717a8248
coverage: 0.939394
learned_at: 2026-10-15 22:26:11
nodes: [WanVideoBlockSwap, FlashVSRNode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, Int, MultiTalkWav2VecEmbeds, PrimitiveStringMultiline, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, SoundFlow_TrimAudio, Fast Groups Muter (rgthree), AudioSeparation, RH_GetAudioDuration, Float to Int, SimpleMath+, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoBlockSwap`
- `FlashVSRNode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoEasyCache`
- `VHS_VideoCombine`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `Int`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveStringMultiline`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `SoundFlow_TrimAudio`
- `Fast Groups Muter (rgthree)`
- `AudioSeparation`
- `RH_GetAudioDuration`
- `Float to Int`
- `SimpleMath+`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`WanVideoBlockSwap`、`FlashVSRNode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoEasyCache`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`Int`、`MultiTalkWav2VecEmbeds`、`CLIPVisionLoader`、`WanVideoVAELoader`、`SoundFlow_TrimAudio`、`AudioSeparation`、`RH_GetAudioDuration`、`Float to Int`、`SimpleMath+`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
