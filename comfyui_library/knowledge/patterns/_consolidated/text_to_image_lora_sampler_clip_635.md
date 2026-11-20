---
name: text_to_image_lora_sampler_clip_635
type: Text To Image
frequency: 2
level: weak
coverage: 0.9085
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Flux2Scheduler, ImageConcanate, ImageScaleToTotalPixels, JWFloat, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913.json, 图片生成/图生图/多图编辑换头｜Flux2Klein写实换脸4B加速版_2090845255133392898.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_635

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913.json、图片生成/图生图/多图编辑换头｜Flux2Klein写实换脸4B加速版_2090845255133392898.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `JWFloat`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Crop Face` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `GetImage` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `Load RetinaFace` —— 1/2 个有
- `MaskColorize` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 580 | - | 2 | 14% |
| 高度 | 1000 | - | 2 | 8% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 50% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 580，样本不足，未给区间，2 个样本，取值分散，一致性仅 14%
- 高度 中位数 1000，样本不足，未给区间，2 个样本，取值分散，一致性仅 8%
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
