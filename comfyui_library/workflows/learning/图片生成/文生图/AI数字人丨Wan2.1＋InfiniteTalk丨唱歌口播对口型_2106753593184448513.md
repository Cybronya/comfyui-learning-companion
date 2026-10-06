---
key: 图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json
name: AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json
hash: c33a84d9717a8248
coverage: 0.030303
learned_at: 2026-10-06 21:44:48
nodes: [WanVideoBlockSwap, FlashVSRNode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, Int, MultiTalkWav2VecEmbeds, PrimitiveStringMultiline, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, SoundFlow_TrimAudio, Fast Groups Muter (rgthree), AudioSeparation, RH_GetAudioDuration, Float to Int, SimpleMath+, LoadAudio, LoadImage]
patterns: []
missing: [AudioSeparation, DownloadAndLoadWav2VecModel, Fast Groups Muter (rgthree), FlashVSRNode, Float to Int, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RH_GetAudioDuration, SimpleMath+, SoundFlow_TrimAudio, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader]
discoveries: [次要节点 `AudioSeparation` 知识库中没有该节点类型的任何知识, 次要节点 `DownloadAndLoadWav2VecModel` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `FlashVSRNode` 知识库中没有该节点类型的任何知识, 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识, 次要节点 `Int` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LoadAudio` 知识库中没有该节点类型的任何知识, 次要节点 `MultiTalkModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `MultiTalkWav2VecEmbeds` 知识库中没有该节点类型的任何知识, 次要节点 `RH_GetAudioDuration` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SoundFlow_TrimAudio` 知识库中没有该节点类型的任何知识, 次要节点 `VHS_VideoCombine` 知识库中没有该节点类型的任何知识, 次要节点 `VHS_VideoCombine` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoBlockSwap` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoEasyCache` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoEnhanceAVideo` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoExperimentalArgs` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoImageToVideoMultiTalk` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `WanVideoSLG` 知识库中没有该节点类型的任何知识, 核心节点 `WanVideoSampler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `CLIPVisionLoader` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `WanVideoClipVisionEncode` 仅有 VAE/CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `WanVideoDecode` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `WanVideoLoraSelect` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `WanVideoLoraSelect` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `WanVideoTextEncodeCached` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `WanVideoVAELoader` 仅有 VAE 的通用知识，没有该节点自己的说明]
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

覆盖率 **3%**（1/33）

**有卡**：`LoadImage`

**缺卡**（31）：`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`Fast Groups Muter (rgthree)`、`FlashVSRNode`、`Float to Int`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`LoadAudio`、`MultiTalkModelLoader`、`MultiTalkWav2VecEmbeds`、`RH_GetAudioDuration`、`SimpleMath+`、`SoundFlow_TrimAudio`、`VHS_VideoCombine`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoImageToVideoMultiTalk`、`WanVideoModelLoader`、`WanVideoSLG`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoLoraSelect`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`

**用到的条目**：LoadImage、sd15-t2i-basic、sd15-t2i-lora、VAELoader、KSampler、sampler_name 调整经验、steps 调整经验、cfg 调整经验

## 学习发现

- 次要节点 `AudioSeparation` 知识库中没有该节点类型的任何知识
- 次要节点 `DownloadAndLoadWav2VecModel` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `FlashVSRNode` 知识库中没有该节点类型的任何知识
- 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识
- 次要节点 `Int` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LoadAudio` 知识库中没有该节点类型的任何知识
- 次要节点 `MultiTalkModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `MultiTalkWav2VecEmbeds` 知识库中没有该节点类型的任何知识
- 次要节点 `RH_GetAudioDuration` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SoundFlow_TrimAudio` 知识库中没有该节点类型的任何知识
- 次要节点 `VHS_VideoCombine` 知识库中没有该节点类型的任何知识
- 次要节点 `VHS_VideoCombine` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoBlockSwap` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoEasyCache` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoEnhanceAVideo` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoExperimentalArgs` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoImageToVideoMultiTalk` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `WanVideoSLG` 知识库中没有该节点类型的任何知识
- 核心节点 `WanVideoSampler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `CLIPVisionLoader` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `WanVideoClipVisionEncode` 仅有 VAE/CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `WanVideoDecode` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `WanVideoLoraSelect` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `WanVideoLoraSelect` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `WanVideoTextEncodeCached` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `WanVideoVAELoader` 仅有 VAE 的通用知识，没有该节点自己的说明
