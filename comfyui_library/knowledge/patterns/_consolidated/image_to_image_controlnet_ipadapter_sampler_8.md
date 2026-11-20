---
name: image_to_image_controlnet_ipadapter_sampler_8
type: Image To Image
frequency: 3
level: strong
coverage: 0.865
common_nodes: [AnyLineArtPreprocessor_aux, CLIPTextEncode, CR Latent Batch Size, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DF_Image_scale_to_side, DepthAnythingPreprocessor, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/产品精修工作流 一键出图细节文字保留_1910307647956971521.json, 图片生成/图生图/电商产品精修+放大 ｜一键生图系列_1907038704337346561.json, 平台全量/产品精修 效果好 万物皆可修_1910223093057683458.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/产品精修工作流 一键出图细节文字保留_1910307647956971521.json、图片生成/图生图/电商产品精修+放大 ｜一键生图系列_1907038704337346561.json、平台全量/产品精修 效果好 万物皆可修_1910223093057683458.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AnyLineArtPreprocessor_aux`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DF_Image_scale_to_side`
- `DepthAnythingPreprocessor`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
