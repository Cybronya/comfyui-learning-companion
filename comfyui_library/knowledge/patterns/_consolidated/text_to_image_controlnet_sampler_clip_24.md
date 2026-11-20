---
name: text_to_image_controlnet_sampler_clip_24
type: Text To Image
frequency: 3
level: moderate
coverage: 0.919
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea大图_1965227597036666882.json, 平台全量/kontext+union pro2姿态迁移_1963239965620678658.json, 数字人/数字人/Flux UnionPro2姿势迁移_1960599807897329666.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/krea大图_1965227597036666882.json、平台全量/kontext+union pro2姿态迁移_1963239965620678658.json、数字人/数字人/Flux UnionPro2姿势迁移_1960599807897329666.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| ControlNet 权重 | 2 | 0.6 - 2 | 3 | 57% |
| 宽度 | 512 | 512 - 1280 | 3 | 53% |
| 高度 | 512 | 512 - 1280 | 3 | 53% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.7 - 1 | 3 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 2，观测区间 0.6 - 2，3 个样本
- 宽度 中位数 512，观测区间 512 - 1280，3 个样本
- 高度 中位数 512，观测区间 512 - 1280，3 个样本
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，3 个样本，取值集中（一致性 84%）
