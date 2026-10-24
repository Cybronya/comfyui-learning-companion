---
name: image_to_image_lora_sampler_unet_55
type: Image To Image
frequency: 11
level: strong
coverage: 0.883545
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, GetImageSize+, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FireRed-Image-Edit-1.0单图编辑发散_2024514345513787393.json, 图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json, 图片生成/文生图/FireRed-Image-Edit-1.0双图编辑_2024517003498754050.json, 图片生成/文生图/Qwen-Image-Edit-2511姿态迁移AnyPose_2008535188858478594.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511单图编辑（发散）_2004187516678926338.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511单图编辑（防偏移）_2004187504674828289.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511多图编辑_2004187543652499458.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511骨骼引导编辑_2004190125385019394.json, 图片生成/文生图/增加光影‑2511单图编辑（发散）_2005600964696571906.json, 图片生成/文生图/增加光影‑2511单图编辑（防偏移）_2005600933931352066.json, 图片生成/文生图/增加光影‑2511多图编辑_2005600974947450882.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_55

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/FireRed-Image-Edit-1.0单图编辑发散_2024514345513787393.json、图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json、图片生成/文生图/FireRed-Image-Edit-1.0双图编辑_2024517003498754050.json、图片生成/文生图/Qwen-Image-Edit-2511姿态迁移AnyPose_2008535188858478594.json、图片生成/文生图/Qwen‑Image‑Edit‑2511单图编辑（发散）_2004187516678926338.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 9/11 个有
- `ReferenceLatent` —— 4/11 个有
- `PreviewImage` —— 3/11 个有
- `Seed Generator` —— 3/11 个有
- `String Literal` —— 3/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `SDPoseOODLoader` —— 1/11 个有
- `SDPoseOODProcessor` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
