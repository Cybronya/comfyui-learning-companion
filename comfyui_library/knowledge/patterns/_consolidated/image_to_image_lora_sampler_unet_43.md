---
name: image_to_image_lora_sampler_unet_43
type: Image To Image
frequency: 12
level: strong
coverage: 0.89325
common_nodes: [CFGNorm, CLIPLoader, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FireRed-Image-Edit-1.0单图编辑发散_2024514345513787393.json, 图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json, 图片生成/文生图/FireRed-Image-Edit-1.0双图编辑_2024517003498754050.json, 图片生成/文生图/Qwen-Edit-2511-拜新年、新年祭、元旦节图生图工作流_2005959009792393217.json, 图片生成/文生图/Qwen-Image-Edit-2511姿态迁移AnyPose_2008535188858478594.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511单图编辑（发散）_2004187516678926338.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511单图编辑（防偏移）_2004187504674828289.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511多图编辑_2004187543652499458.json, 图片生成/文生图/Qwen‑Image‑Edit‑2511骨骼引导编辑_2004190125385019394.json, 图片生成/文生图/增加光影‑2511单图编辑（发散）_2005600964696571906.json, 图片生成/文生图/增加光影‑2511单图编辑（防偏移）_2005600933931352066.json, 图片生成/文生图/增加光影‑2511多图编辑_2005600974947450882.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/FireRed-Image-Edit-1.0单图编辑发散_2024514345513787393.json、图片生成/文生图/FireRed-Image-Edit-1.0单图编辑防偏移_2024514356171509762.json、图片生成/文生图/FireRed-Image-Edit-1.0双图编辑_2024517003498754050.json、图片生成/文生图/Qwen-Edit-2511-拜新年、新年祭、元旦节图生图工作流_2005959009792393217.json、图片生成/文生图/Qwen-Image-Edit-2511姿态迁移AnyPose_2008535188858478594.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 11/12 个有
- `Image Comparer (rgthree)` —— 11/12 个有
- `ImageScaleToTotalPixels` —— 11/12 个有
- `VAEDecodeTiled` —— 11/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 10/12 个有
- `ReferenceLatent` —— 5/12 个有
- `PreviewImage` —— 3/12 个有
- `Seed Generator` —— 3/12 个有
- `String Literal` —— 3/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `SDPoseOODLoader` —— 1/12 个有
- `SDPoseOODProcessor` —— 1/12 个有
- `easy promptList` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 12 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
