---
name: unknown_workflow_video_lora_sampler_262
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9955
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1948369611300438017.json, 视频生成/图生视频/1941678134205038593.json, 视频生成/图生视频/1960923370206498818.json, 视频生成/图生视频/1941298719130337281.json, 视频生成/图生视频/1940894901888512001.json, 视频生成/图生视频/1994221474806513665.json, 视频生成/图生视频/1978726455507095554.json, 视频生成/图生视频/2009633003546353665.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_262

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1948369611300438017.json、视频生成/图生视频/1941678134205038593.json、视频生成/图生视频/1960923370206498818.json、视频生成/图生视频/1941298719130337281.json、视频生成/图生视频/1940894901888512001.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
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
- `MaskPreview+` —— 7/8 个有
- `SeparateMasks` —— 7/8 个有
- `PreviewAudio` —— 6/8 个有
- `WanVideoApplyNAG` —— 4/8 个有
- `WanVideoTextEncode` —— 4/8 个有
- `WanVideoTextEncodeSingle` —— 4/8 个有
- `AudioCrop` —— 3/8 个有
- `AudioSeparation` —— 3/8 个有
- `INTConstant` —— 3/8 个有
- `EsesImageEffectBloom` —— 2/8 个有
- `SaveAudioMP3` —— 2/8 个有
- `WanVideoExperimentalArgs` —— 2/8 个有
- `WanVideoSLG` —— 2/8 个有
- `AudioCropProcessUTK` —— 1/8 个有
- `Manual XY Entry Info` —— 1/8 个有
- `WanVideoSetRadialAttention` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
