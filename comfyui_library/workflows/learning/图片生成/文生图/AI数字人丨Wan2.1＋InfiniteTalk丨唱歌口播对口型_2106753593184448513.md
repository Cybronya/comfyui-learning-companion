---
key: 图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json
name: AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json
hash: c33a84d9717a8248
coverage: 0.818182
learned_at: 2026-10-10 21:26:01
nodes: [WanVideoBlockSwap, FlashVSRNode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, LayerUtility: PurgeVRAM V2, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoEasyCache, VHS_VideoCombine, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoModelLoader, WanVideoTextEncodeCached, WanVideoImageToVideoMultiTalk, WanVideoSampler, Int, MultiTalkWav2VecEmbeds, PrimitiveStringMultiline, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, SoundFlow_TrimAudio, Fast Groups Muter (rgthree), AudioSeparation, RH_GetAudioDuration, Float to Int, SimpleMath+, LoadAudio, LoadImage]
patterns: []
missing: [Float to Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, SimpleMath+]
discoveries: [次要节点 `Float to Int` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI数字人丨Wan2.1＋InfiniteTalk丨唱歌口播对口型_2106753593184448513.json`

## 结构

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
- `WanVideoSampler`
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

覆盖率 **82%**（27/33）

**有卡**：`WanVideoBlockSwap`、`FlashVSRNode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoEasyCache`、`VHS_VideoCombine`、`DownloadAndLoadWav2VecModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`、`Int`、`MultiTalkWav2VecEmbeds`、`PrimitiveStringMultiline`、`CLIPVisionLoader`、`WanVideoVAELoader`、`SoundFlow_TrimAudio`、`Fast Groups Muter (rgthree)`

**缺卡**（4）：`Float to Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`

## 学习发现

- 次要节点 `Float to Int` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
