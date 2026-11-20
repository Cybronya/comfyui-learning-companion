---
name: image_to_image_lora_sampler_clip_99
type: Image To Image
frequency: 3
level: moderate
coverage: 0.911667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux细节放大_2052729152310132738.json, 图片生成/图生图/krea2_基础洗图_2078296158694367233.json, 图片生成/图生图/高清放大_2073939042080743426.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux细节放大_2052729152310132738.json、图片生成/图生图/krea2_基础洗图_2078296158694367233.json、图片生成/图生图/高清放大_2073939042080743426.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
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
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `Float` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `Power Prompt (rgthree)` —— 1/3 个有
- `Qwen3_VQA_Plus` —— 1/3 个有
- `RHUploadZip_V2` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
