---
name: text_to_image_lora_sampler_clip_340
type: Text To Image
frequency: 2
level: weak
coverage: 0.788
common_nodes: [AILab_ImageCompare, AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, PreviewImage, ResizeImageMaskNode, ResizeImagesByLongerEdge, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: [Fast Bypasser (rgthree), Seed (rgthree), easy stylesSelector]
members: [图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2081193864177733633.json, 图片生成/图生图/2092778942037057538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_340

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2-ZimageTurbo-控制文生图_洗图_漫转真人-V1_2081193864177733633.json、图片生成/图生图/2092778942037057538.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_ImageCompare`
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `Krea2ControlApply` —— 1/2 个有
- `Krea2ControlImageEncode` —— 1/2 个有
- `Krea2ControlLoRALoader` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `ZImageFunControlnet` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy stylesSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Fast Bypasser (rgthree)、Seed (rgthree)、easy stylesSelector
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
