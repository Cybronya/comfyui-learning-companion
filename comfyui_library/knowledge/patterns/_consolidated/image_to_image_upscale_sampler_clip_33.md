---
name: image_to_image_upscale_sampler_clip_33
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9032
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/2D转2.5D转3D_1777955473434152961.json, 平台全量/图生图+高清修复_1818199309555793922.json, 平台全量/图生图+高清修复_2013595113817120770.json, 平台全量/提示词反推（WD14)-图片生成放大_1833031846396395521.json, 平台全量/风格转换（揉图)_1777956717909315585.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/2D转2.5D转3D_1777955473434152961.json、平台全量/图生图+高清修复_1818199309555793922.json、平台全量/图生图+高清修复_2013595113817120770.json、平台全量/提示词反推（WD14)-图片生成放大_1833031846396395521.json、平台全量/风格转换（揉图)_1777956717909315585.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `RepeatLatentBatch` —— 4/5 个有
- `ImageResize+` —— 2/5 个有
- `WD14Tagger|pysssss` —— 2/5 个有
- `ConditionText` —— 1/5 个有
- `IPAdapter` —— 1/5 个有
- `IPAdapterUnifiedLoader` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text to Conditioning` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | euler_ancestral | - | 5 | 60% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 0.45 | 0.25 - 1 | 5 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，5 个样本，一致性 60%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 0.45，观测区间 0.25 - 1，5 个样本
