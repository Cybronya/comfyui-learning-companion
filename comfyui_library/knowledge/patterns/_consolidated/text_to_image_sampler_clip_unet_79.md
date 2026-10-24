---
name: text_to_image_sampler_clip_unet_79
type: Text To Image
frequency: 8
level: moderate
coverage: 0.7415
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, KSampler, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json, 图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_2074311721812062209.json, 图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json, 图片生成/文生图/Z-image turbo D-OPSD文生图_2057063739513462785.json, 图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json, 图片生成/文生图/Z-image-暗黑浮世绘_1997401855502258178.json, 图片生成/文生图/Z-image-神级文生图-20秒超快速出图TEXT TO IMAGE_1993958594863366145.json, 图片生成/文生图/多种测试对比Flux2-Klein 9B、4b、qwen image2512、z image_2012884744526106625.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_1993970117180669953.json、图片生成/文生图/Z-image text-to-image-文生图-超自然人像-20秒快速出图_2074311721812062209.json、图片生成/文生图/Z-image text-to-image-文生图（完美支持中文字+超自然）​【Agent必备】_2088917231601278978.json、图片生成/文生图/Z-image turbo D-OPSD文生图_2057063739513462785.json、图片生成/文生图/Z-image-刘亦菲专用_1996450752195338242.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/8 个有
- `easy promptLine` —— 5/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `easy seed` —— 3/8 个有
- `LoadImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `CR Overlay Text` —— 1/8 个有
- `CR SDXL Aspect Ratio` —— 1/8 个有
- `EmptyFlux2LatentImage` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `Int` —— 1/8 个有
- `KSamplerAdvanced` —— 1/8 个有
- `Load Lora` —— 1/8 个有
- `ModelPatchTorchSettings` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 8 | 0% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 1024 - 1920 | 8 | 71% |
| 高度 | 1580 | 1080 - 1920 | 8 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1024 - 1920，8 个样本
- 高度 中位数 1580，观测区间 1080 - 1920，8 个样本
