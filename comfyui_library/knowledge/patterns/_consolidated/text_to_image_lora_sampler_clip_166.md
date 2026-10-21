---
name: text_to_image_lora_sampler_clip_166
type: Text To Image
frequency: 7
level: strong
coverage: 0.885571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PIP_StringConcatenation, RH_RhartImageG2TextToImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy positive, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4K写实人像一键直出｜G-image2文生图人像写真全能输出_2089015295485767681.json, 图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101365555285544962.json, 图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101755378726948865.json, 图片生成/文生图/G-image2全能文生图4K输出｜真实人像写真高清摄影级生成_2088694613237395458.json, 图片生成/文生图/G-image2全能真实人像文生图｜2K输出摄影级写实人像写真_2088691697495662593.json, 图片生成/文生图/真实人像2K输出｜全能图片G-image2文生图人像写真_2093778848361046017.json, 图片生成/文生图/真实人像4K输出｜全能图片G-image2文生图人像写真_2093780250059689985.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/4K写实人像一键直出｜G-image2文生图人像写真全能输出_2089015295485767681.json、图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101365555285544962.json、图片生成/文生图/G-Image2真实人像2K输出全能图片文生图处理工具_2101755378726948865.json、图片生成/文生图/G-image2全能文生图4K输出｜真实人像写真高清摄影级生成_2088694613237395458.json、图片生成/文生图/G-image2全能真实人像文生图｜2K输出摄影级写实人像写真_2088691697495662593.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PIP_StringConcatenation`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/7 个有
- `DualCLIPLoader` —— 3/7 个有
- `FluxGuidance` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `SeedVR2` —— 3/7 个有
- `SeedVR2BlockSwap` —— 3/7 个有
- `SeedVR2ExtraArgs` —— 3/7 个有
- `VAEEncode` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
