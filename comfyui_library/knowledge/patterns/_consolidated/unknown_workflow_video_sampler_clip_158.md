---
name: unknown_workflow_video_sampler_clip_158
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9475
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1_control_官方工作流-优化版_1930315905924808705.json, 视频生成/图生视频/wan2.1_官方工作流_I2V_文生视频_480P_1930296674030141442.json, 视频生成/图生视频/wan2.1图生视频 (分镜转视频剧本)_1986047852856168450.json, 视频生成/图生视频/分镜转视频_2025778542893604865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_158

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.1_control_官方工作流-优化版_1930315905924808705.json、视频生成/图生视频/wan2.1_官方工作流_I2V_文生视频_480P_1930296674030141442.json、视频生成/图生视频/wan2.1图生视频 (分镜转视频剧本)_1986047852856168450.json、视频生成/图生视频/分镜转视频_2025778542893604865.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanImageToVideo` —— 3/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `SaveAnimatedWEBP` —— 2/4 个有
- `easy imageSize` —— 2/4 个有
- `AnimateDiffCombine` —— 1/4 个有
- `CFGZeroStar` —— 1/4 个有
- `WanFunControlToVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 10 - 20 | 4 | 67% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 6 | 4 | 29% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 6，4 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
