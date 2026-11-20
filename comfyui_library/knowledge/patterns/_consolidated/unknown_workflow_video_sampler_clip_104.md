---
name: unknown_workflow_video_sampler_clip_104
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.509333
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, wanBlockSwap]
problems: []
missing: []
members: [图片生成/反推提示词/Qwen3VL-视频反推+文生视频_2008494658141294593.json, 图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json, 图片生成/文生图/文生视频Smootht2v+Qwen3VL反推+_2002512116349300738.json, 视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json, 视频生成/文生视频/Work-Fisher_Qwen3VL-视频反推+文生视频_1982353695629295618.json, 视频生成/文生视频/视频反推+文生视频_2005214263658643458.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/Qwen3VL-视频反推+文生视频_2008494658141294593.json、图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json、图片生成/文生图/文生视频Smootht2v+Qwen3VL反推+_2002512116349300738.json、视频生成/文生视频/Wan2.2_Smooth Mix 文生视频_2049482366405582849.json、视频生成/文生视频/Work-Fisher_Qwen3VL-视频反推+文生视频_1982353695629295618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `RIFE VFI` —— 5/6 个有
- `AILab_QwenVL` —— 4/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | 1 | 1 - 1 | 6 | 100% |
| 重绘幅度 | euler_ancestral | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，6 个样本，一致性 100%
