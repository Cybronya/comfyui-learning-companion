---
name: text_to_image_sampler_clip_unet_86
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9436
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1650 4G 文生图_Z-image量化 低显存_2061641168311640065.json, 图片生成/文生图/1961449815852957697.json, 图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json, 图片生成/文生图/fluxGGUF_官方工作流_文生图i2i_2007734572108222466.json, 图片生成/文生图/文生图工作流_2059966961978793986.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_86

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1650 4G 文生图_Z-image量化 低显存_2061641168311640065.json、图片生成/文生图/1961449815852957697.json、图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json、图片生成/文生图/fluxGGUF_官方工作流_文生图i2i_2007734572108222466.json、图片生成/文生图/文生图工作流_2059966961978793986.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `DualCLIPLoaderGGUF` —— 2/5 个有
- `FluxGuidance` —— 2/5 个有
- `CLIPLoaderGGUF` —— 1/5 个有
- `CLIPTextEncodeFlux` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 304 - 1960 | 5 | 39% |
| 高度 | 1024 | 304 - 1024 | 5 | 67% |
| 采样步数 | 20 | 8 - 26 | 5 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 42% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 304 - 1960，5 个样本，取值分散，一致性仅 39%
- 高度 中位数 1024，观测区间 304 - 1024，5 个样本
- 采样步数 中位数 20，观测区间 8 - 26，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
