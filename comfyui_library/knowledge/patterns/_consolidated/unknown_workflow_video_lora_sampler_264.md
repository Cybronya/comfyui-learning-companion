---
name: unknown_workflow_video_lora_sampler_264
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.691375
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [SimpleMath+]
members: [视频生成/图生视频/2000388407983566850.json, 视频生成/图生视频/1986760720148852738.json, 视频生成/图生视频/2049742304176558082.json, 视频生成/图生视频/2049752785217966082.json, 视频生成/图生视频/1999143356380966913.json, 视频生成/文生视频/1998388912689176577.json, 视频生成/文生视频/SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_1998603247713681410.json, 视频生成/文生视频/网红制造WanVideoWrapper_I2V_SVI_长视频工作流_1988840595856691202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_264

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2000388407983566850.json、视频生成/图生视频/1986760720148852738.json、视频生成/图生视频/2049742304176558082.json、视频生成/图生视频/2049752785217966082.json、视频生成/图生视频/1999143356380966913.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RepeatImageBatch`
- `SetNode`
- `SimpleMath+`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 7/8 个有
- `WanVideoVACEStartToEndFrame` —— 7/8 个有
- `CLIPVisionLoader` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `WanVideoClipVisionEncode` —— 2/8 个有
- `WanVideoSetLoRAs` —— 2/8 个有
- `easy forLoopEnd` —— 2/8 个有
- `easy forLoopStart` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `CR Text Input Switch (4 way)` —— 1/8 个有
- `ColorMatch` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+
