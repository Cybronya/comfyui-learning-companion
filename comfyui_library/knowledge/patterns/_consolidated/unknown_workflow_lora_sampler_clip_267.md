---
name: unknown_workflow_lora_sampler_clip_267
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.830333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RMBG, SaveGLB, SaveImage, Trellis2LoadModel, Trellis2MeshWithVoxelGenerator, Trellis2PostProcessAndUnWrapAndRasterizer, Trellis2SimplifyMesh, TrimeshToMESH, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634.json, 平台全量/微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914.json, 数字人/数字人/微软开源了TRELLIS.2大模型_2030197787362598913.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_267

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Z-Imager+微软TRELLIS.2大模型 文生3D（可3D打印）！_2003342143911493634.json、平台全量/微软开源了TRELLIS.2大模型：可用于生产游戏3D模型，同时支持3D打印🎮！_2002627938883366914.json、数字人/数字人/微软开源了TRELLIS.2大模型_2030197787362598913.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RMBG`
- `SaveGLB`
- `SaveImage`
- `Trellis2LoadModel`
- `Trellis2MeshWithVoxelGenerator`
- `Trellis2PostProcessAndUnWrapAndRasterizer`
- `Trellis2SimplifyMesh`
- `TrimeshToMESH`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 1/3 个有
- `Preview3D` —— 1/3 个有
- `Trellis2ExportMesh` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
