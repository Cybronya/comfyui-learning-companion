---
name: unknown_workflow_upscale_sampler_clip_39
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7986
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSamplerAdvanced, KSamplerSelect, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/VividMuse真实人像摄影洗图V1_2017936931623018498.json, 图片生成/图生图/VividMuse真实人像摄影洗图V2_2036774382349066242.json, 图片生成/图生图/Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698.json, 图片生成/文生图/VividMuse真实人像摄影V1_2015351994625564673.json, 平台全量/真实人像摄影洗图V3_2037838601618202626.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/VividMuse真实人像摄影洗图V1_2017936931623018498.json、图片生成/图生图/VividMuse真实人像摄影洗图V2_2036774382349066242.json、图片生成/图生图/Z-image+FLUX.2 klein真实人像洗图流_2083187504395677698.json、图片生成/文生图/VividMuse真实人像摄影V1_2015351994625564673.json、平台全量/真实人像摄影洗图V3_2037838601618202626.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 4/5 个有
- `Florence2Run` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `LayerUtility: ImageReel` —— 4/5 个有
- `LayerUtility: ImageReelComposit` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `WD14Tagger|pysssss` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `easy promptConcat` —— 4/5 个有
- `BasicScheduler` —— 3/5 个有
- `SigmasPreview` —— 3/5 个有
- `easy promptReplace` —— 3/5 个有
- `DF_Text_Box` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `Text Input [DVB]` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 60% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 5 | 60% |
| 宽度 | 1536 | - | 1 | 100% |
| 高度 | 2048 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 60%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 60%
