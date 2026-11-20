---
name: unknown_workflow_sampler_checkpoint_vae_36
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91675
common_nodes: [CLIPVisionEncode, EmptyLatentHunyuan3Dv2, Hunyuan3Dv2Conditioning, ImageOnlyCheckpointLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveGLB, SaveImage, VAEDecodeHunyuan3D, VoxelToMesh]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/混元3D模型_2020705568129818626.json, 平台全量/电商图片生成白模文件 混元2.1_2040691612170326017.json, 平台全量/腾讯混元3D2.1_1966411627480428546.json, 平台全量/腾讯混元图转3d模型_1961408960597311489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_36

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/混元3D模型_2020705568129818626.json、平台全量/电商图片生成白模文件 混元2.1_2040691612170326017.json、平台全量/腾讯混元3D2.1_1966411627480428546.json、平台全量/腾讯混元图转3d模型_1961408960597311489.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionEncode`
- `EmptyLatentHunyuan3Dv2`
- `Hunyuan3Dv2Conditioning`
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveGLB`
- `SaveImage`
- `VAEDecodeHunyuan3D`
- `VoxelToMesh`

**可变部分**（部分 workflow 才有）：
- `VoxelToMeshBasic` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `ImageResize` —— 1/4 个有
- `ImageScale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 4 | 82% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 3584 | 3072 - 8192 | 4 | 54% |
| 高度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，4 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 3584，观测区间 3072 - 8192，4 个样本
- 高度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
