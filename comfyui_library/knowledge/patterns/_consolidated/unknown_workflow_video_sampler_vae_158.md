---
name: unknown_workflow_video_sampler_vae_158
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.827333
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk数字人-照片语音口播工作流_2095011792023015426.json, 视频生成/文生视频/wan2_1_infinitetalk_music数字人+全节点注释_2055791893207887873.json, 音频生成/音频生成/InfiniteTalk-多人数字人_1991115212053131266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_158

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk数字人-照片语音口播工作流_2095011792023015426.json、视频生成/文生视频/wan2_1_infinitetalk_music数字人+全节点注释_2055791893207887873.json、音频生成/音频生成/InfiniteTalk-多人数字人_1991115212053131266.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 2/3 个有
- `CreateVideo` —— 2/3 个有
- `DownloadAndLoadWav2VecModel` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `VHS_LoadAudioUpload` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `WanVideoBlockSwap` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `Wav2VecModelLoader` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
