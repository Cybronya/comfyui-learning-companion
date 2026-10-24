---
name: image_to_image_controlnet_ipadapter_sampler_5
type: Image To Image
frequency: 3
level: strong
coverage: 0.97
common_nodes: [CLIPSetLastLayer, CLIPTextEncodeWithWeight //Inspire, CR Latent Batch Size, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LineArtPreprocessor, LoadImage, SaveImage, VAEDecode, VAEEncode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键高清画质修复工作流_1899683142339350529.json, 图片生成/图生图/最新flux产品精修，可修复产品瑕疵、划痕_1950498036516573185.json, 图片生成/图生图/电商产品精修2.0_1965841857601277954.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键高清画质修复工作流_1899683142339350529.json、图片生成/图生图/最新flux产品精修，可修复产品瑕疵、划痕_1950498036516573185.json、图片生成/图生图/电商产品精修2.0_1965841857601277954.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncodeWithWeight //Inspire`
- `CR Latent Batch Size`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LineArtPreprocessor`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | dpmpp_sde | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
