---
name: unknown_workflow_video_lora_sampler_385
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.74
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2_3 infinate talk_1958473679946543105.json, 图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json, 图片生成/文生图/wan2_3 infinate talk_1958496258287681537.json, 图片生成/文生图/zpzszr_2080531792297287681.json, 数字人/数字人/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_api+(8)_2078178475407659010.json, 数字人/数字人/infinitetalk多段mv生成5段_1995307640144191489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_385

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/wan2_3 infinate talk_1958473679946543105.json、图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json、图片生成/文生图/wan2_3 infinate talk_1958496258287681537.json、图片生成/文生图/zpzszr_2080531792297287681.json、数字人/数字人/InfiniteTalk数字人图生长视频-自动对口型（支持唱歌_说话）_api+(8)_2078178475407659010.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
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
- `SimpleMath+` —— 5/6 个有
- `WanVideoImageToVideoMultiTalk` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `AudioSeparation` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `LoadWanVideoT5TextEncoder` —— 4/6 个有
- `RH_GetAudioDuration` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `WanVideoTextEncode` —— 4/6 个有
- `Float to Int` —— 2/6 个有
- `Int` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `WanVideoTextEncodeCached` —— 2/6 个有
- `Display Int (rgthree)` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `SaveAudioOpus` —— 1/6 个有
- `SeparateMasks` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有
- `SoundFlow_TrimAudio` —— 1/6 个有
- `WanVideoImageToVideoEncode` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
