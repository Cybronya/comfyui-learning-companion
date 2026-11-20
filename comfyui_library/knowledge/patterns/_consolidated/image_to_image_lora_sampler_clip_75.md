---
name: image_to_image_lora_sampler_clip_75
type: Image To Image
frequency: 4
level: strong
coverage: 0.923
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转真实V2 - Qwen-edit+Flux2-Klein 双采样_2029160705575882754.json, 图片生成/图生图/动漫转真实V2_极致真实_Qwen-edit+Flux2-Klein 双采样_2019762691333693441.json, 图片生成/图生图/动漫转真实V3 Boogu_edit 采样&微调_2077168741405777922.json, 数字人/数字人/动漫转真实V2_极致真实_Qwen-edit+Flux2-Klein 双采样_2056040703163150338.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/动漫转真实V2 - Qwen-edit+Flux2-Klein 双采样_2029160705575882754.json、图片生成/图生图/动漫转真实V2_极致真实_Qwen-edit+Flux2-Klein 双采样_2019762691333693441.json、图片生成/图生图/动漫转真实V3 Boogu_edit 采样&微调_2077168741405777922.json、数字人/数字人/动漫转真实V2_极致真实_Qwen-edit+Flux2-Klein 双采样_2056040703163150338.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `CR Image Input Switch` —— 3/4 个有
- `ImageColorMatch+` —— 3/4 个有
- `ImageSharpen` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `workflow>自定义采样器` —— 3/4 个有
- `1hew_ImageToURL` —— 1/4 个有
- `TT_img_enc_v2` —— 1/4 个有
- `TextEncodeBooguEdit` —— 1/4 个有
- `easy imageColorMatch` —— 1/4 个有
- `easy saveText` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `workflow>自定义采样` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
