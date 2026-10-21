---
name: unknown_workflow_video_sampler_vae_186
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7705
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, MaskBatchMulti, MaskPreview, PreviewImage, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1958478405673107458.json, 视频生成/图生视频/1933898213298757633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_186

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1958478405673107458.json、视频生成/图生视频/1933898213298757633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskBatchMulti`
- `MaskPreview`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
