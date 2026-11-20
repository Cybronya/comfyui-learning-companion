---
name: text_to_image_lora_sampler_clip_211
type: Text To Image
frequency: 9
level: weak
coverage: 0.902667
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, KSampler, KSamplerSelect, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveInt, QwenImage21SageAttentionT8, RHHiddenNodes, ReferenceLatent, SamplerCustom, SaveImage, SeedVR2Conditioning, SeedVR2Preprocess, ShunjingAIShade, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy compare, easy imageBatchToImageList, easy imageListToImageBatch, 长边短边]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json, 图片生成/图生图/单图Qwen2.1八步加速全套写真｜小红书宫格组图随心发_2111789296247205889.json, 图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json, 图片生成/图生图/单图直出Qwen2.1全套写真｜八步加速极速出图｜小红书宫格组图与短剧分镜全搞定_2114612418428104706.json, 图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json, 图片生成/图生图/秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778.json, 平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2110404577534234625.json, 平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2117756795375673345.json, 平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2117789466944434177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_211

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json、图片生成/图生图/单图Qwen2.1八步加速全套写真｜小红书宫格组图随心发_2111789296247205889.json、图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json、图片生成/图生图/单图直出Qwen2.1全套写真｜八步加速极速出图｜小红书宫格组图与短剧分镜全搞定_2114612418428104706.json、图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
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
- `长边短边`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 8/9 个有
- `easy imageSwitch` —— 8/9 个有
- `图像缩放V2_孤海` —— 6/9 个有
- `CR Text Concatenate` —— 5/9 个有
- `DapaoBatchImageGrid` —— 5/9 个有
- `HfImageToRGB` —— 5/9 个有
- `LayerColor: Brightness & Contrast` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `easy promptLine` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `llama_cpp_instruct_adv` —— 5/9 个有
- `llama_cpp_model_loader` —— 5/9 个有
- `llama_cpp_parameters` —— 5/9 个有
- `ImageConcatMulti` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `SeedNode` —— 4/9 个有
- `easy imageRemBg` —— 4/9 个有
- `GetImageSize` —— 3/9 个有
- `JjkText` —— 3/9 个有
- `solarL_SaveImagesToZip` —— 3/9 个有
- `孤海注释` —— 3/9 个有
- `EmptyImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 4 | 9 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 9 | 24% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 80 - 1024 | 9 | 37% |
| 高度 | 1024 | 80 - 1024 | 9 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，9 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，9 个样本，取值分散，一致性仅 37%
- 高发问题（21/9 个样本）：Steps较低可能导致细节不足
