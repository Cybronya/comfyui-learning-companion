---
name: unknown_workflow_video_sampler_clip_150
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1914866283652022273.json, 视频生成/图生视频/1896444966992478209.json, 视频生成/图生视频/1895391021444497410.json, 视频生成/文生视频/1914847426837184514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1914866283652022273.json、视频生成/图生视频/1896444966992478209.json、视频生成/图生视频/1895391021444497410.json、视频生成/文生视频/1914847426837184514.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `WanImageToVideo` —— 3/4 个有
- `CM_IntToFloat` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `MMAudioFeatureUtilsLoader` —— 2/4 个有
- `MMAudioModelLoader` —— 2/4 个有
- `MMAudioSampler` —— 2/4 个有
- `easy mathInt` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 1/4 个有
- `ImageResize+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 4 | 65% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 4 | 87% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，4 个样本，取值集中（一致性 87%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
