---
name: unknown_workflow_video_sampler_clip_177
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/【老金驿站】Wan2.1文生视频CFGZeroStar加强版_1907228226127847425.json, 视频生成/文生视频/万相-Wan2.1 文生视频_1901967053463379970.json, 视频生成/文生视频/万相wan2.1 文生视频 官方版工作流_1895270735554412545.json, 视频生成/文生视频/文生视频WAN2.1_1916378048227381249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/【老金驿站】Wan2.1文生视频CFGZeroStar加强版_1907228226127847425.json、视频生成/文生视频/万相-Wan2.1 文生视频_1901967053463379970.json、视频生成/文生视频/万相wan2.1 文生视频 官方版工作流_1895270735554412545.json、视频生成/文生视频/文生视频WAN2.1_1916378048227381249.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 1/4 个有
- `CLIPLoaderGGUF` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `SaveAnimatedWEBP` —— 1/4 个有
- `TextInput_` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 4 | 84% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
