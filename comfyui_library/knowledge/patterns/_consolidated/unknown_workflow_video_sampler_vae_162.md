---
name: unknown_workflow_video_sampler_vae_162
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.812333
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1930918811107524610.json, 视频生成/图生视频/1929529009221091330.json, 视频生成/图生视频/1933299852677947393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_162

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1930918811107524610.json、视频生成/图生视频/1929529009221091330.json、视频生成/图生视频/1933299852677947393.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImpactMakeImageBatch` —— 2/3 个有
- `ImpactMakeMaskBatch` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RIFE VFI` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
