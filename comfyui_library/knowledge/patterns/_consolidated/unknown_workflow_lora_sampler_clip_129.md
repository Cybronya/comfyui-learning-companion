---
name: unknown_workflow_lora_sampler_clip_129
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.75275
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/26.tonnie-Qwen局部重绘（改中文）_1998076860787490818.json, 图片生成/图生图/29.tonnie-wan2.2最强修手_2001777953891577858.json, 图片生成/图生图/FusionX 稳定修手_1947821442744336385.json, 图片生成/图生图/Klein文生图CG动漫风格（修手）_2043430633757741058.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/26.tonnie-Qwen局部重绘（改中文）_1998076860787490818.json、图片生成/图生图/29.tonnie-wan2.2最强修手_2001777953891577858.json、图片生成/图生图/FusionX 稳定修手_1947821442744336385.json、图片生成/图生图/Klein文生图CG动漫风格（修手）_2043430633757741058.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ColorCorrect` —— 1/4 个有
- `ImageAndMaskPreview` —— 1/4 个有
- `Kontext Inpainting Conditioning` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 4 | 66% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 3.5 | 4 | 47% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.475 | 0.2 - 1 | 4 | 39% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.475，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 39%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
