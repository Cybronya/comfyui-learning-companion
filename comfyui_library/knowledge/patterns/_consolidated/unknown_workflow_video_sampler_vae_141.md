---
name: unknown_workflow_video_sampler_vae_141
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.99075
common_nodes: [CreateCFGScheduleFloatList, INTConstant, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生视频——Wan2.2  SmoothMix_2041409089414107137.json, 视频生成/图生视频/图生视频——Wan2.2  SmoothMix_2042073160241123329.json, 视频生成/文生视频/Remix 1.0新模型文生视频_1977188003040907266.json, 视频生成/文生视频/wan2.2 FP8下 最低显内存使用_1953110455269134338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/图生视频——Wan2.2  SmoothMix_2041409089414107137.json、视频生成/图生视频/图生视频——Wan2.2  SmoothMix_2042073160241123329.json、视频生成/文生视频/Remix 1.0新模型文生视频_1977188003040907266.json、视频生成/文生视频/wan2.2 FP8下 最低显内存使用_1953110455269134338.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `WanVideoImageToVideoEncode` —— 3/4 个有
- `WanVideoSetRadialAttention` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Seed Generator` —— 1/4 个有
- `WanVideoApplyNAG` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoSetBlockSwap` —— 1/4 个有
- `WanVideoSetLoRAs` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
