---
name: image_to_image_lora_sampler_unet_226
type: Image To Image
frequency: 2
level: weak
coverage: 0.873
common_nodes: [CLIPLoader, CR Text Concatenate, ComfySwitchNode, ConditioningZeroOut, DapaoBatchImageGrid, EmptyLatentImage, HfImageToRGB, KSampler, LayerColor: Brightness & Contrast, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, PrimitiveStringMultiline, QwenImage21Cache, RHHiddenNodes, ReferenceLatent, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, ShunjingAIShade, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy compare, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSwitch, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 图像缩放V2_孤海, 长边短边]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/“一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009.json, 图片生成/图生图/“一张图能变多少姿势？”不！是Qwen2.1出的一整套人像写真！小红书宫格图组图故事板分镜随心发！_2108456964538847234.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_226

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/“一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009.json、图片生成/图生图/“一张图能变多少姿势？”不！是Qwen2.1出的一整套人像写真！小红书宫格图组图故事板分镜随心发！_2108456964538847234.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Text Concatenate`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `DapaoBatchImageGrid`
- `EmptyLatentImage`
- `HfImageToRGB`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `RHHiddenNodes`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `ShunjingAIShade`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy compare`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSwitch`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `图像缩放V2_孤海`
- `长边短边`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | deis_2m | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis_2m，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
