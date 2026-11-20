---
name: unknown_workflow_upscale_lora_sampler_77
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.608667
common_nodes: [BasicScheduler, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningAverage, Florence2ModelLoader, Florence2Run, GetNode, Image Comparer (rgthree), ImageResizeKJ, ImageScaleToTotalPixels, ImageSmartSharpen+, ImageUpscaleWithModel, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TTP_CoordinateSplitter, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json, 图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json, 平台全量/✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_77

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/wan2.2+ttp放大【分块提示词】+nag高清放大_1955888060602961921.json、图片生成/图生图/✅wan2.2+ttp放大+nag-高清放大_细节修复-分块提示词_1950234235819966466.json、平台全量/✅Flux.1 SRPO+ttp放大-高清放大_细节修复-分块提示词_1919791173198610433.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
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
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `Manual XY Entry Info` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `NAGGuider` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DetailDaemonSamplerNode` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `Float` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `InjectLatentNoise+` —— 1/3 个有
- `Int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
