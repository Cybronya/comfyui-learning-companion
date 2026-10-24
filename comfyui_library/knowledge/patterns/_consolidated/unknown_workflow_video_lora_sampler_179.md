---
name: unknown_workflow_video_lora_sampler_179
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8398
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2_3 infinate talk_1958473679946543105.json, 图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json, 图片生成/文生图/wan2_3 infinate talk_1958496258287681537.json, 图片生成/文生图/zpzszr_2080531792297287681.json, 视频生成/图生视频/Aiwood-infinitetalk双人对话_1957826997610446849.json, 视频生成/图生视频/INF双人对话_1971453748994359297.json, 视频生成/图生视频/InfiniteTalk图生长视频超自然-AI漫剧口播对口型（唱歌_说话）_2015607180996644865.json, 视频生成/图生视频/双人对话对口型_1994221474806513665.json, 视频生成/图生视频/数字人-口播_1901831714153324545.json, 视频生成/图生视频/最强图生双人数字人万相2.1+Infinite Talk_1958149674144321538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_179

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/wan2_3 infinate talk_1958473679946543105.json、图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json、图片生成/文生图/wan2_3 infinate talk_1958496258287681537.json、图片生成/文生图/zpzszr_2080531792297287681.json、视频生成/图生视频/Aiwood-infinitetalk双人对话_1957826997610446849.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoImageToVideoMultiTalk` —— 9/10 个有
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `AudioCrop` —— 8/10 个有
- `AudioSeparation` —— 8/10 个有
- `LoadWanVideoT5TextEncoder` —— 7/10 个有
- `WanVideoTextEncode` —— 7/10 个有
- `SimpleMath+` —— 6/10 个有
- `RH_GetAudioDuration` —— 5/10 个有
- `SeparateMasks` —— 5/10 个有
- `Float to Int` —— 4/10 个有
- `MaskPreview+` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `INTConstant` —— 3/10 个有
- `Int` —— 3/10 个有
- `PreviewAudio` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `WanVideoTextEncodeCached` —— 3/10 个有
- `easy anythingIndexSwitch` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SaveAudioOpus` —— 1/10 个有
- `SoundFlow_GetLength` —— 1/10 个有
- `WanVideoImageToVideoEncode` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
