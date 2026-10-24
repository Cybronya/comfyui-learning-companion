---
name: unknown_workflow_video_sampler_clip_212
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.561333
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json, 视频生成/文生视频/Work-Fisher_Qwen3VL-视频反推+文生视频_1982353695629295618.json, 视频生成/文生视频/视频反推+文生视频_2005214263658643458.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_212

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json、视频生成/文生视频/Work-Fisher_Qwen3VL-视频反推+文生视频_1982353695629295618.json、视频生成/文生视频/视频反推+文生视频_2005214263658643458.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `easy showAnything` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | euler_ancestral | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，3 个样本，一致性 100%
