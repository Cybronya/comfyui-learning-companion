---
name: unknown_workflow_sampler_clip_unet_149
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.92725
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 人像精修+超高真实度+UPC_2086291438622568450.json, 图片生成/图生图/Klein 人像精修+超高真实度_2082670545430208513.json, 图片生成/图生图/Klein-一致性_2028476879887409154.json, 图片生成/图生图/Krea2 巨构场景_2107642380689166338.json, 图片生成/图生图/klein 人像精修  超高真实度_2076192004383531010.json, 图片生成/图生图/老孙AI人像精修+真实度超高_2095676269265510402.json, 图片生成/文生图/Z-Image-超写实人像质感_2017821123303444482.json, 图片生成/文生图/国风角色设计-橘_2035340702317551618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_149

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Klein 人像精修+超高真实度+UPC_2086291438622568450.json、图片生成/图生图/Klein 人像精修+超高真实度_2082670545430208513.json、图片生成/图生图/Klein-一致性_2028476879887409154.json、图片生成/图生图/Krea2 巨构场景_2107642380689166338.json、图片生成/图生图/klein 人像精修  超高真实度_2076192004383531010.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 7/8 个有
- `KSamplerAdvanced` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `PreviewImage` —— 6/8 个有
- `RH_Captioner` —— 5/8 个有
- `Float` —— 4/8 个有
- `ImageScaleBy` —— 4/8 个有
- `LayerColor: ColorTemperature` —— 4/8 个有
- `RunningHub Deepcleaner` —— 4/8 个有
- `EmptyLatentImage` —— 3/8 个有
- `ImageSharpen` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `ColorMatch` —— 2/8 个有
- `Int` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `ColorMatchV2` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImage` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ProcessString` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `SeedVR2LoadDiTModel` —— 1/8 个有
- `SeedVR2LoadVAEModel` —— 1/8 个有
- `SeedVR2VideoUpscaler` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy promptLine` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 9 | 3 - 12 | 7 | 59% |
| 采样算法 | 1 | 1 - 2 | 7 | 69% |
| 调度器 | euler | - | 7 | 86% |
| 重绘幅度 | beta57 | - | 7 | 57% |
| 宽度 | 1024 | 832 - 1024 | 3 | 91% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 9，观测区间 3 - 12，7 个样本
- 采样算法 中位数 1，观测区间 1 - 2，7 个样本
- 调度器 最常用 euler，7 个样本，一致性 86%
- 重绘幅度 最常用 beta57，7 个样本，一致性 57%
- 宽度 中位数 1024，观测区间 832 - 1024，3 个样本，取值集中（一致性 91%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
