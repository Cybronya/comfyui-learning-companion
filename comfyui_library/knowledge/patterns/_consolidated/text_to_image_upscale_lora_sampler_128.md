---
name: text_to_image_upscale_lora_sampler_128
type: Text To Image
frequency: 2
level: weak
coverage: 0.7895
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy positive, easy showAnything, llama_cpp_clean_states, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model, 孤海注释, 忽略多组孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1-Aiden-KREA2模型提示词优化lora加持工作流 (1)_2079925358706642945.json, 图片生成/文生图/1-Aiden-豹豹的K2墨玉AIO测试工作流（小白福音）_2078350888141414402.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_128

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1-Aiden-KREA2模型提示词优化lora加持工作流 (1)_2079925358706642945.json、图片生成/文生图/1-Aiden-豹豹的K2墨玉AIO测试工作流（小白福音）_2078350888141414402.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy positive`
- `easy showAnything`
- `llama_cpp_clean_states`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_unload_model`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `KOOK_ImageCompression` —— 1/2 个有
- `LayerColor: Brightness & Contrast` —— 1/2 个有
- `LayerFilter: AddGrain` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 616 | - | 2 | 83% |
| 高度 | 896 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 616，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 896，样本不足，未给区间，2 个样本
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
