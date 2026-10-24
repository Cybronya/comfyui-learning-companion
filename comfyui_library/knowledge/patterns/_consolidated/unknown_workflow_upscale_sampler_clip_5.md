---
name: unknown_workflow_upscale_sampler_clip_5
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.877833
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506.json, 图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2064232764295172097.json, 图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2066411204498780162.json, 图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2068584085240504321.json, 图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2068585640224186369.json, 图片生成/图生图/Z-Image+Qwen3.5-洗图-4K高清放大_2081664367967432705.json, 图片生成/图生图/Z-Image+QwenVL-洗图-4K放大_1995873032013066242.json, 图片生成/图生图/图生图-Z-Image+Qwen3.5-完美洗图-4K放大_2064524144569573378.json, 图片生成/图生图/完美洗图-4K放大Z-Image+Qwen3.5_2066331188700205058.json, 图片生成/图生图/模特写真美图随机裂变 Z-Image+Qwen3.5人物写真 -完美洗图 4K高清放大_2064869020309999618.json, 图片生成/文生图/Z-Image-Qwen3vl-洗图-放大_1994350779123240961.json, 图片生成/文生图/Z-Image-base洗图放大_2016774612377407489.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2048356894611349506.json、图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2064232764295172097.json、图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2066411204498780162.json、图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2068584085240504321.json、图片生成/图生图/Z-Image+Qwen3.5-完美洗图-4K放大_2068585640224186369.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `Miaoshouai_Tagger` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/12 个有
- `Text` —— 9/12 个有
- `llama_cpp_instruct_adv` —— 9/12 个有
- `llama_cpp_model_loader` —— 9/12 个有
- `llama_cpp_parameters` —— 9/12 个有
- `PreviewImage` —— 7/12 个有
- `AddLabel` —— 3/12 个有
- `EmptySD3LatentImage` —— 3/12 个有
- `ImageResizeKJv2` —— 3/12 个有
- `孤海注释` —— 3/12 个有
- `MultiplePathsInput` —— 2/12 个有
- `Qwen3_VQA` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `AILab_QwenVL` —— 1/12 个有
- `Florence2ModelLoader` —— 1/12 个有
- `Florence2Run` —— 1/12 个有
- `Int` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 25 | 12 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 12 | 34% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 0.75 | 0.75 - 1 | 12 | 90% |
| LoRA 模型强度 | 0.85 | 0.85 - 0.85 | 11 | 100% |
| LoRA 文本强度 | 0.85 | 0.85 - 0.85 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 25，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，12 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 1，12 个样本，取值集中（一致性 90%）
- LoRA 模型强度 中位数 0.85，观测区间 0.85 - 0.85，11 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.85，观测区间 0.85 - 0.85，11 个样本，取值集中（一致性 100%）
- 高发问题（22/12 个样本）：Steps较低可能导致细节不足
