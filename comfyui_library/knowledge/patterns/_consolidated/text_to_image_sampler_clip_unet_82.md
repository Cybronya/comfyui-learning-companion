---
name: text_to_image_sampler_clip_unet_82
type: Text To Image
frequency: 8
level: moderate
coverage: 0.991125
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2065251202434158594.json, 图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2091791668021387265.json, 图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069706999738232833.json, 图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069712042256322562.json, 图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2074652970565853186.json, 图片生成/文生图/文生图-Qwen3_2054442703181631489.json, 图片生成/文生图/文生图-krea2_2069932258559086593.json, 图片生成/文生图/文生图-人像生成写实风格_2091172485961175041.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2065251202434158594.json、图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2091791668021387265.json、图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069706999738232833.json、图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069712042256322562.json、图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2074652970565853186.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 7/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `ImageUpscaleWithModel` —— 2/8 个有
- `KOOK_ImageCompression` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `PreviewImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 8 | 61% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 8 | 49% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1080 | 768 - 1920 | 8 | 63% |
| 高度 | 1080 | 1024 - 1536 | 8 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，8 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，8 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 768 - 1920，8 个样本
- 高度 中位数 1080，观测区间 1024 - 1536，8 个样本，取值集中（一致性 86%）
