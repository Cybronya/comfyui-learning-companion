---
name: text_to_image_sampler_clip_unet_79
type: Text To Image
frequency: 9
level: weak
coverage: 0.911889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ovis-Image 海报设计工作流_1997462628240932866.json, 图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2066049562531418114.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2075535526135947265.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2078810535986032641.json, 图片生成/文生图/Z-image_1995048903902998530.json, 图片生成/文生图/api-z-image_1995157591246430209.json, 图片生成/文生图/boogu 文生图工作流_2072977078944886785.json, 图片生成/文生图/文生图_2070723264158191617.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Ovis-Image 海报设计工作流_1997462628240932866.json、图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json、图片生成/文生图/Z-image-turbo-bf16-文生图_2066049562531418114.json、图片生成/文生图/Z-image-turbo-bf16-文生图_2075535526135947265.json、图片生成/文生图/Z-image-turbo-bf16-文生图_2078810535986032641.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/9 个有
- `Int` —— 7/9 个有
- `Label (rgthree)` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `ModelSamplingFlux` —— 1/9 个有
- `QwenImage21Cache` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `UnetLoaderGGUF` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 9 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 9 | 13% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1080 | 512 - 2416 | 9 | 52% |
| 高度 | 1536 | 512 - 1920 | 9 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，9 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，9 个样本，取值分散，一致性仅 13%
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 2416，9 个样本
- 高度 中位数 1536，观测区间 512 - 1920，9 个样本
