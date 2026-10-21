---
name: text_to_image_upscale_lora_sampler_3
type: Text To Image
frequency: 14
level: weak
coverage: 0.903571
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageResizeKJv2, JoinStrings, KSampler, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SomethingToString, StringConstantMultiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103816033600622593.json, 图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103831107908227073.json, 图片生成/反推提示词/Z-image turbo三合一 文生图图生图加图片反推提示词_2104271484683374593.json, 图片生成/反推提示词/Z-image turbo出图三玩法 反推提示词文生图图生图全支持_2104310974978285570.json, 图片生成/反推提示词/Z-image turbo图片反推生图｜文生图图生图 反推提示词还原神图_2104066068133277698.json, 图片生成/反推提示词/Z-image turbo文生图图生图｜图片反推生图 反推提示词一键复刻_2104042748226654209.json, 图片生成/图生图/2007738512891715586.json, 图片生成/文生图/Z-image turbo 文生图 - 图生图-图片反推生图_2103816033600622593.json, 图片生成/文生图/Z-image turbo 文生图 - 图生图-图片反推生图_2103831107908227073.json, 图片生成/文生图/Z-image turbo 文生图 （图生图）_1995303972401557505.json, 图片生成/文生图/Z-image turbo三合一 文生图图生图加图片反推提示词_2104271484683374593.json, 图片生成/文生图/Z-image turbo出图三玩法 反推提示词文生图图生图全支持_2104310974978285570.json, 图片生成/文生图/Z-image turbo图片反推生图｜文生图图生图 反推提示词还原神图_2104066068133277698.json, 图片生成/文生图/Z-image turbo文生图图生图｜图片反推生图 反推提示词一键复刻_2104042748226654209.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103816033600622593.json、图片生成/反推提示词/Z-image turbo 文生图 - 图生图-图片反推生图_2103831107908227073.json、图片生成/反推提示词/Z-image turbo三合一 文生图图生图加图片反推提示词_2104271484683374593.json、图片生成/反推提示词/Z-image turbo出图三玩法 反推提示词文生图图生图全支持_2104310974978285570.json、图片生成/反推提示词/Z-image turbo图片反推生图｜文生图图生图 反推提示词还原神图_2104066068133277698.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SomethingToString`
- `StringConstantMultiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TurboWanVAELoader` —— 13/14 个有
- `JjkText` —— 8/14 个有
- `solarL_SaveImagesToZip` —— 8/14 个有
- `孤海注释` —— 8/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 14 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 14 | 42% |
| 采样算法 | er_sde | - | 14 | 57% |
| 调度器 | beta | - | 14 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 1024 | 14 | 4% |
| 高度 | 80 | 80 - 1536 | 14 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，14 个样本，一致性 57%
- 调度器 最常用 beta，14 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，14 个样本，取值分散，一致性仅 4%
- 高度 中位数 80，观测区间 80 - 1536，14 个样本，取值分散，一致性仅 0%
- 高发问题（22/14 个样本）：Steps较低可能导致细节不足
