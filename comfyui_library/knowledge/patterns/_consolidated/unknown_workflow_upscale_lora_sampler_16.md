---
name: unknown_workflow_upscale_lora_sampler_16
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.843385
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, easy cleanGpuUsed, easy int]
problems: []
missing: []
members: [图片生成/反推提示词/z-image+qwen3.8  文生图+洗图双切换_2116426410230378498.json, 图片生成/图生图/大炮V5_2061711762688397314.json, 图片生成/图生图/大炮V5自选lora_2061723320797720578.json, 图片生成/图生图/🥳随机美女孵蛋器 V5升级版 随机+洗图双切换【绅士模式】_2061281616344997890.json, 图片生成/文生图/260816001.自动优化提示词文生图+洗图_2089003471939923969.json, 图片生成/文生图/4K大炮V5CCD氛围感增强_2064895128690577409.json, 图片生成/文生图/Z-Image-文生图-超高清放大_2101279706992697346.json, 图片生成/文生图/大炮V5CCD一次四张横屏_2065332767617015810.json, 图片生成/文生图/大炮V5CCD一次四张竖屏_2065319074950893570.json, 图片生成/文生图/大炮v5-CCD-V2.0_2066696865017581570.json, 图片生成/文生图/大炮v5-CCD-V4.1_2066779112580149250.json, 平台全量/美女生成器_2104536034028642306.json, 平台全量/随机美女生成V5版 随机+洗图双切换_2061993896393138178.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/反推提示词/z-image+qwen3.8  文生图+洗图双切换_2116426410230378498.json、图片生成/图生图/大炮V5_2061711762688397314.json、图片生成/图生图/大炮V5自选lora_2061723320797720578.json、图片生成/图生图/🥳随机美女孵蛋器 V5升级版 随机+洗图双切换【绅士模式】_2061281616344997890.json、图片生成/文生图/260816001.自动优化提示词文生图+洗图_2089003471939923969.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DapaoImageAspectRatioResizeNode` —— 12/13 个有
- `DapaoImageCompressionNode` —— 12/13 个有
- `DapaoImageRatioLimitNode` —— 12/13 个有
- `Dapao_LlamaChat` —— 12/13 个有
- `ImpactSwitch` —— 12/13 个有
- `Int` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `Seed (rgthree)` —— 12/13 个有
- `easy positive` —— 12/13 个有
- `easy showAnything` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `忽略多组孤海` —— 12/13 个有
- `Note Plus (mtb)` —— 8/13 个有
- `easy saveText` —— 5/13 个有
- `RepeatLatentBatch` —— 4/13 个有
- `CR Prompt List` —— 2/13 个有
- `DapaoSafeSaveImage` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `String Literal` —— 2/13 个有
- `Text Concatenate (JPS)` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1536 | 1536 - 1536 | 13 | 100% |
| 采样步数 | fixed | - | 13 | 85% |
| Prompt 约束强度(CFG) | 3 | 3 - 12 | 13 | 35% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler | - | 13 | 100% |
| 重绘幅度 | simple | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，13 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，13 个样本，一致性 85%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 12，13 个样本，取值分散，一致性仅 35%
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，13 个样本，一致性 100%
- 重绘幅度 最常用 simple，13 个样本，一致性 100%
