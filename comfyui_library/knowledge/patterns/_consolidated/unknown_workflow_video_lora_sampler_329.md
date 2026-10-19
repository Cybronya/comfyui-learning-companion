---
name: unknown_workflow_video_lora_sampler_329
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.835286
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1960200175715299330.json, 视频生成/图生视频/2080630602679803906.json, 视频生成/图生视频/2061461382494769153.json, 视频生成/图生视频/2061456753035923458.json, 视频生成/图生视频/2076965188426878978.json, 视频生成/图生视频/2061428743545114626.json, 视频生成/图生视频/2052234323893465089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_329

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1960200175715299330.json、视频生成/图生视频/2080630602679803906.json、视频生成/图生视频/2061461382494769153.json、视频生成/图生视频/2061456753035923458.json、视频生成/图生视频/2076965188426878978.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `Audio Duration (mtb)`
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `PlaySound|pysssss` —— 5/7 个有
- `Anything Everywhere` —— 1/7 个有
- `Apply Whisper` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `DF_Float` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `IndexTTS2Run` —— 1/7 个有
- `MelBandRoFormerModelLoader` —— 1/7 个有
- `MelBandRoFormerSampler` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `WanVideoTorchCompileSettings` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
