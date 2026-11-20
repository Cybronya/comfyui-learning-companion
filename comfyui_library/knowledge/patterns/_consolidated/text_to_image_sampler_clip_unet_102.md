---
name: text_to_image_sampler_clip_unet_102
type: Text To Image
frequency: 7
level: strong
coverage: 0.923714
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/无损扩图 360度lora工作流_1990199382748393474.json, 图片生成/文生图/1.FLUX1 文生图工作流_2043903853527048193.json, 图片生成/文生图/FLUX + LoRA 文生图工作流_2087432058120523777.json, 图片生成/文生图/FLUX + 加速LoRA 文生图工作流_2039621959402659841.json, 图片生成/文生图/Kontext 功能大全-(卷心菜YA )_1942874687296704513.json, 图片生成/文生图/喜剧复古动漫风格2.0_1942404910103080961.json, 视频生成/图生视频/kontext 360度lora工作流_1947265490784784385.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_102

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/无损扩图 360度lora工作流_1990199382748393474.json、图片生成/文生图/1.FLUX1 文生图工作流_2043903853527048193.json、图片生成/文生图/FLUX + LoRA 文生图工作流_2087432058120523777.json、图片生成/文生图/FLUX + 加速LoRA 文生图工作流_2039621959402659841.json、图片生成/文生图/Kontext 功能大全-(卷心菜YA )_1942874687296704513.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `FluxKontextImageScale` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `Kontext Inpainting Conditioning` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 7 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1504 | 768 - 1536 | 7 | 76% |
| 高度 | 1000 | 768 - 1504 | 7 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1504，观测区间 768 - 1536，7 个样本
- 高度 中位数 1000，观测区间 768 - 1504，7 个样本
