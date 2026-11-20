---
name: unknown_workflow_controlnet_sampler_clip_29
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.852
common_nodes: [ApplyFluxControlNet, CLIPTextEncodeFlux, CannyEdgePreprocessor, DualCLIPLoader, EmptyLatentImage, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json, 图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json, 平台全量/Flux (ControlNet) Canny - V3_1890288463416270850.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux-controlnet-canny-v3-workflow_1832556051337228290.json、图片生成/图生图/【遇见AI】FLUX模型XLabs版ControlNet_2041074656567894018.json、平台全量/Flux (ControlNet) Canny - V3_1890288463416270850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
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
- `UNETLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GetImageSize+` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
