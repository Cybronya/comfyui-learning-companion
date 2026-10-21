---
name: text_to_image_sampler_clip_unet_73
type: Text To Image
frequency: 7
level: moderate
coverage: 0.991143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2-双采+放大_2077598774695907329.json, 图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2065251202434158594.json, 图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069706999738232833.json, 图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069712042256322562.json, 图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2074652970565853186.json, 图片生成/文生图/文生图超快生成_2101274758447980545.json, 图片生成/文生图/文生图（生成高清手机壁纸）_2064532712718950402.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/krea2-双采+放大_2077598774695907329.json、图片生成/文生图/文生图 Qwen2512  领军模型 完美中文_2065251202434158594.json、图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069706999738232833.json、图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2069712042256322562.json、图片生成/文生图/文生图+Qwen2512++领军模型+完美中文_2074652970565853186.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `VAEEncode` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 25 | 7 | 62% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 7 | 57% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1200 | 1024 - 1920 | 7 | 72% |
| 高度 | 1080 | 1080 - 2640 | 7 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1200，观测区间 1024 - 1920，7 个样本
- 高度 中位数 1080，观测区间 1080 - 2640，7 个样本
