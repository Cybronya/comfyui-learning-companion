---
name: unknown_workflow_video_lora_sampler_811
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6765
common_nodes: [CR Text, DF_Int_to_Float, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, InvertMask, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RepeatImageBatch, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2021226831017418753.json, 视频生成/图生视频/2003700180081909761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_811

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2021226831017418753.json、视频生成/图生视频/2003700180081909761.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DF_Int_to_Float`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `InvertMask`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
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
- `GetImageRangeFromBatch` —— 1/2 个有
- `IndexTTSRun` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MultiLinePromptIndex` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
