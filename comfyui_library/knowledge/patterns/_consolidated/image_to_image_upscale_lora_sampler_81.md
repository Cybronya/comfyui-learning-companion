---
name: image_to_image_upscale_lora_sampler_81
type: Image To Image
frequency: 3
level: moderate
coverage: 0.884667
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, CLIPTextEncode, FluxKontextImageScale, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text, TextEncodeQwenImageEditPlus, UpscaleModelLoader, VAEDecode, VAEEncode, VAEEncodeTiled, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen+Edit+Plus编辑_1991791597601894401.json, 平台全量/人物角色三视图生成  Qwen_Edit_2509 不同视角高清放大_1997116534558507009.json, 平台全量/角色三视图一键生成-Qwen-edit模型_2039767271060545538.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen+Edit+Plus编辑_1991791597601894401.json、平台全量/人物角色三视图生成  Qwen_Edit_2509 不同视角高清放大_1997116534558507009.json、平台全量/角色三视图一键生成-Qwen-edit模型_2039767271060545538.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `FluxKontextImageScale`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Latent Input Switch JK` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `QwenImageLatentAspectRatio` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.35 | 0.3 - 1 | 3 | 42% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.3 - 1，3 个样本，取值分散，一致性仅 42%
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
