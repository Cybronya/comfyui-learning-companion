---
name: text_to_image_lora_sampler_clip_648
type: Text To Image
frequency: 2
level: weak
coverage: 0.783
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, EmptyHunyuanLatentVideo, EmptyLatentImage, EmptySD3LatentImage, FilmGrain, KSampler, KSamplerSelect, LayerColor: Brightness & Contrast, LoadImage, LoraLoader, ModelSamplingAuraFlow, ModelSamplingSD3, PreviewImage, PrimitiveInt, RH_Jimeng4_Image2Image, RH_Nano_Banana_Image2Image, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, String, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图+图生图课堂教学_1999847196843536385.json, 图片生成/文生图/文生图大集合_1970102000228704258.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_648

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/文生图+图生图课堂教学_1999847196843536385.json、图片生成/文生图/文生图大集合_1970102000228704258.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `FilmGrain`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `RH_Jimeng4_Image2Image`
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `String`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningCombine` —— 1/2 个有
- `ConditioningSetTimestepRange` —— 1/2 个有
- `FSampler` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `TeaCache` —— 1/2 个有
- `TripleCLIPLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.45 | - | 2 | 100% |
| LoRA 文本强度 | 0.45 | - | 2 | 100% |
| 宽度 | 1152 | - | 2 | 89% |
| 高度 | 1472 | - | 2 | 70% |
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
