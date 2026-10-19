---
name: unknown_workflow_video_sampler_clip_83
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.93
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1925841932033937410.json, 视频生成/图生视频/1935900536141246465.json, 视频生成/图生视频/1934825065211207682.json, 视频生成/图生视频/1930296674030141442.json, 视频生成/图生视频/1986047852856168450.json, 视频生成/图生视频/2025778542893604865.json, 视频生成/文生视频/1957967397764349953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1925841932033937410.json、视频生成/图生视频/1935900536141246465.json、视频生成/图生视频/1934825065211207682.json、视频生成/图生视频/1930296674030141442.json、视频生成/图生视频/1986047852856168450.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 5/7 个有
- `RIFE VFI` —— 3/7 个有
- `ConstrainImage|pysssss` —— 2/7 个有
- `ImageResize+` —— 2/7 个有
- `WanFirstLastFrameToVideo` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `Label (rgthree)` —— 1/7 个有
- `SaveAnimatedWEBP` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 30 | 7 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 7 | 19% |
| 采样算法 | uni_pc | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，7 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 uni_pc，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
