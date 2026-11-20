---
name: image_to_image_controlnet_lora_sampler_17
type: Image To Image
frequency: 2
level: weak
coverage: 0.7155
common_nodes: [> Text Replace, AILab_QwenVL, AIO_Preprocessor, AnyIsEmpty, CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Float, GroupSwitcher, Image Comparer (rgthree), ImageResizeKJ, Int, JjkText, KSampler, LoadImage, LoraLoaderModelOnly_Any, ModelPatchLoader, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, QwenImageDiffsynthControlnet, RH_Captioner, RH_Translator, SaveImage, Text Input Switch, Text Multiline, TextPreview, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转写实Z-IMAGE版-弱cos风格_2034710998669594625.json, 图片生成/图生图/动漫转写实Z-IMAGE版cosplay风格_2034610294747566082.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_17

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/动漫转写实Z-IMAGE版-弱cos风格_2034710998669594625.json、图片生成/图生图/动漫转写实Z-IMAGE版cosplay风格_2034610294747566082.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `> Text Replace`
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `AnyIsEmpty`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Float`
- `GroupSwitcher`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `Int`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly_Any`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `RH_Captioner`
- `RH_Translator`
- `SaveImage`
- `Text Input Switch`
- `Text Multiline`
- `TextPreview`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
