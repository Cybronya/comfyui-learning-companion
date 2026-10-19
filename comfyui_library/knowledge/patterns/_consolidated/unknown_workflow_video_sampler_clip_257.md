---
name: unknown_workflow_video_sampler_clip_257
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.389
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, ImageLoader, ImageResizeKJv2, Int, KSamplerAdvanced, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2022797713682735106.json, 视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_257

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2022797713682735106.json、视频生成/文生视频/漫剧最强工具WAN2.2最强首尾帧视频 （高动态）_2047997524845268994.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：39%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageLoader`
- `ImageResizeKJv2`
- `Int`
- `KSamplerAdvanced`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
