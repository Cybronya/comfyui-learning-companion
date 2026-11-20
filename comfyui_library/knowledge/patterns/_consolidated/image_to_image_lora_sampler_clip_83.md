---
name: image_to_image_lora_sampler_clip_83
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8962
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux细节放大_2052729152310132738.json, 图片生成/图生图/krea2_基础洗图_2078296158694367233.json, 图片生成/图生图/高清放大_2073939042080743426.json, 平台全量/Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449.json, 平台全量/KR_基础洗图（2号流）wy_2057668746197684225.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux细节放大_2052729152310132738.json、图片生成/图生图/krea2_基础洗图_2078296158694367233.json、图片生成/图生图/高清放大_2073939042080743426.json、平台全量/Flux2 Klein+Qwen 模糊图变高清去油腻 图像高清放大全能图片2.0  4k超清细节修复_2030832469687144449.json、平台全量/KR_基础洗图（2号流）wy_2057668746197684225.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `llama_cpp_instruct_adv` —— 4/5 个有
- `llama_cpp_model_loader` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `KSamplerAdvanced` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `llama_cpp_parameters` —— 3/5 个有
- `Float` —— 2/5 个有
- `MemoryCleaner` —— 2/5 个有
- `Power Prompt (rgthree)` —— 2/5 个有
- `RH_Nano_Banana2_Image2Image` —— 2/5 个有
- `Qwen3_VQA_Plus` —— 1/5 个有
- `RHUploadZip_V2` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 5 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
