---
name: image_to_image_sampler_clip_unet_93
type: Image To Image
frequency: 6
level: strong
coverage: 0.874333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/3d角色ip三视图（白底背景）_1954720030204293122.json, 图片生成/图生图/CG迷-Kontext dev多图融合标准工作流_1938582981999316993.json, 图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json, 图片生成/图生图/Flux Kontext Dev_1938415127047897089.json, 图片生成/图生图/Kontext  lora换装+多图融合工作流_1959167012272549890.json, 平台全量/iP形象_三视图（白底背景）_1954110098857705474.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_93

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/3d角色ip三视图（白底背景）_1954720030204293122.json、图片生成/图生图/CG迷-Kontext dev多图融合标准工作流_1938582981999316993.json、图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json、图片生成/图生图/Flux Kontext Dev_1938415127047897089.json、图片生成/图生图/Kontext  lora换装+多图融合工作流_1959167012272549890.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageStitch` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ModelSamplingFlux` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `ConstrainImage|pysssss` —— 2/6 个有
- `Int` —— 2/6 个有
- `RMBG` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 6 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
