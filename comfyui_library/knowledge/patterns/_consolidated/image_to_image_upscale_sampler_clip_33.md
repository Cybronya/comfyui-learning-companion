---
name: image_to_image_upscale_sampler_clip_33
type: Image To Image
frequency: 3
level: moderate
coverage: 0.920333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageUpscaleWithModel, KSampler, LoadImage, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/一张图的百变风格_1805176859603755010.json, 图片生成/图生图/图生图+高清修复_1865926491224621057.json, 图片生成/图生图/图生图+高清修复_2030924373321846786.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一张图的百变风格_1805176859603755010.json、图片生成/图生图/图生图+高清修复_1865926491224621057.json、图片生成/图生图/图生图+高清修复_2030924373321846786.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `RepeatLatentBatch` —— 2/3 个有
- `CannyEdgePreprocessor` —— 1/3 个有
- `ControlNetApply` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `SDXLPromptStyler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 3 | 87% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.45 | 0.15 - 0.8 | 3 | 43% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，3 个样本，取值集中（一致性 87%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.45，观测区间 0.15 - 0.8，3 个样本，取值分散，一致性仅 43%
