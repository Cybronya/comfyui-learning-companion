---
name: unknown_workflow_video_lora_sampler_339
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.890167
common_nodes: [INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/1956565680000782337.json, 视频生成/图生视频/2035336872209162242.json, 视频生成/图生视频/1964201625864818690.json, 视频生成/图生视频/1964640487892242434.json, 视频生成/图生视频/1963945783164850177.json, 视频生成/图生视频/1992952460717342721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_339

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1956565680000782337.json、视频生成/图生视频/2035336872209162242.json、视频生成/图生视频/1964201625864818690.json、视频生成/图生视频/1964640487892242434.json、视频生成/图生视频/1963945783164850177.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `WanVideoSLG` —— 4/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `easy positive` —— 3/6 个有
- `GetNode` —— 2/6 个有
- `ImageStitch` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `WanVideoEmptyEmbeds` —— 1/6 个有
- `WanVideoLoraSelectMulti` —— 1/6 个有
- `easy humanSegmentation` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
