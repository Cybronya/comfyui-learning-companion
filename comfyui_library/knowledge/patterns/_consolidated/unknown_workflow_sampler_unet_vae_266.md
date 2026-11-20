---
name: unknown_workflow_sampler_unet_vae_266
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.992
common_nodes: [BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/双 redux 随意搭配_1890040180156379137.json, 平台全量/Flux Redux 多图融合_1860596179414249473.json, 平台全量/Flux Redux 风格迁移+场景融合_1888068894102585346.json, 平台全量/Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777.json, 平台全量/Redux图像混合_在线生图_1893690109743529985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_266

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/双 redux 随意搭配_1890040180156379137.json、平台全量/Flux Redux 多图融合_1860596179414249473.json、平台全量/Flux Redux 风格迁移+场景融合_1888068894102585346.json、平台全量/Multi Flux Redux - Mix 2 image by flux redux_1861984687953739777.json、平台全量/Redux图像混合_在线生图_1893690109743529985.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LayerMask: BiRefNetUltraV2` —— 1/5 个有
- `LayerMask: LoadBiRefNetModel` —— 1/5 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1152 | 5 | 86% |
| 高度 | 1024 | 896 - 1536 | 5 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1152，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 896 - 1536，5 个样本
