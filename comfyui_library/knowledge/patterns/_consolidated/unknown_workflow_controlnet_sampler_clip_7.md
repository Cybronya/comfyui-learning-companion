---
name: unknown_workflow_controlnet_sampler_clip_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9135
common_nodes: [AIO_Preprocessor, ApplyFluxControlNet, CLIPTextEncodeFlux, EmptyLatentImage, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/文生图/FLUX ControlNet Easy Workflow_1836364118327717889.json, 图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX ControlNet Easy Workflow_1836364118327717889.json、图片生成/文生图/FLUX controlnet (canny V3) CN工作流_1825464189249826818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux`
- `EmptyLatentImage`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 640 | - | 2 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 640，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
