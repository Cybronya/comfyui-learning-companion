---
name: unknown_workflow_controlnet_sampler_clip_23
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86325
common_nodes: [AIO_Preprocessor, ApplyFluxControlNet, CLIPTextEncodeFlux, EmptyLatentImage, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/文生图/FLUX ControlNet Easy Workflow_1836364118327717889.json, 图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json, 平台全量/FLUX controlnet (depth V3) CN工作流_1825726695277268994.json, 平台全量/Flux ControlNet Depth - Beginner Friendly_1881274373649702914.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX ControlNet Easy Workflow_1836364118327717889.json、图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json、平台全量/FLUX controlnet (depth V3) CN工作流_1825726695277268994.json、平台全量/Flux ControlNet Depth - Beginner Friendly_1881274373649702914.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux`
- `EmptyLatentImage`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `ImageResize+` —— 2/4 个有
- `ModelSamplingFlux` —— 2/4 个有
- `UnetLoaderGGUF` —— 2/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `DualCLIPLoaderGGUF` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 4 | 65% |
| 高度 | 640 | 512 - 1024 | 4 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，4 个样本
- 高度 中位数 640，观测区间 512 - 1024，4 个样本
