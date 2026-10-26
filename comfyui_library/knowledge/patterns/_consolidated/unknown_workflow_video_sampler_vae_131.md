---
name: unknown_workflow_video_sampler_vae_131
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.445
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkWav2VecEmbeds, PreviewAny, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoImageToVideoSkyreelsv3_audio, WanVideoModelLoader, WanVideoPassImagesFromSamples, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader, Wav2VecModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/SkyReels-V3 音频驱动数字人 对口型 skyreels_2027275262676705281.json, 视频生成/图生视频/wanvideo_2_1_14B_A2V_SkyReelsV31_2019435864274771969.json, 视频生成/图生视频/wanvideo_2_1_14B_A2V_SkyReelsV31_2058833651323990018.json, 视频生成/文生视频/02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_131

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/SkyReels-V3 音频驱动数字人 对口型 skyreels_2027275262676705281.json、视频生成/图生视频/wanvideo_2_1_14B_A2V_SkyReelsV31_2019435864274771969.json、视频生成/图生视频/wanvideo_2_1_14B_A2V_SkyReelsV31_2058833651323990018.json、视频生成/文生视频/02-SkyReelsV3_TalkingAvatar 数字人+唇形同步 RH工作流_2029563194267672578.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoSkyreelsv3_audio`
- `WanVideoModelLoader`
- `WanVideoPassImagesFromSamples`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/4 个有
- `DownloadAndLoadWav2VecModel` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `AudioCrop` —— 1/4 个有
- `FB_Qwen3TTSVoiceClone` —— 1/4 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Float` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `Qwen3ASRLoader` —— 1/4 个有
- `Qwen3ASRTranscribe` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `Textbox` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
