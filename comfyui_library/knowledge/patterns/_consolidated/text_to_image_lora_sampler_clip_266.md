---
name: text_to_image_lora_sampler_clip_266
type: Text To Image
frequency: 4
level: strong
coverage: 0.658
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, QwenImage21Cache, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything, ki_宫格拼图简易版, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1全能工作流，文生图反推提示词图生图多合一_2102880404171739138.json, 图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json, 图片生成/文生图/Qwen image2.1全能工作流｜文生图人像写真 图生图一套全包_2104107604501942274.json, 视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_266

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1全能工作流，文生图反推提示词图生图多合一_2102880404171739138.json、图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json、图片生成/文生图/Qwen image2.1全能工作流｜文生图人像写真 图生图一套全包_2104107604501942274.json、视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `QwenImage21Cache`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `ki_宫格拼图简易版`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 3/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
