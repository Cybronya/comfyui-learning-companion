---
name: unknown_workflow_video_lora_sampler_431
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7078
common_nodes: [GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2021226831017418753.json, 视频生成/图生视频/2003700180081909761.json, 视频生成/图生视频/2049742304176558082.json, 视频生成/图生视频/2049752785217966082.json, 视频生成/图生视频/1999143356380966913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_431

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2021226831017418753.json、视频生成/图生视频/2003700180081909761.json、视频生成/图生视频/2049742304176558082.json、视频生成/图生视频/2049752785217966082.json、视频生成/图生视频/1999143356380966913.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `InvertMask`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RepeatImageBatch`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `DF_Int_to_Float` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `IndexTTSRun` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `MultiLinePromptIndex` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SaveAudioMP3` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
