---
name: image_to_image_sampler_clip_vae_37
type: Image To Image
frequency: 6
level: strong
coverage: 0.75
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext Presets官方预设模板发（懒人福音）_1944392404331843585.json, 图片生成/图生图/Kontext nunchaku单图编辑_1939898967906029569.json, 图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json, 图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json, 图片生成/文生图/Flux Kontext Dev 加速优化版服务端_1938625984528572418.json, 平台全量/Kontext Presets预设模板_LLM-API_1944251535570141186.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_37

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext Presets官方预设模板发（懒人福音）_1944392404331843585.json、图片生成/图生图/Kontext nunchaku单图编辑_1939898967906029569.json、图片生成/图生图/NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1938810664225792002.json、图片生成/图生图/脸部加强！NUCHAKU-Flux Kontext Dev 8步极速优化版服务端_1940326991549874177.json、图片生成/文生图/Flux Kontext Dev 加速优化版服务端_1938625984528572418.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 5/6 个有
- `DualCLIPLoader` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `ImageStitch` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `NunchakuFluxDiTLoader` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `Image Rembg (Remove Background)` —— 3/6 个有
- `Int` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `RepeatLatentBatch` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `easy seed` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `LoadKontextPresets` —— 2/6 个有
- `NunchakuFluxLoraLoader` —— 2/6 个有
- `ApplyFBCacheOnModel` —— 1/6 个有
- `CR String To Combo` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `NunchakuTextEncoderLoader` —— 1/6 个有
- `SDXLAspectRatioSelector` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 6 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
