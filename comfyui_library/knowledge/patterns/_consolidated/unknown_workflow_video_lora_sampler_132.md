---
name: unknown_workflow_video_lora_sampler_132
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.845917
common_nodes: [INTConstant, LoadImage, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [SimpleMath+]
members: [图片生成/文生图/1956565680000782337.json, 视频生成/图生视频/2035336872209162242.json, 视频生成/图生视频/1952003952139292673.json, 视频生成/图生视频/2061786208002465793.json, 视频生成/图生视频/2061806465001803778.json, 视频生成/图生视频/1950495596585144322.json, 视频生成/图生视频/1952283809247080449.json, 视频生成/图生视频/1981341961615474690.json, 视频生成/图生视频/2000388407983566850.json, 视频生成/图生视频/1986760720148852738.json, 视频生成/文生视频/1998388912689176577.json, 视频生成/文生视频/SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_1998603247713681410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_132

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/1956565680000782337.json、视频生成/图生视频/2035336872209162242.json、视频生成/图生视频/1952003952139292673.json、视频生成/图生视频/2061786208002465793.json、视频生成/图生视频/2061806465001803778.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 11/12 个有
- `GetImageSizeAndCount` —— 10/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `WanVideoSetLoRAs` —— 9/12 个有
- `CreateCFGScheduleFloatList` —— 6/12 个有
- `GetNode` —— 6/12 个有
- `SetNode` —— 6/12 个有
- `SimpleMath+` —— 6/12 个有
- `GetImageRangeFromBatch` —— 5/12 个有
- `ImageBatchMulti` —— 5/12 个有
- `RepeatImageBatch` —— 5/12 个有
- `InvertMask` —— 4/12 个有
- `WanVideoVACEStartToEndFrame` —— 4/12 个有
- `CLIPVisionLoader` —— 2/12 个有
- `ColorMatch` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `WanVideoClipVisionEncode` —— 2/12 个有
- `PreviewImage` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `WanVideoEmptyEmbeds` —— 1/12 个有
- `WanVideoLoraSelectMulti` —— 1/12 个有
- `WanVideoSLG` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+
