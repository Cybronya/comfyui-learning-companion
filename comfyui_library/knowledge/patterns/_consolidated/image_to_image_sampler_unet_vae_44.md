---
name: image_to_image_sampler_unet_vae_44
type: Image To Image
frequency: 4
level: moderate
coverage: 0.97925
common_nodes: [DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux.1-图生图工作流_2087420374983200769.json, 图片生成/文生图/Flux基础文_图生图_2010971059218026497.json, 图片生成/文生图/自用美女_1963796521585299457.json, 数字人/数字人/jjll_1988794258486341634.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_44

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux.1-图生图工作流_2087420374983200769.json、图片生成/文生图/Flux基础文_图生图_2010971059218026497.json、图片生成/文生图/自用美女_1963796521585299457.json、数字人/数字人/jjll_1988794258486341634.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `CLIPTextEncodeFlux` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 8 | 4 | 15% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.9 | 0.5 - 1 | 4 | 75% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 8，4 个样本，取值分散，一致性仅 15%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.9，观测区间 0.5 - 1，4 个样本
