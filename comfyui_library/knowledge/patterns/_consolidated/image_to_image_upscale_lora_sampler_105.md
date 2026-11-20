---
name: image_to_image_upscale_lora_sampler_105
type: Image To Image
frequency: 2
level: weak
coverage: 0.855
common_nodes: [CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, GetNode, Image Comparer (rgthree), Image Tiled, ImageConcanate, ImageFromBatch, ImageListToBatch+, ImageResizeKJv2, ImageUpscaleWithModel, Images to RGB, ImpactCompare, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, PreviewImage, PrimitiveInt, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy if, easy imageBatchToImageList, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/反推提示词+生成彩色总图+放大_2030931424068509697.json, 图片生成/图生图/建筑-qwen2511总图风格迁移工作流_2037860753994162178.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/反推提示词+生成彩色总图+放大_2030931424068509697.json、图片生成/图生图/建筑-qwen2511总图风格迁移工作流_2037860753994162178.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageListToBatch+`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `Images to RGB`
- `ImpactCompare`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `PrimitiveInt`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy if`
- `easy imageBatchToImageList`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
