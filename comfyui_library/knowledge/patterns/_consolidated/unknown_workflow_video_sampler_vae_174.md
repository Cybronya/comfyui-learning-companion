---
name: unknown_workflow_video_sampler_vae_174
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7625
common_nodes: [CLIPVisionLoader, CreateVideo, ImageResizeKJv2, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SaveVideo, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk数字人-照片语音口播工作流_2095011792023015426.json, 视频生成/文生视频/wan2_1_infinitetalk_music数字人+全节点注释_2055791893207887873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_174

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk数字人-照片语音口播工作流_2095011792023015426.json、视频生成/文生视频/wan2_1_infinitetalk_music数字人+全节点注释_2055791893207887873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CreateVideo`
- `ImageResizeKJv2`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SaveVideo`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 1/2 个有
- `DownloadAndLoadWav2VecModel` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `VHS_LoadAudioUpload` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `Wav2VecModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
