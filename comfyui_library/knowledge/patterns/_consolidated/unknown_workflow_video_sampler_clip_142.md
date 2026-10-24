---
name: unknown_workflow_video_sampler_clip_142
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.98225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, PatchModelPatcherOrder, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537.json, 视频生成/图生视频/wan2.1_1.3B_self_forcing 超高速高质量视频生成_1933438103912624130.json, 视频生成/文生视频/wan2.1 sageattension 文生视频基础工作流_1903963257324085250.json, 视频生成/文生视频/wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537.json、视频生成/图生视频/wan2.1_1.3B_self_forcing 超高速高质量视频生成_1933438103912624130.json、视频生成/文生视频/wan2.1 sageattension 文生视频基础工作流_1903963257324085250.json、视频生成/文生视频/wan2.1_1.3B_self_forcing 高质量视频生成极速版_1934951116805185538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 3/4 个有
- `FloatConstant` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `RIFE VFI` —— 3/4 个有
- `Video_Upscale_With_Model` —— 3/4 个有
- `Int` —— 1/4 个有
- `Text Load Line From File` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy batchAnything` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 4 | 29% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 4 | 4% |
| 采样算法 | lcm | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，4 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，4 个样本，取值分散，一致性仅 4%
- 采样算法 最常用 lcm，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
