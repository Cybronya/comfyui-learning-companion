---
name: text_to_image_lora_sampler_clip_336
type: Text To Image
frequency: 6
level: weak
coverage: 0.892167
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, KSampler, KSamplerSelect, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveInt, QwenImage21SageAttentionT8, RHHiddenNodes, ReferenceLatent, SamplerCustom, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, ShunjingAIShade, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy compare, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSwitch, 长边短边]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json, 图片生成/图生图/单图Qwen2.1八步加速全套写真｜小红书宫格组图随心发_2111789296247205889.json, 图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json, 图片生成/图生图/单图直出Qwen2.1全套写真｜八步加速极速出图｜小红书宫格组图与短剧分镜全搞定_2114612418428104706.json, 图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json, 图片生成/图生图/秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_336

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json、图片生成/图生图/单图Qwen2.1八步加速全套写真｜小红书宫格组图随心发_2111789296247205889.json、图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json、图片生成/图生图/单图直出Qwen2.1全套写真｜八步加速极速出图｜小红书宫格组图与短剧分镜全搞定_2114612418428104706.json、图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
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
- `长边短边`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 5/6 个有
- `DapaoBatchImageGrid` —— 5/6 个有
- `HfImageToRGB` —— 5/6 个有
- `LayerColor: Brightness & Contrast` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `easy promptLine` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `llama_cpp_parameters` —— 5/6 个有
- `图像缩放V2_孤海` —— 5/6 个有
- `JjkText` —— 3/6 个有
- `solarL_SaveImagesToZip` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `EmptyImage` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SeedNode` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.5 | 1 - 4 | 6 | 40% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 6 | 36% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 552 | 80 - 1024 | 6 | 14% |
| 高度 | 552 | 80 - 1024 | 6 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2.5，观测区间 1 - 4，6 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 552，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 14%
- 高发问题（15/6 个样本）：Steps较低可能导致细节不足
