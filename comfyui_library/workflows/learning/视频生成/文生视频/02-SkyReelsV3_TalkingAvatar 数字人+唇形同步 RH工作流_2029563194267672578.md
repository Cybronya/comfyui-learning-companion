---
key: 视频生成/文生视频/02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578.json
name: 02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578.json
hash: accdccea0e00455b
coverage: 0.419355
learned_at: 2026-10-10 22:58:09
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, MultiTalkWav2VecEmbeds, WanVideoClipVisionEncode, MarkdownNote, SetNode, GetNode, SetNode, GetNode, Note, SetNode, ImageResizeKJv2, Note, MelBandRoFormerModelLoader, MarkdownNote, MarkdownNote, WanVideoPassImagesFromSamples, Note, WanVideoImageToVideoSkyreelsv3_audio, WanVideoSamplerv2, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoDecode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, WanVideoSamplerExtraArgs, MarkdownNote, MarkdownNote, FB_Qwen3TTSVoiceClone, Qwen3ASRTranscribe, Qwen3ASRLoader, ShowText|pysssss, FB_Qwen3TTSVoiceClonePrompt, GetNode, MelBandRoFormerSampler, SetNode, SetNode, GetNode, GetNode, Any Switch (rgthree), WanVideoSetBlockSwap, Note, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, WanVideoSchedulerv2, Wav2VecModelLoader, DownloadAndLoadWav2VecModel, VHS_VideoCombine, WanVideoTextEncodeCached, SetNode, LoadAudio, INTConstant, SetNode, GetNode, GetNode, PreviewAny, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, GetNode, GetNode, Note, PreviewAudio, VHS_VideoCombine, LoadAudio, AudioCrop, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, INTConstant, INTConstant, WanVideoTextEncodeCached, Textbox]
patterns: []
missing: []
---

# 视频生成/文生视频/02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（93 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `MultiTalkWav2VecEmbeds`
- `WanVideoClipVisionEncode`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `SetNode`
- `ImageResizeKJv2`
- `Note`
- `MelBandRoFormerModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoPassImagesFromSamples`
- `Note`
- `WanVideoImageToVideoSkyreelsv3_audio`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSamplerExtraArgs` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `FB_Qwen3TTSVoiceClone`
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `ShowText|pysssss`
- `FB_Qwen3TTSVoiceClonePrompt`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoSchedulerv2`
- `Wav2VecModelLoader`
- `DownloadAndLoadWav2VecModel`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `SetNode`
- `LoadAudio`
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `PreviewAudio`
- `VHS_VideoCombine`
- `LoadAudio`
- `AudioCrop`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncodeCached`
- `Textbox`

## 知识

覆盖率 **42%**（39/93）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`MultiTalkWav2VecEmbeds`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`MelBandRoFormerModelLoader`、`WanVideoPassImagesFromSamples`、`WanVideoImageToVideoSkyreelsv3_audio`、`WanVideoSamplerv2`、`WanVideoSamplerExtraArgs`、`WanVideoDecode`、`FB_Qwen3TTSVoiceClone`、`Qwen3ASRTranscribe`、`Qwen3ASRLoader`、`FB_Qwen3TTSVoiceClonePrompt`、`MelBandRoFormerSampler`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSchedulerv2`、`Wav2VecModelLoader`、`DownloadAndLoadWav2VecModel`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`LoadAudio`、`INTConstant`、`WanVideoImageToVideoEncode`、`PreviewAudio`、`AudioCrop`、`LoadImage`、`Textbox`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
