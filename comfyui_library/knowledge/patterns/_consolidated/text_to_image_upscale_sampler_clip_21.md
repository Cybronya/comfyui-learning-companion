---
name: text_to_image_upscale_sampler_clip_21
type: Text To Image
frequency: 3
level: moderate
coverage: 0.877
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1960144611694030850.json, 图片生成/文生图/1969985825045946369.json, 图片生成/文生图/1975059549734481921.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1960144611694030850.json、图片生成/文生图/1969985825045946369.json、图片生成/文生图/1975059549734481921.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 832 | 3 | 96% |
| 高度 | 1024 | 1024 - 1280 | 3 | 89% |
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.3 | 0.25 - 0.4 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 832，3 个样本，取值集中（一致性 96%）
- 高度 中位数 1024，观测区间 1024 - 1280，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.3，观测区间 0.25 - 0.4，3 个样本，取值集中（一致性 80%）
