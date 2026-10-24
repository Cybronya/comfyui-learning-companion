---
name: unknown_workflow_upscale_lora_sampler_100
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.947
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, DetailDaemonSamplerNode, Image Comparer (rgthree), ImageAddNoise, ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/自用放大_2066451375378227201.json, 图片生成/图生图/自用放大_2068887043123531777.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_100

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/自用放大_2066451375378227201.json、图片生成/图生图/自用放大_2068887043123531777.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `Image Comparer (rgthree)`
- `ImageAddNoise`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
