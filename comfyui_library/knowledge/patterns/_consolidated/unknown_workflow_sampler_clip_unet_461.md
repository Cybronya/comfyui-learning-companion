---
name: unknown_workflow_sampler_clip_unet_461
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.814
common_nodes: [CLIPTextEncodeFlux, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, StyleModelApplyAdvanced, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Flux - Finally consistent style transfer!_1861972528293150722.json, 平台全量/Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506.json, 平台全量/Style Transfer Canny Controlnet for Room Design!_1889135446880935938.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_461

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Flux - Finally consistent style transfer!_1861972528293150722.json、平台全量/Flux - Style Transfer + ControlNet + FaceSwap!_1861949689242517506.json、平台全量/Style Transfer Canny Controlnet for Room Design!_1889135446880935938.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApplyAdvanced`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `ControlNetApplySD3` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `DF_Get_image_size` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `ReActorFaceSwap` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
