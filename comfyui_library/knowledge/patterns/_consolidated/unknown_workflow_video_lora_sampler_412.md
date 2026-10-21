---
name: unknown_workflow_video_lora_sampler_412
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8478
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1983563401169444866.json, 视频生成/图生视频/1958425733460815874.json, 视频生成/图生视频/1968672721771143169.json, 视频生成/图生视频/2069716627356217345.json, 视频生成/图生视频/2080617453847138306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_412

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1983563401169444866.json、视频生成/图生视频/1958425733460815874.json、视频生成/图生视频/1968672721771143169.json、视频生成/图生视频/2069716627356217345.json、视频生成/图生视频/2080617453847138306.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `Int` —— 4/5 个有
- `ToInt` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `SaveAudio` —— 3/5 个有
- `Audio Duration (mtb)` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `IndexTTS2_Emotion` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `RH_GetAudioDuration` —— 2/5 个有
- `GetAudioDurationFromAudio` —— 1/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `IndexTTS2Run` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2BlockSwap` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
