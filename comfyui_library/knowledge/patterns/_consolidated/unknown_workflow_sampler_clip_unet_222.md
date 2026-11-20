---
name: unknown_workflow_sampler_clip_unet_222
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.893429
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/003.FLUX.2智能综合001.lora文生图_2035170208612098050.json, 图片生成/文生图/2031285736095358978.json, 图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json, 图片生成/文生图/EDGE OF QWEN文生图工作流_1957357556198993922.json, 图片生成/文生图/ERNIE 满血版+Turbo版两条工作流，百度大模型_2055111279836180481.json, 图片生成/文生图/FLSampler (BSS) 画质提升-ZImage_2062006258563108866.json, 图片生成/文生图/Qwen-image局部重绘_1956259506659446786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_222

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/003.FLUX.2智能综合001.lora文生图_2035170208612098050.json、图片生成/文生图/2031285736095358978.json、图片生成/文生图/ComfyUI Z-Image-Turbo工作流详解｜8步照片级出图+中英文文字渲染+全节点注释_2059594391173554177.json、图片生成/文生图/EDGE OF QWEN文生图工作流_1957357556198993922.json、图片生成/文生图/ERNIE 满血版+Turbo版两条工作流，百度大模型_2055111279836180481.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `LoadImage` —— 4/7 个有
- `EmptyFlux2LatentImage` —— 3/7 个有
- `EmptySD3LatentImage` —— 3/7 个有
- `ModelSamplingAuraFlow` —— 3/7 个有
- `LoraLoader` —— 2/7 个有
- `FLS_SamplerV4` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 8 | 4 - 50 | 7 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 30% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 50，7 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 30%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
