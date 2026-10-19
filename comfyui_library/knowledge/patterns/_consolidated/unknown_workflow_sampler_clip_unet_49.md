---
name: unknown_workflow_sampler_clip_unet_49
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8902
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json, 图片生成/文生图/00.flux生成脸模_许老师专用_1976289488496402434.json, 图片生成/文生图/1909419548767100930.json, 图片生成/文生图/1909435534924460034.json, 图片生成/文生图/1926584319706566658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json、图片生成/文生图/00.flux生成脸模_许老师专用_1976289488496402434.json、图片生成/文生图/1909419548767100930.json、图片生成/文生图/1909435534924460034.json、图片生成/文生图/1926584319706566658.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `EmptyLatentImage` —— 3/5 个有
- `EmptySD3LatentImage` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `TTP_Image_Tile_Batch` —— 2/5 个有
- `FluxGuidance` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `ModelMergeFlux1` —— 1/5 个有
- `SaveLatent` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 35 | 5 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 35，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
