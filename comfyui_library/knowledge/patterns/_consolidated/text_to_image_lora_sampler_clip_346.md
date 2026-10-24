---
name: text_to_image_lora_sampler_clip_346
type: Text To Image
frequency: 5
level: weak
coverage: 0.468
common_nodes: [Any Switch (rgthree), BatchImagesNode, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, GetNode, Image Comparer (rgthree), ImageScaleToMaxDimension, JsonExtractString, KSampler, LoadImage, LoraLoaderBypassModelOnly, PreviewAny, PrimitiveBoolean, QwenImage21Cache, ResolutionSelector, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274.json, 图片生成/文生图/Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977.json, 图片生成/文生图/Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050.json, 图片生成/文生图/Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345.json, 图片生成/文生图/双自动提示词加持 Qwen image 2.1文生图与图像编辑提速版_2104264781883592705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_346

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1文生与编辑加速工作流双自动提示词，文生图图生图方案_2106086535849398274.json、图片生成/文生图/Qwen image 2.1 全家桶！加速版！ 图像编辑！文生图！  自动化高清！_2104014492534398977.json、图片生成/文生图/Qwen image 2.1全家桶加速版 图像编辑文生图自动化高清一站搞定_2104661091862274050.json、图片生成/文生图/Qwen image 2.1文生与编辑加速工作流｜双自动提示词 文生图图生图全能_2104030500267577345.json、图片生成/文生图/双自动提示词加持 Qwen image 2.1文生图与图像编辑提速版_2104264781883592705.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：47%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToMaxDimension`
- `JsonExtractString`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `PreviewAny`
- `PrimitiveBoolean`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `solarL_SaveImagesToZip` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `GoohaiAnyExists` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `JWFloat` —— 2/5 个有
- `KSamplerAdvanced` —— 2/5 个有
- `LatentSwitch` —— 2/5 个有
- `PDIMAGE_LongerSize` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `ReferenceLatent` —— 2/5 个有
- `SeedNode` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 5 | 0% |
| 高度 | 80 | 80 - 1024 | 5 | 0% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 4.5 | 5 | 95% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 4.5，5 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（14/5 个样本）：Steps较低可能导致细节不足
