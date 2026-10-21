---
name: unknown_workflow_video_sampler_vae_92
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.855667
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1960200175715299330.json, 视频生成/图生视频/2044939873613783041.json, 视频生成/图生视频/2078771569698099202.json, 视频生成/图生视频/2080723260165152769.json, 视频生成/图生视频/数字人口播_2106320471296925698.json, 视频生成/文生视频/数字人口播_2106320471296925698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_92

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1960200175715299330.json、视频生成/图生视频/2044939873613783041.json、视频生成/图生视频/2078771569698099202.json、视频生成/图生视频/2080723260165152769.json、视频生成/图生视频/数字人口播_2106320471296925698.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 5/6 个有
- `WanVideoLoraSelect` —— 5/6 个有
- `GetImageRangeFromBatch` —— 4/6 个有
- `easy int` —— 3/6 个有
- `IndexTTS2Run` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `DF_Float` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `WanVideoLoraSelectMulti` —— 1/6 个有
- `WanVideoSetBlockSwap` —— 1/6 个有
- `WanVideoSetLoRAs` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
