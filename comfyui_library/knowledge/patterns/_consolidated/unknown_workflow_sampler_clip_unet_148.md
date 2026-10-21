---
name: unknown_workflow_sampler_clip_unet_148
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.83725
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1956259506659446786.json, 图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json, 图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json, 图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1956259506659446786.json、图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json、图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json、图片生成/文生图/Z-Image-Turbo with Low VRAM(4-6 GB)_2075074765303410689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `FLS_SamplerV4` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 8 | 8 - 9 | 4 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，4 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
