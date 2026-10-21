---
name: text_to_image_sampler_clip_unet_146
type: Text To Image
frequency: 3
level: moderate
coverage: 0.966667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/🦖可正可邪-Z-IMAGE_1993956349084188673.json, 视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json, 视频生成/文生视频/高清超真实Z-image文生图_1999125125809176577.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/🦖可正可邪-Z-IMAGE_1993956349084188673.json、视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json、视频生成/文生视频/高清超真实Z-image文生图_1999125125809176577.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `AnyAspectRatio` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 35 | 3 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1024 - 1184 | 3 | 94% |
| 高度 | 1536 | 1024 - 1920 | 3 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 35，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1184，3 个样本，取值集中（一致性 94%）
- 高度 中位数 1536，观测区间 1024 - 1920，3 个样本
