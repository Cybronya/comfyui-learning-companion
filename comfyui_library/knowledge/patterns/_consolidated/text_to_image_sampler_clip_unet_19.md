---
name: text_to_image_sampler_clip_unet_19
type: Text To Image
frequency: 3
level: weak
coverage: 0.832333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, ConditioningZeroOut, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImpactInt, KSampler, LoadImage, RegexReplace, SaveImage, String Literal, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, String Literal, easy cleanGpuUsed, CR Prompt List]
members: [图片生成/图生图/2044345054734589954.json, 图片生成/文生图/Krea 2 turbo一键反推生图_2073390634911748097.json, 视频生成/图生视频/Krea2_Turbo一键反推生图_超高艺术性图片生成_2101078290697117697.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2044345054734589954.json、图片生成/文生图/Krea 2 turbo一键反推生图_2073390634911748097.json、视频生成/图生视频/Krea2_Turbo一键反推生图_超高艺术性图片生成_2101078290697117697.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `ConditioningZeroOut`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `RegexReplace`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Batch Images From List` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PixaromaLoraLoader` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 80 - 1280 | 3 | 29% |
| 高度 | 720 | 80 - 1280 | 3 | 29% |
| 采样步数 | 8 | 4 - 15 | 3 | 49% |
| Prompt 约束强度(CFG) | 1.1 | 1 - 4.5 | 3 | 26% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 80 - 1280，3 个样本，取值分散，一致性仅 29%
- 高度 中位数 720，观测区间 80 - 1280，3 个样本，取值分散，一致性仅 29%
- 采样步数 中位数 8，观测区间 4 - 15，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、String Literal、easy cleanGpuUsed、CR Prompt List
