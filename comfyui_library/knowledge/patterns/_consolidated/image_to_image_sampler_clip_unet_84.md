---
name: image_to_image_sampler_clip_unet_84
type: Image To Image
frequency: 5
level: strong
coverage: 0.8578
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3d角色ip三视图（白底背景）_1954720030204293122.json, 图片生成/图生图/CG迷-Kontext dev多图融合标准工作流_1938582981999316993.json, 图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json, 图片生成/图生图/Flux Kontext Dev_1938415127047897089.json, 图片生成/图生图/Kontext  lora换装+多图融合工作流_1959167012272549890.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/3d角色ip三视图（白底背景）_1954720030204293122.json、图片生成/图生图/CG迷-Kontext dev多图融合标准工作流_1938582981999316993.json、图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json、图片生成/图生图/Flux Kontext Dev_1938415127047897089.json、图片生成/图生图/Kontext  lora换装+多图融合工作流_1959167012272549890.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ModelSamplingFlux` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Int` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 5 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
