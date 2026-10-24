---
name: text_to_image_upscale_sampler_clip_6
type: Text To Image
frequency: 16
level: weak
coverage: 0.897125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103816033600622593.json, 图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103831107908227073.json, 图片生成/反推提示词/Z-image turbo三合一 文生图图生图加图片反推提示词_2104271484683374593.json, 图片生成/反推提示词/Z-image turbo出图三玩法 反推提示词文生图图生图全支持_2104310974978285570.json, 图片生成/反推提示词/Z-image turbo图片反推生图｜文生图图生图 反推提示词还原神图_2104066068133277698.json, 图片生成/反推提示词/Z-image turbo文生图图生图｜图片反推生图 反推提示词一键复刻_2104042748226654209.json, 图片生成/图生图/Z image超真实高清洗图无AI感 照片级质感图片优化_2105031763482472449.json, 图片生成/图生图/Z-image turbo 图片反推生图 -文生图 - 图生图_2079541950725844994.json, 图片生成/图生图/Z-image turbo 文生图 - 图生图-图片反推生图_2007738512891715586.json, 图片生成/图生图/Z-image-turbo基础图生图+高清放大_2063183525263798273.json, 图片生成/图生图/Z-image_turbo_文生图_-_图生图-图片反推生图_2108387804148494338.json, 图片生成/图生图/Z-image_turbo_文生图_-_图生图-图片反推生图_2110182398058131457.json, 图片生成/图生图/Z-image_turbo图片反推生图，文生图图生图两相宜_2110871171519574017.json, 图片生成/图生图/超清质感修复｜klein高清放大写实图生图_2093740247157919745.json, 图片生成/文生图/Z-image turbo 图片反推生图 -文生图 - 图生图_2055905347117821953.json, 图片生成/文生图/Z-image turbo 文生图 （图生图）_1995303972401557505.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103816033600622593.json、图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103831107908227073.json、图片生成/反推提示词/Z-image turbo三合一 文生图图生图加图片反推提示词_2104271484683374593.json、图片生成/反推提示词/Z-image turbo出图三玩法 反推提示词文生图图生图全支持_2104310974978285570.json、图片生成/反推提示词/Z-image turbo图片反推生图｜文生图图生图 反推提示词还原神图_2104066068133277698.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/16 个有
- `Image Comparer (rgthree)` —— 15/16 个有
- `ImageResizeKJv2` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `ShowText|pysssss` —— 15/16 个有
- `VAEEncode` —— 15/16 个有
- `JoinStrings` —— 14/16 个有
- `Qwen3_VQA` —— 14/16 个有
- `SomethingToString` —— 14/16 个有
- `StringConstantMultiline` —— 13/16 个有
- `TurboWanVAELoader` —— 12/16 个有
- `JjkText` —— 7/16 个有
- `solarL_SaveImagesToZip` —— 7/16 个有
- `孤海注释` —— 7/16 个有
- `AILab_QwenVL` —— 1/16 个有
- `CR Text` —— 1/16 个有
- `KSamplerAdvanced` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `ReferenceLatent` —— 1/16 个有
- `SetNode` —— 1/16 个有
- `easy imageColorMatch` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 16 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 16 | 31% |
| 采样算法 | euler | - | 16 | 56% |
| 调度器 | simple | - | 16 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 872 | 80 - 1024 | 16 | 23% |
| 高度 | 1408 | 80 - 1536 | 16 | 20% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，16 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，16 个样本，一致性 56%
- 调度器 最常用 simple，16 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 872，观测区间 80 - 1024，16 个样本，取值分散，一致性仅 23%
- 高度 中位数 1408，观测区间 80 - 1536，16 个样本，取值分散，一致性仅 20%
- 高发问题（21/16 个样本）：Steps较低可能导致细节不足
