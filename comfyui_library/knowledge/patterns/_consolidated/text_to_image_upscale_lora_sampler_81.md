---
name: text_to_image_upscale_lora_sampler_81
type: Text To Image
frequency: 3
level: strong
coverage: 0.844
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, FluxKontextImageScale, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, Text, TextEncodeQwenImageEditPlus, UnetLoaderGGUF, UpscaleModelLoader, VAEDecode, VAEEncodeTiled, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit Plus编辑（2511加速工作流）_2004400909193019393.json, 图片生成/文生图/Qwen Edit Plus 编辑+多图+放大（2511加速工作流）_2007661504455249921.json, 图片生成/文生图/Qwen Edit Plus编辑+多图+放大_1981990179764346882.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Edit Plus编辑（2511加速工作流）_2004400909193019393.json、图片生成/文生图/Qwen Edit Plus 编辑+多图+放大（2511加速工作流）_2007661504455249921.json、图片生成/文生图/Qwen Edit Plus编辑+多图+放大_1981990179764346882.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxKontextImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UnetLoaderGGUF`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 8 | 3 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 3 | 57% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，3 个样本
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
