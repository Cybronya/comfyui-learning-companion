---
name: text_to_image_lora_sampler_clip_360
type: Text To Image
frequency: 2
level: weak
coverage: 0.8505
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, easy seed]
members: [图片生成/文生图/1954008777874034689.json, 图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_360

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1954008777874034689.json、图片生成/文生图/F.1+ZIT - 极致逼真文生图_2007498725198929922.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 11 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 0.29 | - | 2 | 62% |
| 宽度 | 1152 | - | 2 | 89% |
| 高度 | 1344 | - | 2 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 0.29，样本不足，未给区间，2 个样本
- 宽度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 1344，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、LayerUtility: ImageScaleByAspectRatio V2、easy seed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
