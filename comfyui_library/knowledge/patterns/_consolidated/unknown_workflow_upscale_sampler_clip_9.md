---
name: unknown_workflow_upscale_sampler_clip_9
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.894
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, FancyTimerNode, GetImageSize+, GetImageSizeAndCount, GptImage2, If ANY execute A else B, Image Comparer (rgthree), ImageColorMatch+, ImageFromBatch, ImageListToImageBatch, ImageResize+, ImageResizeKJv2, ImpactCompare, ImpactImageBatchToImageList, Int, KSamplerAdvanced, LoadImage, MathExpression|pysssss, ModelSamplingAuraFlow, RH_Captioner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, Switch any [Crystools], TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, Upscale Model Loader, Upscale by Factor with Model (WLSH), VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/文生图/免费使用image-2带API-提示词合集_2048062518664372226.json, 图片生成/文生图/免费使用image-2带API提示词合集_2047662382851301378.json, 图片生成/文生图/单次0.02最强图像模型gp-2_2047335832788406274.json, 图片生成/文生图/最强图像模型单次0.02_2046593384072089602.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/免费使用image-2带API-提示词合集_2048062518664372226.json、图片生成/文生图/免费使用image-2带API提示词合集_2047662382851301378.json、图片生成/文生图/单次0.02最强图像模型gp-2_2047335832788406274.json、图片生成/文生图/最强图像模型单次0.02_2046593384072089602.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `FancyTimerNode`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GptImage2`
- `If ANY execute A else B`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageFromBatch`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImpactCompare`
- `ImpactImageBatchToImageList`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingAuraFlow`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `Switch any [Crystools]`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `Upscale Model Loader`
- `Upscale by Factor with Model (WLSH)`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | res_multistep | - | 4 | 100% |
| 重绘幅度 | sgm_uniform | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，4 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，4 个样本，一致性 100%
