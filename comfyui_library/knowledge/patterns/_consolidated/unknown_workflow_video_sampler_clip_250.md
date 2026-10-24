---
name: unknown_workflow_video_sampler_clip_250
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CM_IntToFloat, INTConstant, KSampler, MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1-i2v-720p-图生视频-官方版_1914866283652022273.json, 视频生成/文生视频/wan2.1-t2v-720p-文生视频-官方版-加智能配音_1914847426837184514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_250

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan2.1-i2v-720p-图生视频-官方版_1914866283652022273.json、视频生成/文生视频/wan2.1-t2v-720p-文生视频-官方版-加智能配音_1914847426837184514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `INTConstant`
- `KSampler`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
