---
name: unknown_workflow_video_lora_sampler_648
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.937333
common_nodes: [AudioSeparation, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1960541577531842561.json, 视频生成/图生视频/2035945836609277954.json, 视频生成/图生视频/1968146725170982914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_648

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1960541577531842561.json、视频生成/图生视频/2035945836609277954.json、视频生成/图生视频/1968146725170982914.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_GetAudioDuration` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `Display Int (rgthree)` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImageScaleToMegapixels` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SeparateMasks` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `SoundFlow_TrimAudio` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
