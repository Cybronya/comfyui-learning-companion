---
name: text_to_image_sampler_clip_vae_10
type: Text To Image
frequency: 12
level: moderate
coverage: 0.983333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image-t2v-gguf 千问量化模型文生图_2058416159862640641.json, 图片生成/文生图/qwen-image（0.1）_2038526752217112577.json, 图片生成/文生图/qwen-image（0.1）_2038784092753367042.json, 图片生成/文生图/qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226.json, 图片生成/文生图/qwen-image（0.1）漫剧道具_2042856409104130050.json, 图片生成/文生图/qwen-image（0.1）真人_2042783785372094466.json, 图片生成/文生图/qwen-image（0.2）_2038498159269253121.json, 图片生成/文生图/qwen-image（0.2）_2038786485712850946.json, 图片生成/文生图/qwen文生图动漫人物_2010134432182706177.json, 图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json, 图片生成/文生图/z-image文生图 基础版 lora模型加载_2001116171342577665.json, 图片生成/文生图/造相 Z-image 文生图 Ultra_2073291168456200194.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/qwen-image-t2v-gguf 千问量化模型文生图_2058416159862640641.json、图片生成/文生图/qwen-image（0.1）_2038526752217112577.json、图片生成/文生图/qwen-image（0.1）_2038784092753367042.json、图片生成/文生图/qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226.json、图片生成/文生图/qwen-image（0.1）漫剧道具_2042856409104130050.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 11/12 个有
- `LoraLoaderModelOnly` —— 7/12 个有
- `ConditioningZeroOut` —— 4/12 个有
- `LatentUpscaleBy` —— 2/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `ImageSharpen` —— 1/12 个有
- `ImageUpscaleWithModel` —— 1/12 个有
- `ModelSamplingAuraFlow` —— 1/12 个有
- `UnetLoaderGGUF` —— 1/12 个有
- `Upscale Model Loader` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 12 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 12 | 12% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1080 | 512 - 1920 | 12 | 71% |
| 高度 | 1920 | 512 - 1920 | 12 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，12 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，12 个样本
- 高度 中位数 1920，观测区间 512 - 1920，12 个样本
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
