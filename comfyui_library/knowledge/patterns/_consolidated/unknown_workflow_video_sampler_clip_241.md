---
name: unknown_workflow_video_sampler_clip_241
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 smooth mix图生视频_1997495774311288833.json, 视频生成/图生视频/首尾帧生视频（解禁模型）：Wan2.2 Remix_2053411602111709186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_241

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 smooth mix图生视频_1997495774311288833.json、视频生成/图生视频/首尾帧生视频（解禁模型）：Wan2.2 Remix_2053411602111709186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `wanBlock_Swap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 50% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 80% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler_ancestral | - | 2 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，2 个样本，一致性 50%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
