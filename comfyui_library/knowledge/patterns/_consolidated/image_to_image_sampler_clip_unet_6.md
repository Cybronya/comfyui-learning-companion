---
name: image_to_image_sampler_clip_unet_6
type: Image To Image
frequency: 2
level: weak
coverage: 0.7805
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImpactSwitch, KSampler, LoadImage, PreviewImage, RH_Captioner, RH_Translator, ReferenceLatent, RepeatLatentBatch, SaveImage, ShowText|pysssss, TTP_text_mix, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [Primitive integer [Crystools], CR Text Concatenate, Mask Fill Holes]
members: [图片生成/图生图/1938785222286565378.json, 图片生成/图生图/1940597087887323137.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/1938785222286565378.json、图片生成/图生图/1940597087887323137.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner`
- `RH_Translator`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_text_mix`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `LoadAndResizeImage` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `Seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Primitive integer [Crystools]、CR Text Concatenate、Mask Fill Holes
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
