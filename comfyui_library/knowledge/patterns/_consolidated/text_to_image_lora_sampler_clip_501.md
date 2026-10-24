---
name: text_to_image_lora_sampler_clip_501
type: Text To Image
frequency: 3
level: strong
coverage: 0.892667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, JjkText, KSampler, LoraLoaderModelOnly, PIP_StringConcatenation, PrimitiveInt, RH_Captioner, RH_RhartImageG2TextToImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4K写实人像一键直出｜G-image2文生图人像写真全能输出_2089015295485767681.json, 图片生成/文生图/G-image2全能文生图4K输出｜真实人像写真高清摄影级生成_2088694613237395458.json, 图片生成/文生图/真实人像4K输出｜全能图片G-image2文生图人像写真_2093780250059689985.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_501

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/4K写实人像一键直出｜G-image2文生图人像写真全能输出_2089015295485767681.json、图片生成/文生图/G-image2全能文生图4K输出｜真实人像写真高清摄影级生成_2088694613237395458.json、图片生成/文生图/真实人像4K输出｜全能图片G-image2文生图人像写真_2093780250059689985.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PIP_StringConcatenation`
- `PrimitiveInt`
- `RH_Captioner`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
