---
name: unknown_workflow_sampler_clip_unet_264
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9818
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json, 图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json, 图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json, 图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json, 视频生成/图生视频/wan2.2-5B图生视频女人飞走_1951274276659867650.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_264

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/wan2.2-ti2v-5B图生图_1952197317170548738.json、图片生成/文生图/RH-PSAPI插件用-文生图_2068260936263233538.json、图片生成/文生图/image_z_image_turbo文生图_2085969344235917313.json、图片生成/文生图/wan2.2-ti2v-5B文生图_1951273402428502018.json、视频生成/图生视频/wan2.2-5B图生视频女人飞走_1951274276659867650.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `ModelSamplingSD3` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `Wan22ImageToVideoLatent` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有
- `QwenImageLatentAspectRatio` —— 1/5 个有
- `SDXLEmptyLatentSizePicker+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 30 | 5 | 55% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 5 | 42% |
| 采样算法 | uni_pc | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，5 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 uni_pc，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
