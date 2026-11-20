---
name: unknown_workflow_controlnet_sampler_clip_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8445
common_nodes: [ApplyFluxControlNet, CLIPTextEncodeFlux, CannyEdgePreprocessor, DualCLIPLoader, EmptyLatentImage, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json, 图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json、图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux`
- `CannyEdgePreprocessor`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
