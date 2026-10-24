---
name: unknown_workflow_video_lora_sampler_408
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9928
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json, 视频生成/图生视频/Multitalk双人对唱数字人_1941678134205038593.json, 视频生成/图生视频/infinitetalk单人图生视频对口型_1960923370206498818.json, 视频生成/图生视频/multiTalk多人对话小短剧，效果不错_1941298719130337281.json, 视频生成/图生视频/multiTalk多人对话震撼上线，效果不错_1940894901888512001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_408

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Multitalk三人多人对话+Radial Attention加速_1948369611300438017.json、视频生成/图生视频/Multitalk双人对唱数字人_1941678134205038593.json、视频生成/图生视频/infinitetalk单人图生视频对口型_1960923370206498818.json、视频生成/图生视频/multiTalk多人对话小短剧，效果不错_1941298719130337281.json、视频生成/图生视频/multiTalk多人对话震撼上线，效果不错_1940894901888512001.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 4/5 个有
- `SeparateMasks` —— 4/5 个有
- `WanVideoApplyNAG` —— 4/5 个有
- `WanVideoTextEncodeSingle` —— 4/5 个有
- `PreviewAudio` —— 3/5 个有
- `EsesImageEffectBloom` —— 2/5 个有
- `SaveAudioMP3` —— 2/5 个有
- `WanVideoExperimentalArgs` —— 2/5 个有
- `WanVideoSLG` —— 2/5 个有
- `AudioCropProcessUTK` —— 1/5 个有
- `Manual XY Entry Info` —— 1/5 个有
- `WanVideoSetRadialAttention` —— 1/5 个有
- `WanVideoTextEncode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
