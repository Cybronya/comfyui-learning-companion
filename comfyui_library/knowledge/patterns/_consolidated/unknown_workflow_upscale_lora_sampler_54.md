---
name: unknown_workflow_upscale_lora_sampler_54
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.841667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Latent Batch Size, CR Text, CR Text Concatenate, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MathExpression|pysssss, PrimitiveBoolean, RH_Captioner, RH_Prompter, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy float, easy ifElse, easy imageBatchToImageList, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/FLUX Krea 去ai感洗图+高清放大_1951155305814142977.json, 图片生成/图生图/FLUX Krea 去ai感洗图+高清放大_1951568183708864514.json, 图片生成/图生图/FLUX Krea 去ai感洗图+高清放大_1961386334780854273.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX Krea 去ai感洗图+高清放大_1951155305814142977.json、图片生成/图生图/FLUX Krea 去ai感洗图+高清放大_1951568183708864514.json、图片生成/图生图/FLUX Krea 去ai感洗图+高清放大_1961386334780854273.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `CR Text`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
- `RH_Captioner`
- `RH_Prompter`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy float`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
