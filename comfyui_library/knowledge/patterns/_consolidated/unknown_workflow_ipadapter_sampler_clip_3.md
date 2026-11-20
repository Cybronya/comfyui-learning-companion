---
name: unknown_workflow_ipadapter_sampler_clip_3
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8465
common_nodes: [ApplyFluxIPAdapter, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, ImageScale, LoadFluxIPAdapter, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [平台全量/FLUX STYLE TRANSFER (better version)_1869661957786603522.json, 平台全量/FLUX ip adapter_1879423567862657025.json, 平台全量/Flux ipadapter + CN(depth canny hed)_1836384659478573058.json, 平台全量/flux-ip-adapter-v2_1851291720024551425.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FLUX STYLE TRANSFER (better version)_1869661957786603522.json、平台全量/FLUX ip adapter_1879423567862657025.json、平台全量/Flux ipadapter + CN(depth canny hed)_1836384659478573058.json、平台全量/flux-ip-adapter-v2_1851291720024551425.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyFluxIPAdapter`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImageScale`
- `LoadFluxIPAdapter`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ApplyFluxControlNet` —— 2/4 个有
- `CannyEdgePreprocessor` —— 2/4 个有
- `DepthAnythingPreprocessor` —— 2/4 个有
- `HEDPreprocessor` —— 2/4 个有
- `LoadFluxControlNet` —— 2/4 个有
- `ImageCrop` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
