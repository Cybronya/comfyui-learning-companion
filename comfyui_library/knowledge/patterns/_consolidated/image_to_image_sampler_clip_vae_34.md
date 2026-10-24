---
name: image_to_image_sampler_clip_vae_34
type: Image To Image
frequency: 4
level: moderate
coverage: 0.74575
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), Image Rembg (Remove Background), ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext LORA训练对比工作流_1941711270368460801.json, 图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json, 图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json, 图片生成/文生图/Flux Kontext Dev 加速优化版服务端_1938625984528572418.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext LORA训练对比工作流_1941711270368460801.json、图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json、图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json、图片生成/文生图/Flux Kontext Dev 加速优化版服务端_1938625984528572418.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `Image Rembg (Remove Background)`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `Int` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `NunchakuFluxDiTLoader` —— 3/4 个有
- `NunchakuFluxLoraLoader` —— 3/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `ApplyFBCacheOnModel` —— 1/4 个有
- `CR SDXL Aspect Ratio` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `GoogleTranslateTextNode` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `NunchakuTextEncoderLoader` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 4 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，4 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
