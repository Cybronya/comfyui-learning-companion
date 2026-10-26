---
name: unknown_workflow_upscale_lora_sampler_100
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.597
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningAverage, Florence2ModelLoader, Florence2Run, GetNode, Image Comparer (rgthree), ImageResizeKJ, ImageScaleToTotalPixels, ImageSmartSharpen+, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoaderModelOnly, Manual XY Entry Info, ModelSamplingSD3, NAGGuider, PathchSageAttentionKJ, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TTP_CoordinateSplitter, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json, 图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_100

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json、图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningAverage`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageSmartSharpen+`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Manual XY Entry Info`
- `ModelSamplingSD3`
- `NAGGuider`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_CoordinateSplitter`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
