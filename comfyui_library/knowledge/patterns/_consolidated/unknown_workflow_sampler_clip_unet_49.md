---
name: unknown_workflow_sampler_clip_unet_49
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.925
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein 人像精修+超高真实度+UPC_2086291438622568450.json, 图片生成/图生图/Klein 人像精修+超高真实度_2082670545430208513.json, 图片生成/图生图/Klein-一致性_2028476879887409154.json, 图片生成/图生图/Klein转线稿_2039620047836024834.json, 图片生成/图生图/Klein转线稿_2060181415077171201.json, 图片生成/图生图/Krea2 巨构场景_2107642380689166338.json, 图片生成/图生图/klein 人像精修  超高真实度_2076192004383531010.json, 图片生成/图生图/老孙AI人像精修+真实度超高_2095676269265510402.json, 图片生成/文生图/Z-Image-超写实人像质感_2017821123303444482.json, 图片生成/文生图/国风角色设计-橘_2035340702317551618.json, 图片生成/文生图/文生图 角色生成 仙侠 古风 现代（超清）_2100600038656405506.json, 图片生成/文生图/最新版万能图像生成器-太牛逼了_2028849021414023170.json, 图片生成/文生图/自用-万能图像生成器工作流_2037031301642981378.json, 图片生成/文生图/角色设计（动漫）-橘_2053012314667925506.json, 图片生成/文生图/超强自定义角色生成_2024732759662530561.json, 图片生成/文生图/👾怪獸-国风角色设计👾_2058099509644840962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Klein 人像精修+超高真实度+UPC_2086291438622568450.json、图片生成/图生图/Klein 人像精修+超高真实度_2082670545430208513.json、图片生成/图生图/Klein-一致性_2028476879887409154.json、图片生成/图生图/Klein转线稿_2039620047836024834.json、图片生成/图生图/Klein转线稿_2060181415077171201.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `GetImageSize` —— 15/16 个有
- `CR Text` —— 14/16 个有
- `KSamplerAdvanced` —— 13/16 个有
- `LoraLoaderModelOnly` —— 13/16 个有
- `ModelSamplingAuraFlow` —— 13/16 个有
- `PreviewImage` —— 12/16 个有
- `EmptyLatentImage` —— 9/16 个有
- `ImageSharpen` —— 9/16 个有
- `LayerUtility: PurgeVRAM V2` —— 9/16 个有
- `LoadImage` —— 9/16 个有
- `ColorMatch` —— 8/16 个有
- `INTConstant` —— 7/16 个有
- `Int` —— 7/16 个有
- `SeedVR2LoadDiTModel` —— 7/16 个有
- `SeedVR2LoadVAEModel` —— 7/16 个有
- `SeedVR2VideoUpscaler` —— 7/16 个有
- `Float` —— 6/16 个有
- `RH_Captioner` —— 5/16 个有
- `ImageScaleBy` —— 4/16 个有
- `Label (rgthree)` —— 4/16 个有
- `LayerColor: ColorTemperature` —— 4/16 个有
- `RunningHub Deepcleaner` —— 4/16 个有
- `easy showAnything` —— 4/16 个有
- `ProcessString` —— 3/16 个有
- `ShowText|pysssss` —— 3/16 个有
- `easy promptLine` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `RH_LLMAPI_Pro_Node` —— 2/16 个有
- `Any Switch (rgthree)` —— 1/16 个有
- `CLIPLoaderGGUF` —— 1/16 个有
- `ColorMatchV2` —— 1/16 个有
- `GetImage` —— 1/16 个有
- `RH_LLMAPI_NODE` —— 1/16 个有
- `Seed (rgthree)` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 92% |
| Prompt 约束强度(CFG) | 3 | 3 - 12 | 13 | 40% |
| 采样算法 | 1 | 1 - 2 | 13 | 66% |
| 调度器 | euler | - | 13 | 92% |
| 重绘幅度 | simple | - | 13 | 69% |
| 宽度 | 1024 | 832 - 1024 | 9 | 94% |
| 高度 | 1536 | 1536 - 1536 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 12，13 个样本，取值分散，一致性仅 40%
- 采样算法 中位数 1，观测区间 1 - 2，13 个样本
- 调度器 最常用 euler，13 个样本，一致性 92%
- 重绘幅度 最常用 simple，13 个样本，一致性 69%
- 宽度 中位数 1024，观测区间 832 - 1024，9 个样本，取值集中（一致性 94%）
- 高度 中位数 1536，观测区间 1536 - 1536，9 个样本，取值集中（一致性 100%）
