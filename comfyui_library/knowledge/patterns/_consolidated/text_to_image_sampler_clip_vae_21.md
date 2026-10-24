---
name: text_to_image_sampler_clip_vae_21
type: Text To Image
frequency: 7
level: strong
coverage: 0.791143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImpactSwitch, Int, KSampler, LoadImage, RH_Captioner, RH_Translator, RepeatLatentBatch, SaveImage, VAEDecode, VAELoader, easy imageSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea 提升高级质感｜图生图 _ 反推生图 __1951124219956539393.json, 图片生成/图生图/Flux Krea-Dev-图片反推-无AI逼真感--4K直出-自动提示词_1952211810726391810.json, 图片生成/图生图/Flux Krea-图片反推-自动提示词_1951862344861339650.json, 图片生成/图生图/Krea 图生图 _ 反推生图 _ 提升高级质感_1951122412194701313.json, 图片生成/文生图/Krea 文生图 _ 反推生图_1951091937367498754.json, 图片生成/文生图/Krea 极速版文生图 _ 反推生图_1951212723730325505.json, 图片生成/文生图/Krea-DEV 文生图 _ 反推生图_1956161644252549122.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux Krea 提升高级质感｜图生图 _ 反推生图 __1951124219956539393.json、图片生成/图生图/Flux Krea-Dev-图片反推-无AI逼真感--4K直出-自动提示词_1952211810726391810.json、图片生成/图生图/Flux Krea-图片反推-自动提示词_1951862344861339650.json、图片生成/图生图/Krea 图生图 _ 反推生图 _ 提升高级质感_1951122412194701313.json、图片生成/文生图/Krea 文生图 _ 反推生图_1951091937367498754.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoadImage`
- `RH_Captioner`
- `RH_Translator`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `easy ifElse` —— 6/7 个有
- `CR SDXL Aspect Ratio` —— 5/7 个有
- `CR Text Replace` —— 2/7 个有
- `DF_Integer` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `TextBox` —— 2/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有
- `NunchakuFluxLoraLoader` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
