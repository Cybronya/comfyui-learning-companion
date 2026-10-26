---
name: unknown_workflow_upscale_lora_sampler_23
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.824111
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DapaoImageAspectRatioResizeNode, DapaoImageCompressionNode, DapaoImageRatioLimitNode, Dapao_LlamaChat, EmptyLatentImage, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, ImpactSwitch, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, easy cleanGpuUsed, easy int, easy positive, easy showAnything, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [图片生成/图生图/大炮V5_2061711762688397314.json, 图片生成/图生图/大炮V5自选lora_2061723320797720578.json, 图片生成/图生图/🥳随机美女孵蛋器 V5升级版 随机+洗图双切换【绅士模式】_2061281616344997890.json, 图片生成/文生图/260816001.自动优化提示词文生图+洗图_2089003471939923969.json, 图片生成/文生图/4K大炮V5CCD氛围感增强_2064895128690577409.json, 图片生成/文生图/大炮V5CCD一次四张横屏_2065332767617015810.json, 图片生成/文生图/大炮V5CCD一次四张竖屏_2065319074950893570.json, 图片生成/文生图/大炮v5-CCD-V2.0_2066696865017581570.json, 图片生成/文生图/大炮v5-CCD-V4.1_2066779112580149250.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/大炮V5_2061711762688397314.json、图片生成/图生图/大炮V5自选lora_2061723320797720578.json、图片生成/图生图/🥳随机美女孵蛋器 V5升级版 随机+洗图双切换【绅士模式】_2061281616344997890.json、图片生成/文生图/260816001.自动优化提示词文生图+洗图_2089003471939923969.json、图片生成/文生图/4K大炮V5CCD氛围感增强_2064895128690577409.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DapaoImageAspectRatioResizeNode`
- `DapaoImageCompressionNode`
- `DapaoImageRatioLimitNode`
- `Dapao_LlamaChat`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed (rgthree)`
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
- `easy positive`
- `easy showAnything`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 8/9 个有
- `easy saveText` —— 5/9 个有
- `RepeatLatentBatch` —— 4/9 个有
- `CR Prompt List` —— 2/9 个有
- `String Literal` —— 2/9 个有
- `Text Concatenate (JPS)` —— 2/9 个有
- `DapaoSafeSaveImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1536 | 1536 - 1536 | 9 | 100% |
| 采样步数 | fixed | - | 9 | 78% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，9 个样本，取值集中（一致性 100%）
- 采样步数 最常用 fixed，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
