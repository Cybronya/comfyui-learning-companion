---
name: text_to_image_lora_sampler_clip_413
type: Text To Image
frequency: 4
level: weak
coverage: 0.88375
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Concatenate, ComfySwitchNode, ConditioningZeroOut, DapaoBatchImageGrid, EmptyLatentImage, HfImageToRGB, KSampler, KSamplerSelect, LayerColor: Brightness & Contrast, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, QwenImage21SageAttentionT8, RHHiddenNodes, ReferenceLatent, SamplerCustom, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, ShunjingAIShade, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy compare, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSwitch, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, 图像缩放V2_孤海, 长边短边]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json, 图片生成/图生图/单图Qwen2.1八步加速全套写真｜小红书宫格组图随心发_2111789296247205889.json, 图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json, 图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_413

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json、图片生成/图生图/单图Qwen2.1八步加速全套写真｜小红书宫格组图随心发_2111789296247205889.json、图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json、图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `DapaoBatchImageGrid`
- `EmptyLatentImage`
- `HfImageToRGB`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImage21SageAttentionT8`
- `RHHiddenNodes`
- `ReferenceLatent`
- `SamplerCustom`
- `SaveImage`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `ShunjingAIShade`
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

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `孤海注释` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 1 - 4 | 4 | 60% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 4 | 58% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 1 - 4，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高发问题（11/4 个样本）：Steps较低可能导致细节不足
