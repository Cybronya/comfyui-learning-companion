---
name: text_to_image_lora_sampler_clip_392
type: Text To Image
frequency: 5
level: weak
coverage: 0.7068
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ki_人物四视图合集_2114476716134584321.json, 图片生成/文生图/Qwen Image 2.1全能工作流，文生图反推提示词图生图多合一_2102880404171739138.json, 图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json, 图片生成/文生图/Qwen image2.1全能工作流｜文生图人像写真 图生图一套全包_2104107604501942274.json, 视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_392

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ki_人物四视图合集_2114476716134584321.json、图片生成/文生图/Qwen Image 2.1全能工作流，文生图反推提示词图生图多合一_2102880404171739138.json、图片生成/文生图/Qwen image2.1全能工作流 文生图人像写真一站搞定_2104332186555080705.json、图片生成/文生图/Qwen image2.1全能工作流｜文生图人像写真 图生图一套全包_2104107604501942274.json、视频生成/图生视频/Qwen_Image_2.1全能工作流，文生图反推提示词图生图多合一_2105118701145120770.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 4/5 个有
- `CR Text Concatenate` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `JjkText` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `ki_宫格拼图简易版` —— 4/5 个有
- `solarL_SaveImagesToZip` —— 4/5 个有
- `孤海注释` —— 3/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `EmptyImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 2048 | 5 | 0% |
| 高度 | 80 | 80 - 1024 | 5 | 0% |
| 采样步数 | 4 | 4 - 40 | 5 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 5 | 63% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 2048，5 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，5 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 40，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
