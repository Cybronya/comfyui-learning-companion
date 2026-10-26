---
name: unknown_workflow_video_lora_sampler_416
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.710333
common_nodes: [GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 + SVI2：三镜头带货lyan_2021226831017418753.json, 视频生成/图生视频/Wan2.2 + SVI2：多镜头自动衔接与无限时长_2003700180081909761.json, 视频生成/图生视频/图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049742304176558082.json, 视频生成/图生视频/图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049752785217966082.json, 视频生成/文生视频/SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_1998603247713681410.json, 视频生成/文生视频/SVI-Wan22-1207超长视频生成工作流-课程同步工作流_1998388912689176577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_416

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 + SVI2：三镜头带货lyan_2021226831017418753.json、视频生成/图生视频/Wan2.2 + SVI2：多镜头自动衔接与无限时长_2003700180081909761.json、视频生成/图生视频/图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049742304176558082.json、视频生成/图生视频/图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049752785217966082.json、视频生成/文生视频/SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_1998603247713681410.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
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
- `GetImageRangeFromBatch` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `CR Text` —— 2/6 个有
- `DF_Int_to_Float` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `IndexTTSRun` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MultiLinePromptIndex` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SaveAudioMP3` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
