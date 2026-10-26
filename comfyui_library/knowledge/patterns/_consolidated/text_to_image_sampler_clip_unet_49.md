---
name: text_to_image_sampler_clip_unet_49
type: Text To Image
frequency: 12
level: weak
coverage: 0.93175
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ovis-Image 海报设计工作流_1997462628240932866.json, 图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json, 图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json, 图片生成/文生图/Z-image 超清快速文生图_2010897242143592450.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2066049562531418114.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2075535526135947265.json, 图片生成/文生图/Z-image-turbo-bf16-文生图_2078810535986032641.json, 图片生成/文生图/Z-image_1995048903902998530.json, 图片生成/文生图/文生图_2070723264158191617.json, 图片生成/文生图/百度ERNIE-image-turbo-文生图_2044322834406707202.json, 图片生成/文生图/百度ERNIE-image-turbo-文生图_2044665456572764161.json, 图片生成/文生图/🦖可正可邪-Z-IMAGE_1993956349084188673.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Ovis-Image 海报设计工作流_1997462628240932866.json、图片生成/文生图/Qwen-2.1 文生图_2104918958309732354.json、图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json、图片生成/文生图/Z-image 超清快速文生图_2010897242143592450.json、图片生成/文生图/Z-image-turbo-bf16-文生图_2066049562531418114.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/12 个有
- `Int` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `Label (rgthree)` —— 5/12 个有
- `AnyAspectRatio` —— 1/12 个有
- `ModelSamplingFlux` —— 1/12 个有
- `QwenImage21Cache` —— 1/12 个有
- `UnetLoaderGGUF` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 50 | 12 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 12 | 17% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1052 | 720 - 2416 | 12 | 60% |
| 高度 | 1408 | 576 - 1920 | 12 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 50，12 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，12 个样本，取值分散，一致性仅 17%
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 720 - 2416，12 个样本
- 高度 中位数 1408，观测区间 576 - 1920，12 个样本
