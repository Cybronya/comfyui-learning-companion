---
name: image_to_image_lora_sampler_vae_21
type: Image To Image
frequency: 3
level: strong
coverage: 0.433
common_nodes: [Any Switch (rgthree), CFGNorm, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键角色卡V2，无惧肩宽_1986954034261200897.json, 图片生成/图生图/一键角色卡_1978318250926858242.json, 图片生成/文生图/qwen多视角生成图片_2001986168365412353.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键角色卡V2，无惧肩宽_1986954034261200897.json、图片生成/图生图/一键角色卡_1978318250926858242.json、图片生成/文生图/qwen多视角生成图片_2001986168365412353.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：43%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `easy bookmark` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有
- `孤海图像裁剪按比例` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 600 | 480 - 720 | 3 | 84% |
| 高度 | 1024 | 832 - 1200 | 3 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 37/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 600，观测区间 480 - 720，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 832 - 1200，3 个样本，取值集中（一致性 85%）
- 高发问题（37/3 个样本）：Steps较低可能导致细节不足
