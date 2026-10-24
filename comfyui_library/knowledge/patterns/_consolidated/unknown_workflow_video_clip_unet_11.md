---
name: unknown_workflow_video_clip_unet_11
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.959833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan2.1文生视频工作流（ComfyUI官方版）_1935893378293035010.json, 视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json, 视频生成/文生视频/Wan2.2文生视频工作流_2012090867787501569.json, 视频生成/文生视频/causvid文生视频加速_1923578202491711490.json, 视频生成/文生视频/wan-alpha透明图层工作流_1973317342270722050.json, 视频生成/文生视频/新版 Wan2.2_Lightning_Palingenesis 精品免费课程对应工作流 ____1974007898521120769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/Wan2.1文生视频工作流（ComfyUI官方版）_1935893378293035010.json、视频生成/文生视频/Wan2.2文生视频工作流_2011439259349159938.json、视频生成/文生视频/Wan2.2文生视频工作流_2012090867787501569.json、视频生成/文生视频/causvid文生视频加速_1923578202491711490.json、视频生成/文生视频/wan-alpha透明图层工作流_1973317342270722050.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `TorchCompileModel` —— 2/6 个有
- `KSamplerAdvanced` —— 1/6 个有
- `SavePNGZIP_and_Preview_RGBA_AnimatedWEBP` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 5 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 6 | 12% |
| 采样算法 | uni_pc | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，5 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，6 个样本，取值分散，一致性仅 12%
- 采样算法 最常用 uni_pc，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
