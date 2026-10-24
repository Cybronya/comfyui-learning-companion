---
name: unknown_workflow_upscale_sampler_clip_23
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.882833
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, GetImageSize+, GetImageSizeAndCount, If ANY execute A else B, Image Comparer (rgthree), ImageColorMatch+, ImageFromBatch, ImageListToImageBatch, ImageResize+, ImageResizeKJv2, ImpactCompare, ImpactImageBatchToImageList, Int, KSamplerAdvanced, LoadImage, MathExpression|pysssss, ModelSamplingAuraFlow, RH_Captioner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, Switch any [Crystools], TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, Upscale Model Loader, Upscale by Factor with Model (WLSH), VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2047310409799049218.json, 图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577.json, 图片生成/文生图/免费使用image-2带API-提示词合集_2048062518664372226.json, 图片生成/文生图/免费使用image-2带API提示词合集_2047662382851301378.json, 图片生成/文生图/单次0.02最强图像模型gp-2_2047335832788406274.json, 图片生成/文生图/最强图像模型单次0.02_2046593384072089602.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2047310409799049218.json、图片生成/图生图/image2.0 后处理 去模糊放大，去ai感，合理细节_2068868548872728577.json、图片生成/文生图/免费使用image-2带API-提示词合集_2048062518664372226.json、图片生成/文生图/免费使用image-2带API提示词合集_2047662382851301378.json、图片生成/文生图/单次0.02最强图像模型gp-2_2047335832788406274.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize+`
- `GetImageSizeAndCount`
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

**可变部分**（部分 workflow 才有）：
- `FancyTimerNode` —— 4/6 个有
- `GptImage2` —— 4/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | res_multistep | - | 6 | 100% |
| 重绘幅度 | sgm_uniform | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，6 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，6 个样本，一致性 100%
