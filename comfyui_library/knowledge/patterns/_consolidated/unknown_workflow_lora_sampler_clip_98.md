---
name: unknown_workflow_lora_sampler_clip_98
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.789
common_nodes: [AddNoise, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Bypasser (rgthree), Fast Groups Muter (rgthree), GetNode, ImageScaleBy, KSamplerAdvanced, LayerColor: Brightness & Contrast, LayerFilter: FilmV2, LayerFilter: HDREffects, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RandomNoise, RepeatLatentBatch, SaveImage, Seed (rgthree), SetNode, ShowText|pysssss, Text Concatenate (JPS), UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive, easy stylesSelector, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Hui批量nannan_2066557417206411265.json, 图片生成/图生图/Z-image-图生图-超现实无虑境-原生2k高清大图--图生图-小红书风格-抖音洗图_2060364173141434369.json, 图片生成/图生图/Z图生图CCD加强_2064562670862426114.json, 图片生成/图生图/Z图生图_2061627415536951297.json, 图片生成/图生图/Z图生图自选lora_2061639631917117441.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Hui批量nannan_2066557417206411265.json、图片生成/图生图/Z-image-图生图-超现实无虑境-原生2k高清大图--图生图-小红书风格-抖音洗图_2060364173141434369.json、图片生成/图生图/Z图生图CCD加强_2064562670862426114.json、图片生成/图生图/Z图生图_2061627415536951297.json、图片生成/图生图/Z图生图自选lora_2061639631917117441.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `AddNoise`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LayerColor: Brightness & Contrast`
- `LayerFilter: FilmV2`
- `LayerFilter: HDREffects`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `RepeatLatentBatch`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`
- `easy stylesSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `easy saveText` —— 4/5 个有
- `Int` —— 1/5 个有
- `KOOK_ImageCompression` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1088 | 5 | 100% |
| 高度 | 1920 | 1920 - 1920 | 5 | 100% |
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 9 | 9 - 9 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | dpmpp_2m | - | 5 | 100% |
| 重绘幅度 | sgm_uniform | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1088，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，5 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，5 个样本，一致性 100%
