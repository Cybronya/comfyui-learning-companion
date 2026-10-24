---
name: image_to_image_sampler_clip_unet_76
type: Image To Image
frequency: 6
level: moderate
coverage: 0.814
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, INTConstant, ImageScaleDownToSize, ImageScaleToTotalPixels, ImageSharpen, KSampler, KSamplerSelect, LayerFilter: Sharp & Soft, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingAuraFlow, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z image base 3合1 高清放大+文生图+图生图  满血版 反推出图 极致真实，抖音小红书_2039575881663909890.json, 图片生成/图生图/zimage+klein图像反推生图+高清放大_2037440968860897282.json, 图片生成/文生图/3合1=高清放大+文生图生图=Z image base！B站艾橘溪_2036421892235595778.json, 图片生成/文生图/Z image base三合一：文生图+图生图+高清放大_2036692926176169986.json, 图片生成/文生图/文生图+图生图+高清放大=Z image base三合一！_2036695524622995457.json, 图片生成/文生图/高清放大+文生图+图生图 Z image base 3合1   满血版 反推出图 极致真实，抖音小红_2039588818780688386.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_76

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z image base 3合1 高清放大+文生图+图生图  满血版 反推出图 极致真实，抖音小红书_2039575881663909890.json、图片生成/图生图/zimage+klein图像反推生图+高清放大_2037440968860897282.json、图片生成/文生图/3合1=高清放大+文生图生图=Z image base！B站艾橘溪_2036421892235595778.json、图片生成/文生图/Z image base三合一：文生图+图生图+高清放大_2036692926176169986.json、图片生成/文生图/文生图+图生图+高清放大=Z image base三合一！_2036695524622995457.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `INTConstant`
- `ImageScaleDownToSize`
- `ImageScaleToTotalPixels`
- `ImageSharpen`
- `KSampler`
- `KSamplerSelect`
- `LayerFilter: Sharp & Soft`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `JjkText` —— 5/6 个有
- `LayerUtility: BooleanOperator` —— 5/6 个有
- `LayerUtility: If ` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `BasicScheduler` —— 4/6 个有
- `PreviewAny` —— 4/6 个有
- `llama_cpp_instruct_adv` —— 4/6 个有
- `llama_cpp_model_loader` —— 4/6 个有
- `EmptyFlux2LatentImage` —— 2/6 个有
- `Flux2Scheduler` —— 2/6 个有
- `GetImageSize+` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `TextGenerateLTX2Prompt` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 44 | 10 - 50 | 6 | 66% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 6 | 72% |
| 采样算法 | res_multistep | - | 6 | 83% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 44，观测区间 10 - 50，6 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，6 个样本
- 采样算法 最常用 res_multistep，6 个样本，一致性 83%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
