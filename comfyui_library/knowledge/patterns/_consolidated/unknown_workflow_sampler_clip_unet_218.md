---
name: unknown_workflow_sampler_clip_unet_218
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.895
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/表情包 一键生成表情包_1941876274459787265.json, 图片生成/文生图/05.Flux_LoRA_文生图工作流_1993297427371327490.json, 图片生成/文生图/07.Flux_文生图_1993297490357190657.json, 图片生成/文生图/Flux+LoRA的文生图基础工作流_2001894494809276417.json, 图片生成/文生图/SRPO+SDXL  二重采样人物细节增强方案（文生图）_1975059574103347202.json, 图片生成/文生图/SRPO-flux文生图_1981703392366084098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_218

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/表情包 一键生成表情包_1941876274459787265.json、图片生成/文生图/05.Flux_LoRA_文生图工作流_1993297427371327490.json、图片生成/文生图/07.Flux_文生图_1993297490357190657.json、图片生成/文生图/Flux+LoRA的文生图基础工作流_2001894494809276417.json、图片生成/文生图/SRPO+SDXL  二重采样人物细节增强方案（文生图）_1975059574103347202.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `ImageUpscaleWithModel` —— 3/6 个有
- `UpscaleModelLoader` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ImageScaleBy` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `TeaCache` —— 2/6 个有
- `VAEEncode` —— 2/6 个有
- `DualCLIPLoaderGGUF` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 6 | 1% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 0.25 - 1 | 6 | 53% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，6 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，6 个样本
