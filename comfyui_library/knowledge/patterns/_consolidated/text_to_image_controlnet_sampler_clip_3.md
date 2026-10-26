---
name: text_to_image_controlnet_sampler_clip_3
type: Text To Image
frequency: 9
level: moderate
coverage: 0.881778
common_nodes: [CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX CONTROLNET重绘洗图_1906693392619778050.json, 图片生成/图生图/FLUX CONTROLNET重绘洗图，避免版权问题_1911721428226404354.json, 图片生成/图生图/FLUX Krea 洗图 ControlNet  Union_1956165297998843906.json, 图片生成/图生图/FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953.json, 图片生成/图生图/图片-洗图重绘  Flux CN 加速_1979481164350132225.json, 图片生成/图生图/洗图重绘  Flux CN 加速_1964712702805463042.json, 图片生成/图生图/洗图重绘  Flux CN 加速_1981258074071752705.json, 图片生成/图生图/洗图重绘Flux超分加噪声_1981260742190161921.json, 图片生成/文生图/flux文生图控制_1915206472983318529.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX CONTROLNET重绘洗图_1906693392619778050.json、图片生成/图生图/FLUX CONTROLNET重绘洗图，避免版权问题_1911721428226404354.json、图片生成/图生图/FLUX Krea 洗图 ControlNet  Union_1956165297998843906.json、图片生成/图生图/FLUX Krea 重绘洗图 ControlNet  Union_1951500495967997953.json、图片生成/图生图/图片-洗图重绘  Flux CN 加速_1979481164350132225.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 8/9 个有
- `Joy_caption_two_load` —— 8/9 个有
- `easy imageSize` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `PreviewImage` —— 6/9 个有
- `Anything Everywhere3` —— 5/9 个有
- `ConditioningZeroOut` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `RH_Translator` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `JjkShowText` —— 4/9 个有
- `LayerUtility: PurgeVRAM` —— 4/9 个有
- `SDVN Translate` —— 3/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `ArgosTranslateTextNode` —— 1/9 个有
- `DifferentialDiffusion` —— 1/9 个有
- `VAEEncode` —— 1/9 个有
- `ttN concat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 9 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 0.8 | 0.3 - 0.8 | 9 | 63% |
| 宽度 | 512 | 512 - 720 | 9 | 88% |
| 高度 | 512 | 512 - 1280 | 9 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，9 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.3 - 0.8，9 个样本
- 宽度 中位数 512，观测区间 512 - 720，9 个样本，取值集中（一致性 88%）
- 高度 中位数 512，观测区间 512 - 1280，9 个样本
