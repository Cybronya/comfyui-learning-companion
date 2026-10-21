---
name: text_to_image_lora_sampler_clip_191
type: Text To Image
frequency: 6
level: strong
coverage: 0.861167
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), JjkText, KSampler, LoraLoaderModelOnly, PreviewAny, PrimitiveStringMultiline, ResizeImageMaskNode, SDXLEmptyLatentSizePicker+, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2PostProcessing, SeedVR2Preprocess, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [SDXLEmptyLatentSizePicker+, Seed (rgthree)]
members: [图片生成/图生图/2102147030348029953.json, 图片生成/文生图/Krea2 Turbo 文生图利器｜风格参考巨物四视图V2升级版_2097881094573092866.json, 图片生成/文生图/Krea2 Turbo文生风格参考LoRA强化版V2，图片风格反推极速高清放大_2103528384851693570.json, 图片生成/文生图/Krea2Turbo四视图巨物｜风格参考文生图工作流V2_2093425905577316354.json, 图片生成/文生图/Krea2Turbo文生图V2工作流｜风格参考巨物美学四视图生成_2097751520233218050.json, 图片生成/文生图/风格参考巨物四视图｜Krea2Turbo文生图V2工作流_2093755784319553538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_191

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2102147030348029953.json、图片生成/文生图/Krea2 Turbo 文生图利器｜风格参考巨物四视图V2升级版_2097881094573092866.json、图片生成/文生图/Krea2 Turbo文生风格参考LoRA强化版V2，图片风格反推极速高清放大_2103528384851693570.json、图片生成/文生图/Krea2Turbo四视图巨物｜风格参考文生图工作流V2_2093425905577316354.json、图片生成/文生图/Krea2Turbo文生图V2工作流｜风格参考巨物美学四视图生成_2097751520233218050.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `SDXLEmptyLatentSizePicker+`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 4/6 个有
- `MuyeTextEditOutput` —— 4/6 个有
- `easy stylesSelector` —— 4/6 个有
- `BasicScheduler` —— 2/6 个有
- `BiRefNetRMBG` —— 2/6 个有
- `CFGGuider` —— 2/6 个有
- `Fast Bypasser (rgthree)` —— 2/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `KSamplerSelect` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `ModelSamplingFlux` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `RandomNoise` —— 2/6 个有
- `SamplerCustomAdvanced` —— 2/6 个有
- `TextEncodeQwenImageEditPlus` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（22/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SDXLEmptyLatentSizePicker+、Seed (rgthree)
