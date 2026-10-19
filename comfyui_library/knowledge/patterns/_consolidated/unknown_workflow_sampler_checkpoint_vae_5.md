---
name: unknown_workflow_sampler_checkpoint_vae_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8676
common_nodes: [CLIPVisionEncode, EmptyLatentHunyuan3Dv2, ImageOnlyCheckpointLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveGLB, VAEDecodeHunyuan3D, VoxelToMesh]
problems: [发现KSampler但没有VAEDecode]
missing: [easy imageRemBg]
members: [comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json, comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json, comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json, comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json, 图片生成/文生图/1966105526599847937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/3d_hunyuan3d-v2.1.json、comfyui-workflow-templates-json/3d_hunyuan3d_image_to_model.json、comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model.json、comfyui-workflow-templates-json/3d_hunyuan3d_multiview_to_model_turbo.json、图片生成/文生图/1966105526599847937.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveGLB`
- `VAEDecodeHunyuan3D`
- `VoxelToMesh`

**可变部分**（部分 workflow 才有）：
- `Hunyuan3Dv2Conditioning` —— 3/5 个有
- `Hunyuan3Dv2ConditioningMultiView` —— 2/5 个有
- `FluxGuidance` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `VoxelToMeshBasic` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 7.5 | 4 - 8 | 5 | 74% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 3072 | 3072 - 8192 | 5 | 54% |
| 高度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 5/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 4 - 8，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 3072，观测区间 3072 - 8192，5 个样本
- 高度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：发现KSampler但没有VAEDecode
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageRemBg
