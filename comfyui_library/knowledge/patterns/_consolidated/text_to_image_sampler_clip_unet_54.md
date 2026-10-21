---
name: text_to_image_sampler_clip_unet_54
type: Text To Image
frequency: 8
level: weak
coverage: 0.86525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json, 图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json, 图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json, 图片生成/文生图/Anima-turbo-v1.0 文生图_2092898755967279105.json, 图片生成/文生图/Anima_V10-Turbo 10-Step｜10步极速文生图_2079037824149573634.json, 图片生成/文生图/Krea2 漫剧角色资产一键生成工作流｜文生四视图_2099740461484302337.json, 图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json, 图片生成/文生图/绝区零风格文生图场景设计_2100441031195062274.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json、图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json、图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json、图片生成/文生图/Anima-turbo-v1.0 文生图_2092898755967279105.json、图片生成/文生图/Anima_V10-Turbo 10-Step｜10步极速文生图_2079037824149573634.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `CompressImages` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `PDRatioSelector` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有
- `XB_UNetNameBroadcaster` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 8 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 26% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1152 | 512 - 2000 | 8 | 67% |
| 高度 | 984 | 248 - 1536 | 8 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，8 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，观测区间 512 - 2000，8 个样本
- 高度 中位数 984，观测区间 248 - 1536，8 个样本
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
