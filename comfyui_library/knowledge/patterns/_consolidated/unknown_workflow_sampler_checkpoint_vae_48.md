---
name: unknown_workflow_sampler_checkpoint_vae_48
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.894333
common_nodes: [CLIPVisionEncode, EmptyLatentHunyuan3Dv2, Hunyuan3Dv2Conditioning, ImageOnlyCheckpointLoader, ImageResizeKJv2, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageRemoveAlpha, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveGLB, VAEDecodeHunyuan3D, VoxelToMesh, easy imageSizeBySide]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/图片生成3D模型 混元3d2.1_1971470368882016257.json, 平台全量/模型3D-图片生成3D模型-混元3d-2.1_2051860245256916993.json, 平台全量/混元模型 图片生成3D模型_2033442637734219778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_48

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图片生成3D模型 混元3d2.1_1971470368882016257.json、平台全量/模型3D-图片生成3D模型-混元3d-2.1_2051860245256916993.json、平台全量/混元模型 图片生成3D模型_2033442637734219778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2`
- `Hunyuan3Dv2Conditioning`
- `ImageOnlyCheckpointLoader`
- `ImageResizeKJv2`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveGLB`
- `VAEDecodeHunyuan3D`
- `VoxelToMesh`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 2/3 个有
- `easy int` —— 1/3 个有
- `easy saveText` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 35 | 3 | 72% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 3 | 94% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 3000 | 3000 - 3000 | 3 | 100% |
| 高度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 35，3 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 3000，观测区间 3000 - 3000，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
