---
name: unknown_workflow_video_lora_sampler_412
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.976167
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SeparateMasks, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MultiTalk+LightX2v Rank64+AniWan双人加速版极限动态质量版V1（KJ）_1945360751139934210.json, 视频生成/图生视频/MultiTalk双人加速KJ版+视频放大_1941283119796535298.json, 视频生成/图生视频/MultiTalk双人加速版高质量修改版V1（KJ非真人）_1941338366120194050.json, 视频生成/图生视频/MultiTalk双人加速版高质量修改版V1（KJ）_1941135610319106050.json, 视频生成/图生视频/MultiTalk双人加速版高运动运镜版V1（KJ）_1945014615811219457.json, 视频生成/图生视频/电商带货 双人对话图生视频（multiTalk）_1944226088988053505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_412

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MultiTalk+LightX2v Rank64+AniWan双人加速版极限动态质量版V1（KJ）_1945360751139934210.json、视频生成/图生视频/MultiTalk双人加速KJ版+视频放大_1941283119796535298.json、视频生成/图生视频/MultiTalk双人加速版高质量修改版V1（KJ非真人）_1941338366120194050.json、视频生成/图生视频/MultiTalk双人加速版高质量修改版V1（KJ）_1941135610319106050.json、视频生成/图生视频/MultiTalk双人加速版高运动运镜版V1（KJ）_1945014615811219457.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SeparateMasks`
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

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 5/6 个有
- `MathExpression|pysssss` —— 5/6 个有
- `SaveAudio` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `AudioSeparation` —— 4/6 个有
- `CR Prompt Text` —— 4/6 个有
- `JWStringToInteger` —— 4/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `WanVideoExperimentalArgs` —— 3/6 个有
- `WanVideoFreeInitArgs` —— 3/6 个有
- `WanVideoSLG` —— 3/6 个有
- `ACE_AudioCrop` —— 1/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `Compare` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `Int` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
