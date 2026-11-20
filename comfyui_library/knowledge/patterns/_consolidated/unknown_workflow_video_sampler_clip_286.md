---
name: unknown_workflow_video_sampler_clip_286
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResize+, KSampler, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json, 视频生成/文生视频/wan2.1 FusionX 2video_1957967397764349953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_286

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan 2.1 ComfyUI 首尾帧+故事版驱动工作流_1926598014440251394.json、视频生成/文生视频/wan2.1 FusionX 2video_1957967397764349953.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Load Lora` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
