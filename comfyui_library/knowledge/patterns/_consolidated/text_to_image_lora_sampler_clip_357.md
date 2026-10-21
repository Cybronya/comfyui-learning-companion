---
name: text_to_image_lora_sampler_clip_357
type: Text To Image
frequency: 2
level: weak
coverage: 0.75
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptyHunyuanLatentVideo, EmptyLatentImage, ImageConcanate, ImpactInt, ImpactSwitch, KSampler, KSamplerAdvanced, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PIP_longsize, PathchSageAttentionKJ, RH_Captioner, RH_LLMAPI_NODE, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, easy seed]
members: [图片生成/文生图/1951336843713433602.json, 图片生成/文生图/1952974633274380290.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_357

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1951336843713433602.json、图片生成/文生图/1952974633274380290.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `EmptyLatentImage`
- `ImageConcanate`
- `ImpactInt`
- `ImpactSwitch`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PIP_longsize`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | bong_tangent | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 bong_tangent，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageReel、LayerUtility: ImageReelComposit、LayerUtility: PurgeVRAM V2、easy seed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
