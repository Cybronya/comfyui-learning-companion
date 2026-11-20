---
name: image_to_image_sampler_vae_25
type: Image To Image
frequency: 5
level: weak
coverage: 0.877
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen图生图+双节棍 (1)_1963551670277066753.json, 图片生成/图生图/qwen图生图（加速版）_2003497225005219841.json, 图片生成/图生图/人像多角度一致性_2005505501842599938.json, 图片生成/图生图/双截棍nunchaku加速 qwen-image-edit-2509多图编辑工作流_1971005495635021826.json, 图片生成/文生图/人像数据集生成_2073290538132004866.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen图生图+双节棍 (1)_1963551670277066753.json、图片生成/图生图/qwen图生图（加速版）_2003497225005219841.json、图片生成/图生图/人像多角度一致性_2005505501842599938.json、图片生成/图生图/双截棍nunchaku加速 qwen-image-edit-2509多图编辑工作流_1971005495635021826.json、图片生成/文生图/人像数据集生成_2073290538132004866.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `CR Prompt List` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SaveImageKJ` —— 1/5 个有
- `StringConcatenate` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy imageScaleDownToSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 0.5 - 1 | 5 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，5 个样本
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
