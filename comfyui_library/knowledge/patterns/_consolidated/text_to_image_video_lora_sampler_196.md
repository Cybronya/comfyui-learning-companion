---
name: text_to_image_video_lora_sampler_196
type: Text To Image
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DisableNoise, EmptyLatentImage, Image Comparer (rgthree), KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/通义千问+WAN2.2反推图生图_1956263880253210626.json, 图片生成/文生图/Z-image 1K反推出图_1993986224063004673.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_196

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/通义千问+WAN2.2反推图生图_1956263880253210626.json、图片生成/文生图/Z-image 1K反推出图_1993986224063004673.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DisableNoise`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SDXLPromptStyler` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `UltimateSDUpscale` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 50% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
