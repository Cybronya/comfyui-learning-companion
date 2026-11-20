---
name: unknown_workflow_sampler_clip_unet_258
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.909333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json, 图片生成/文生图/Flux3_Klein图像编辑工作流_2111476889922662402.json, 图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json, 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json, 平台全量/FLUX 3 图像编辑_2114204084717842433.json, 视频生成/图生视频/wan2.2-5B图生视频女人飞走_1951274276659867650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_258

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json、图片生成/文生图/Flux3_Klein图像编辑工作流_2111476889922662402.json、图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json、图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json、平台全量/FLUX 3 图像编辑_2114204084717842433.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `ModelSamplingSD3` —— 3/6 个有
- `VHS_VideoCombine` —— 3/6 个有
- `Wan22ImageToVideoLatent` —— 3/6 个有
- `ReferenceMultiLatent` —— 2/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `QwenImageLatentAspectRatio` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 23 | 4 - 30 | 6 | 53% |
| Prompt 约束强度(CFG) | 3 | 1 - 5 | 6 | 33% |
| 采样算法 | uni_pc | - | 6 | 50% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 23，观测区间 4 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 5，6 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 uni_pc，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
