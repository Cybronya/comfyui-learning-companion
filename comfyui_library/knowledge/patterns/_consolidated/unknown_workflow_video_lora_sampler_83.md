---
name: unknown_workflow_video_lora_sampler_83
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.906158
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2_3 infinate talk_1958473679946543105.json, 图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json, 图片生成/文生图/wan2_3 infinate talk_1958496258287681537.json, 图片生成/文生图/zpzszr_2080531792297287681.json, 平台全量/视频单人口播_1976468308692176898.json, 数字人/数字人/infinitetalk单人_1971164845422845953.json, 数字人/数字人/infinitetalk单人_1982997553975296001.json, 数字人/数字人/infinitetalk单人_2015405889087348737.json, 数字人/数字人/infinitetalk单人_2045855900015009793.json, 数字人/数字人/infinitetalk单人数字人 横版_2082645345531682818.json, 数字人/数字人/infinitetalk数字人_1958547075095019522.json, 数字人/数字人/multi synic_1992613566192873473.json, 数字人/数字人/出单捷径：生成虚拟IP口播数字人视频工作流_2043705488394686466.json, 数字人/数字人/图片+音频对口型_2039190838558855170.json, 数字人/数字人/常用Infinite Talk单人版 720P_2002190519998529538.json, 数字人/数字人/数字人_新闻_带货_口播_2059369980210270210.json, 数字人/数字人/数字人infinitetalk_2017517708992057345.json, 视频生成/图生视频/Infinite Talk单人版_1968672721771143169.json, 视频生成/图生视频/Infinite Talk数字人_2069716627356217345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/wan2_3 infinate talk_1958473679946543105.json、图片生成/文生图/wan2.2 multitalk 数字人_1956947526549999617.json、图片生成/文生图/wan2_3 infinate talk_1958496258287681537.json、图片生成/文生图/zpzszr_2080531792297287681.json、平台全量/视频单人口播_1976468308692176898.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 19 个 workflow 都包含：
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_GetAudioDuration` —— 18/19 个有
- `SimpleMath+` —— 18/19 个有
- `WanVideoImageToVideoMultiTalk` —— 18/19 个有
- `AudioCrop` —— 17/19 个有
- `AudioSeparation` —— 17/19 个有
- `LoadWanVideoT5TextEncoder` —— 17/19 个有
- `WanVideoTextEncode` —— 17/19 个有
- `Int` —— 16/19 个有
- `ToInt` —— 15/19 个有
- `easy showAnything` —— 15/19 个有
- `GetNode` —— 3/19 个有
- `SetNode` —— 3/19 个有
- `PreviewImage` —— 2/19 个有
- `WanVideoTextEncodeCached` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `Float to Int` —— 1/19 个有
- `GetImageRangeFromBatch` —— 1/19 个有
- `Image Comparer (rgthree)` —— 1/19 个有
- `IndexTTS2_Basic` —— 1/19 个有
- `MaskPreview+` —— 1/19 个有
- `SaveAudioOpus` —— 1/19 个有
- `SeedVR2` —— 1/19 个有
- `SeedVR2BlockSwap` —— 1/19 个有
- `SeparateMasks` —— 1/19 个有
- `WanVideoImageToVideoEncode` —— 1/19 个有
- `easy anythingIndexSwitch` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
