---
name: unknown_workflow_sampler_clip_vae_23
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8585
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingSD3, QuadrupleCLIPLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/GGUF-HiDream-i1官方工作流_1930274381468176385.json, 图片生成/文生图/HiDream dev_full Workflow ComfyOrg_1913645697319796738.json, 图片生成/文生图/HiDream dev_full Workflow ComfyOrg_2052662704036429825.json, 图片生成/文生图/HiDream dev文生图工作流_1920089942221848578.json, 图片生成/文生图/HiDream-dev官方工作流_1930275054787969025.json, 图片生成/文生图/HiDream_i1_Full基础工作流_1923682437421780993.json, 图片生成/文生图/HiDream基础工作流_1922468199466487809.json, 图片生成/文生图/Hidream Full + Teacache_1926961584344584194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_23

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/GGUF-HiDream-i1官方工作流_1930274381468176385.json、图片生成/文生图/HiDream dev_full Workflow ComfyOrg_1913645697319796738.json、图片生成/文生图/HiDream dev_full Workflow ComfyOrg_2052662704036429825.json、图片生成/文生图/HiDream dev文生图工作流_1920089942221848578.json、图片生成/文生图/HiDream-dev官方工作流_1930275054787969025.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingSD3`
- `QuadrupleCLIPLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 7/8 个有
- `PreviewImage` —— 2/8 个有
- `CLIPTextEncodeHiDream` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `Primitive string multiline [Crystools]` —— 1/8 个有
- `TeaCache` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 50 | 8 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 8 | 13% |
| 采样算法 | lcm | - | 8 | 75% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，8 个样本，取值分散，一致性仅 13%
- 采样算法 最常用 lcm，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
