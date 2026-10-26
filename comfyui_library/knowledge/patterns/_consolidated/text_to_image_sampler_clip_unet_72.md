---
name: text_to_image_sampler_clip_unet_72
type: Text To Image
frequency: 9
level: moderate
coverage: 0.887444
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image广告海报设计_1956984376598913026.json, 图片生成/图生图/Qwen-image洗图模仿海报_1982385126329982978.json, 图片生成/图生图/Qwen-image海报洗图_2034524062973698049.json, 图片生成/图生图/Qwen图生图（仿图）V1.0_1971583463797223426.json, 图片生成/图生图/qwen-洗图仿图海报模仿-8步快速出图_1962417242996609026.json, 图片生成/图生图/【电商仿图】Qwen海报设计图生图 电商产品平面设计编辑图片_1979055932632109058.json, 图片生成/图生图/洗图模仿海报风格，效果稳定_1992790546683064322.json, 图片生成/文生图/Qwen-image洗图模仿海报_风格等_1955802388865191937.json, 图片生成/文生图/奶茶产品宣传图_1975922379924877314.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-image广告海报设计_1956984376598913026.json、图片生成/图生图/Qwen-image洗图模仿海报_1982385126329982978.json、图片生成/图生图/Qwen-image海报洗图_2034524062973698049.json、图片生成/图生图/Qwen图生图（仿图）V1.0_1971583463797223426.json、图片生成/图生图/qwen-洗图仿图海报模仿-8步快速出图_1962417242996609026.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/9 个有
- `JanusImageUnderstanding` —— 7/9 个有
- `JanusModelLoader` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `FluxResolutionNode` —— 2/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `ImageUpscaleWithModel` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `UpscaleModelLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 768 | 9 | 85% |
| 高度 | 1024 | 512 - 1024 | 9 | 77% |
| 采样步数 | 35 | 8 - 35 | 9 | 73% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 9 | 74% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 768，9 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 512 - 1024，9 个样本
- 采样步数 中位数 35，观测区间 8 - 35，9 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
