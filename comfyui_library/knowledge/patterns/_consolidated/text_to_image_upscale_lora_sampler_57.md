---
name: text_to_image_upscale_lora_sampler_57
type: Text To Image
frequency: 5
level: weak
coverage: 0.5374
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelPreviewOverrideKJ, PathchSageAttentionKJ, PlaySound|pysssss, ProcessString, QwenImage21Cache, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, TextEncodeQwenImage21, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy int, easy promptLine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210.json, 图片生成/图生图/写真V2 Qwen2.1分镜加Z修复加TTP HD 人像写真批量生成_2109079609693261826.json, 图片生成/文生图/Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025.json, 图片生成/文生图/④「写真V0」Z+Qwen2.1写真分镜10.9｜分镜写真一站出_2111787573340368897.json, 图片生成/文生图/写真V0方案Z加Qwen2.1，写真分镜反推提示词图生图_2111914346568830977.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_57

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/❼「写真V2」Qwen2.1分镜+Z修复+TTP-HD「10.9」_2108567666360414210.json、图片生成/图生图/写真V2 Qwen2.1分镜加Z修复加TTP HD 人像写真批量生成_2109079609693261826.json、图片生成/文生图/Z加Qwen2.1写真分镜方案，文生图反推提示词出片_2110508368321409025.json、图片生成/文生图/④「写真V0」Z+Qwen2.1写真分镜10.9｜分镜写真一站出_2111787573340368897.json、图片生成/文生图/写真V0方案Z加Qwen2.1，写真分镜反推提示词图生图_2111914346568830977.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `ProcessString`
- `QwenImage21Cache`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy promptLine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `solarL_SaveImagesToZip` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `ImageScaleBy` —— 3/5 个有
- `LayerUtility: TextBox` —— 3/5 个有
- `PrimitiveString` —— 3/5 个有
- `StringConcatenate` —— 3/5 个有
- `ColorMatchV2` —— 2/5 个有
- `ComfySwitchNode` —— 2/5 个有
- `ImageScale` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `TTP_Image_Assy` —— 2/5 个有
- `TTP_Image_Tile_Batch` —— 2/5 个有
- `TTP_Tile_image_size` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `easy imageSize` —— 2/5 个有
- `easy imageSizeBySide` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 5 | 0% |
| 高度 | 80 | 80 - 1024 | 5 | 0% |
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 63% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 0.15 - 1 | 5 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，5 个样本
- 高发问题（9/5 个样本）：Steps较低可能导致细节不足
