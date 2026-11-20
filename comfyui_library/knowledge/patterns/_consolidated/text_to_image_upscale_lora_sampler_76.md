---
name: text_to_image_upscale_lora_sampler_76
type: Text To Image
frequency: 4
level: strong
coverage: 0.883
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxKontextImageScale, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit Plus编辑（2511加速工作流）_2004400909193019393.json, 图片生成/文生图/Qwen Edit Plus 编辑+多图+放大（2511加速工作流）_2007661504455249921.json, 图片生成/文生图/Qwen Edit Plus编辑+多图+放大_1981990179764346882.json, 平台全量/超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_76

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Edit Plus编辑（2511加速工作流）_2004400909193019393.json、图片生成/文生图/Qwen Edit Plus 编辑+多图+放大（2511加速工作流）_2007661504455249921.json、图片生成/文生图/Qwen Edit Plus编辑+多图+放大_1981990179764346882.json、平台全量/超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Text` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `UltimateSDUpscaleCustomSample` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 8 | 4 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 4 | 63% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 8，4 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，4 个样本
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
