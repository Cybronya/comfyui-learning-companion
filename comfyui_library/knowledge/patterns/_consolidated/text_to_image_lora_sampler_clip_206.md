---
name: text_to_image_lora_sampler_clip_206
type: Text To Image
frequency: 6
level: weak
coverage: 0.988833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image-t2v-gguf 千问量化模型文生图_2058416159862640641.json, 图片生成/文生图/qwen2512完美魔鬼身材的美女_2018950663933267969.json, 图片生成/文生图/qwenimg2512-文生图_2009674166802321409.json, 图片生成/文生图/qwen文生图动漫人物_2010134432182706177.json, "图片生成/文生图/全新VAE Z_image_turbo-VAE,加强细节，更高清_2003404331451912194.json", 图片生成/文生图/极品美女｜Krea2文生图 + 雯雯的后宫极品身材LoRA_2077759044986695682.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_206

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/qwen-image-t2v-gguf 千问量化模型文生图_2058416159862640641.json、图片生成/文生图/qwen2512完美魔鬼身材的美女_2018950663933267969.json、图片生成/文生图/qwenimg2512-文生图_2009674166802321409.json、图片生成/文生图/qwen文生图动漫人物_2010134432182706177.json、图片生成/文生图/全新VAE Z_image_turbo-VAE,加强细节，更高清_2003404331451912194.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `CompressImages` —— 2/6 个有
- `CFGNorm` —— 1/6 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 30 | 6 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 6 | 11% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 896 | 512 - 1536 | 6 | 60% |
| 高度 | 1248 | 512 - 1920 | 6 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 30，6 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，6 个样本，取值分散，一致性仅 11%
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 1536，6 个样本
- 高度 中位数 1248，观测区间 512 - 1920，6 个样本
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
