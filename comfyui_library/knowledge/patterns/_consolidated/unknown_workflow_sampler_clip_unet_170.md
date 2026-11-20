---
name: unknown_workflow_sampler_clip_unet_170
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.988625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2文生视频工作流_2011408541554315266.json, 图片生成/文生图/wan2.1_t2v1_3B提升本地运行速度_1902941440509382658.json, 图片生成/文生图/wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json, 图片生成/文生图/wan22文生图_1950527410125066242.json, 视频生成/图生视频/Wan2.1+文生视频  高清流畅版_2010908567217381378.json, 视频生成/图生视频/【老金驿站】高清WANt2v高速Magcache生成工作流_1934184638036275202.json, 视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json, 视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_170

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生视频工作流_2011408541554315266.json、图片生成/文生图/wan2.1_t2v1_3B提升本地运行速度_1902941440509382658.json、图片生成/文生图/wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json、图片生成/文生图/wan22文生图_1950527410125066242.json、视频生成/图生视频/Wan2.1+文生视频  高清流畅版_2010908567217381378.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 7/8 个有
- `ModelSamplingSD3` —— 5/8 个有
- `WanVideoTeaCacheKJ` —— 3/8 个有
- `MagCache` —— 1/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `TeaCache` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 4 - 30 | 8 | 65% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 8 | 66% |
| 采样算法 | uni_pc | - | 8 | 38% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 4 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，8 个样本
- 采样算法 最常用 uni_pc，8 个样本，一致性 38%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
