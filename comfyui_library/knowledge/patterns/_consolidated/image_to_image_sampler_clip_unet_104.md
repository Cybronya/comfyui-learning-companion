---
name: image_to_image_sampler_clip_unet_104
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9254
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/（洗图图生图效果很好）Z-Image_turbo图生图-又快又好_2101289951110459394.json, 图片生成/文生图/Anima Preview2图生图_2033542974574956546.json, 图片生成/文生图/Anima图生图_2021929700087566337.json, 视频生成/图生视频/【动漫】Anima Preview2图生图_2038098911314841602.json, 视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_104

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/（洗图图生图效果很好）Z-Image_turbo图生图-又快又好_2101289951110459394.json、图片生成/文生图/Anima Preview2图生图_2033542974574956546.json、图片生成/文生图/Anima图生图_2021929700087566337.json、视频生成/图生视频/【动漫】Anima Preview2图生图_2038098911314841602.json、视频生成/文生视频/Anima-2.9B｜智能图生图_Qwen3VL反推_2089343535781859329.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 4/5 个有
- `image_scale_pixel_v2` —— 4/5 个有
- `Qwen3VLProcessor` —— 2/5 个有
- `WD14Tagger|pysssss` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `RepeatLatentBatch` —— 1/5 个有
- `VAELoaderKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 31 | 8 - 40 | 5 | 60% |
| Prompt 约束强度(CFG) | 4 | 1 - 5 | 5 | 60% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 5 | 40% |
| 调度器 | simple | - | 5 | 40% |
| 重绘幅度 | 0.7 | 0.5 - 0.75 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 31，观测区间 8 - 40，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 5，5 个样本
- 采样算法 最常用 dpmpp_2m_sde_gpu，5 个样本，一致性 40%
- 调度器 最常用 simple，5 个样本，一致性 40%
- 重绘幅度 中位数 0.7，观测区间 0.5 - 0.75，5 个样本，取值集中（一致性 86%）
