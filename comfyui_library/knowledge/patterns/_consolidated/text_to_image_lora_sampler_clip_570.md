---
name: text_to_image_lora_sampler_clip_570
type: Text To Image
frequency: 3
level: moderate
coverage: 0.916667
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, FastGroupsBypassSwitch, ImageScaleToTotalPixels, JWFloat, KSampler, KSamplerAdvanced, LatentSwitch, LoraLoaderModelOnly, PreviewAny, PreviewImage, PrimitiveStringMultiline, RH_LLMAPI_NODE, ReferenceLatent, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/巨构Krea2+Klein组合｜高清急速数字人文生图双开_2103060942782296065.json, 图片生成/文生图/巨构！ Krea2+Klein高清！ 急速！_2102715333214818306.json, 图片生成/文生图/巨物构图 Krea2+Klein高清_2102610143589523457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_570

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/巨构Krea2+Klein组合｜高清急速数字人文生图双开_2103060942782296065.json、图片生成/文生图/巨构！ Krea2+Klein高清！ 急速！_2102715333214818306.json、图片生成/文生图/巨物构图 Krea2+Klein高清_2102610143589523457.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FastGroupsBypassSwitch`
- `ImageScaleToTotalPixels`
- `JWFloat`
- `KSampler`
- `KSamplerAdvanced`
- `LatentSwitch`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1024 | 80 - 1024 | 3 | 37% |
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4.5 | 3 | 94% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4.5，3 个样本，取值集中（一致性 94%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 高发问题（10/3 个样本）：Steps较低可能导致细节不足
