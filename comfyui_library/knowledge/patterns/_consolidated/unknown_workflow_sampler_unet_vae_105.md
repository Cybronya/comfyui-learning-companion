---
name: unknown_workflow_sampler_unet_vae_105
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.907857
common_nodes: [DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json, 图片生成/文生图/00.flux生成脸模_许老师专用_1976289488496402434.json, 图片生成/文生图/05.Flux_LoRA_文生图工作流_1993297427371327490.json, 图片生成/文生图/1910297443941187586.json, 图片生成/文生图/1926584319706566658.json, 图片生成/文生图/1975059574103347202.json, 图片生成/文生图/1981703392366084098.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_105

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json、图片生成/文生图/00.flux生成脸模_许老师专用_1976289488496402434.json、图片生成/文生图/05.Flux_LoRA_文生图工作流_1993297427371327490.json、图片生成/文生图/1910297443941187586.json、图片生成/文生图/1926584319706566658.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `CLIPTextEncode` —— 4/7 个有
- `FluxGuidance` —— 4/7 个有
- `RH_Translator` —— 4/7 个有
- `CLIPTextEncodeFlux` —— 3/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `UpscaleModelLoader` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `TeaCache` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `EmptyLatentImage` —— 1/7 个有
- `ModelMergeFlux1` —— 1/7 个有
- `SaveLatent` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 7 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 7 | 5% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 43% |
| 重绘幅度 | 1 | 0.25 - 1 | 7 | 57% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，7 个样本，取值分散，一致性仅 5%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，7 个样本
