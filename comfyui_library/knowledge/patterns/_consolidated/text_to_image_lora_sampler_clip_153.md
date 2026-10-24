---
name: text_to_image_lora_sampler_clip_153
type: Text To Image
frequency: 10
level: strong
coverage: 0.9231
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Flux2Scheduler, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2Klein 4B加速版多图编辑 高效换头换脸_2098106416744722433.json, 图片生成/图生图/Flux2Klein多图编辑4B加速｜写实换头换脸图生图_2090541141182734337.json, 图片生成/图生图/Flux2Klein换内衣｜图生图服装替换_2089687838047694850.json, 图片生成/图生图/Klein 9B商业级光影融合工作流零偏移处理_2100306858379669505.json, 图片生成/图生图/KleinFace换头换脸Flux2 Klein 9B模型高清人物AI智能面部替换，图生图_2106910609794232322.json, 图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2108373965847744513.json, 图片生成/图生图/KleinFace换头换脸Flux2_Klein_9B模型高清人物AI智能面部替换，图生图_2112837974730829825.json, 图片生成/图生图/KleinFace高清换头换脸｜Flux2-Klein-9B面部替换_2106642679978356738.json, 图片生成/图生图/多图编辑换头｜Flux2Klein写实换脸4B加速版_2090845255133392898.json, 图片生成/图生图/皮带纹路质感优化 lora增强光感清晰度与细节_2098300203974619138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux2Klein 4B加速版多图编辑 高效换头换脸_2098106416744722433.json、图片生成/图生图/Flux2Klein多图编辑4B加速｜写实换头换脸图生图_2090541141182734337.json、图片生成/图生图/Flux2Klein换内衣｜图生图服装替换_2089687838047694850.json、图片生成/图生图/Klein 9B商业级光影融合工作流零偏移处理_2100306858379669505.json、图片生成/图生图/KleinFace换头换脸Flux2 Klein 9B模型高清人物AI智能面部替换，图生图_2106910609794232322.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 8/10 个有
- `EmptyFlux2LatentImage` —— 7/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `CR Text` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `FluxKontextImageScale` —— 4/10 个有
- `GetImageSize` —— 4/10 个有
- `ImageConcanate` —— 4/10 个有
- `JWFloat` —— 4/10 个有
- `YC Color Match` —— 4/10 个有
- `ImageSmartSharpen+` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `easy int` —— 2/10 个有
- `CR Text Input Switch (4 way)` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `ShowText` —— 1/10 个有
- `Text` —— 1/10 个有
- `TextCombinerTwo` —— 1/10 个有
- `easy imageColorMatch` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
