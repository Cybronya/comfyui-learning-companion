---
name: unknown_workflow_video_sampler_vae_64
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.947
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/人物对口型_2035299713183916034.json, 平台全量/InfiniteTalk视频对口型工作流_2070777463252279297.json, 平台全量/Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793.json, 平台全量/infinitetalk_视频对口型，无限时长_1980865039265611778.json, 数字人/数字人/infinitetalk数字人_2084490925362999297.json, 数字人/数字人/视频对口型，无限时长——infinitetalk视频对口型，video2video_1958795663838437378.json, 数字人/数字人/视频数字人最新优化版infinitetalk_2035600145890418689.json, 数字人/数字人/视频数字人最新优化版infinitetalk_2045833153872400385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_64

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/人物对口型_2035299713183916034.json、平台全量/InfiniteTalk视频对口型工作流_2070777463252279297.json、平台全量/Infinitetalk视频数字人最新优化版 V1.0_2040910072682913793.json、平台全量/infinitetalk_视频对口型，无限时长_1980865039265611778.json、数字人/数字人/infinitetalk数字人_2084490925362999297.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 7/8 个有
- `WanVideoEncode` —— 7/8 个有
- `WanVideoLoraSelectMulti` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `AudioCrop` —— 6/8 个有
- `LoadAudio` —— 6/8 个有
- `ImageResizeKJv2` —— 5/8 个有
- `Audio Duration (mtb)` —— 4/8 个有
- `GetImageRangeFromBatch` —— 4/8 个有
- `LoadWanVideoT5TextEncoder` —— 4/8 个有
- `MathExpression|pysssss` —— 4/8 个有
- `VHS_VideoInfo` —— 4/8 个有
- `WanVideoTextEncode` —— 4/8 个有
- `WanVideoTextEncodeCached` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `INTConstant` —— 2/8 个有
- `ImageFromBatch` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `WanVideoEnhanceAVideo` —— 2/8 个有
- `WanVideoExperimentalArgs` —— 2/8 个有
- `WanVideoSLG` —— 2/8 个有
- `WanVideoTeaCache` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `ImageConcatMulti` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
