---
name: unknown_workflow_video_sampler_vae_103
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4654
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJ, LoadImage, SetNode, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoDiffusionForcingSampler, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoTeaCache, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1948680598048124929.json, 视频生成/图生视频/1915438645938163713.json, 视频生成/图生视频/1919284911071494146.json, 视频生成/图生视频/1914572430503833601.json, 视频生成/文生视频/1923575384724393985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_103

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1948680598048124929.json、视频生成/图生视频/1915438645938163713.json、视频生成/图生视频/1919284911071494146.json、视频生成/图生视频/1914572430503833601.json、视频生成/文生视频/1923575384724393985.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJ`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoDiffusionForcingSampler`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `CLIPTextEncode` —— 4/5 个有
- `WanVideoBlockSwap` —— 4/5 个有
- `WanVideoTextEmbedBridge` —— 4/5 个有
- `LoadWanVideoT5TextEncoder` —— 3/5 个有
- `WanVideoTextEncode` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `WanVideoVRAMManagement` —— 3/5 个有
- `LoadImageFromUrl` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
