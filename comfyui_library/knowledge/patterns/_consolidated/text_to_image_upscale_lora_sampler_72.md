---
name: text_to_image_upscale_lora_sampler_72
type: Text To Image
frequency: 4
level: strong
coverage: 0.9065
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleBy, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, StringConstantMultiline, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy clearCacheAll, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537.json, 图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109760924293881857.json, 图片生成/文生图/Qwen2.1文生图带提示词增强高清放大精干版，数字人文生图方案_2103559733838962690.json, 图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109345585735233537.json、图片生成/文生图/Qwen2.1文生图工作流带提示词增强加seedvr2放大 高质量画面直出_2109760924293881857.json、图片生成/文生图/Qwen2.1文生图带提示词增强高清放大精干版，数字人文生图方案_2103559733838962690.json、图片生成/文生图/Qwen2.1文生图带提示词增强｜SeedVR2放大加持｜清晰度直接拉满_2102593214871072769.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `StringConstantMultiline`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy clearCacheAll`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `easy int` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `QwenImage21BlockCacheT8` —— 2/4 个有
- `QwenImage21Cache` —— 2/4 个有
- `QwenImage21SageAttentionT8` —— 2/4 个有
- `QwenImage21SpectrumT8` —— 2/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
