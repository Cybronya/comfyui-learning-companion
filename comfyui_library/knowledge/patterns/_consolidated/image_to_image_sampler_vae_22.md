---
name: image_to_image_sampler_vae_22
type: Image To Image
frequency: 6
level: strong
coverage: 0.4555
common_nodes: [Any Switch (rgthree), CFGNorm, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键角色卡V2，无惧肩宽_1986954034261200897.json, 图片生成/图生图/一键角色卡_1978318250926858242.json, 图片生成/文生图/qwen多视角生成图片_2001986168365412353.json, 平台全量/人物一致性三视图qwen2509_1999085546028793858.json, 平台全量/人物图生不同姿势全角度_2046536660602589185.json, 数字人/数字人/多角度丨人物角色一致性丨一张图出全角度丨高度一致性丨一致性衍生训练集丨开源稳定！！_1984143610499268609.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键角色卡V2，无惧肩宽_1986954034261200897.json、图片生成/图生图/一键角色卡_1978318250926858242.json、图片生成/文生图/qwen多视角生成图片_2001986168365412353.json、平台全量/人物一致性三视图qwen2509_1999085546028793858.json、平台全量/人物图生不同姿势全角度_2046536660602589185.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `VAELoader` —— 5/6 个有
- `PrimitiveString` —— 4/6 个有
- `easy bookmark` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `CheckpointLoaderSimple` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `Mute / Bypass Relay (rgthree)` —— 2/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/6 个有
- `NunchakuQwenImageDiTLoader` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: CropByMask V2` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有
- `孤海图像裁剪按比例` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 840 | 480 - 960 | 6 | 75% |
| 高度 | 1252 | 832 - 1304 | 6 | 85% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 70/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 840，观测区间 480 - 960，6 个样本
- 高度 中位数 1252，观测区间 832 - 1304，6 个样本，取值集中（一致性 85%）
- 高发问题（70/6 个样本）：Steps较低可能导致细节不足
