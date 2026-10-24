---
name: text_to_image_lora_sampler_clip_554
type: Text To Image
frequency: 2
level: weak
coverage: 0.6415
common_nodes: [AIO_Preprocessor, AnimaArtistStyleT8, AnimaBoosterLoader, AnimaGelbooruStyleT8, AnimaLLLiteApply, AnimaPromptCombinerT8, AnimaPromptT8, AnimaTeaCache, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, GetImageSize, GetNode, INTConstant, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LazySwitchKJ, Load Lora, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, PrimitiveBoolean, RHHiddenNodes, SaveImage, SetNode, SimpleMath+, Text Concatenate, VAEDecode, VAELoader, easy seed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima风格动漫-画师转绘_2074192226405675009.json, 图片生成/图生图/画师转绘风格化｜Anima风格动漫图生图直出_2090877696929787906.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_554

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Anima风格动漫-画师转绘_2074192226405675009.json、图片生成/图生图/画师转绘风格化｜Anima风格动漫图生图直出_2090877696929787906.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `AnimaArtistStyleT8`
- `AnimaBoosterLoader`
- `AnimaGelbooruStyleT8`
- `AnimaLLLiteApply`
- `AnimaPromptCombinerT8`
- `AnimaPromptT8`
- `AnimaTeaCache`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitchKJ`
- `Load Lora`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveBoolean`
- `RHHiddenNodes`
- `SaveImage`
- `SetNode`
- `SimpleMath+`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 50% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 552 | - | 2 | 14% |
| 高度 | 552 | - | 2 | 14% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
