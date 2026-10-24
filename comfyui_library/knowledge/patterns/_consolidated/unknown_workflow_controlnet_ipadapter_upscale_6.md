---
name: unknown_workflow_controlnet_ipadapter_upscale_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.895
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, IPAdapterFaceID, IPAdapterUnifiedLoaderFaceID, Image Comparer (rgthree), ImageResize+, LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, UltimateSDUpscale, UpscaleModelLoader, easy a1111Loader, easy fullkSampler, easy globalSeed, easy pipeOut]
problems: []
missing: []
members: [图片生成/图生图/老照片修复-Old photo restoration_1893276148200062978.json, 图片生成/图生图/老照片修复放大（照片质感）_1915024136203137025.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/老照片修复-Old photo restoration_1893276148200062978.json、图片生成/图生图/老照片修复放大（照片质感）_1915024136203137025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `IPAdapterFaceID`
- `IPAdapterUnifiedLoaderFaceID`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `easy a1111Loader`
- `easy fullkSampler`
- `easy globalSeed`
- `easy pipeOut`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.95 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
