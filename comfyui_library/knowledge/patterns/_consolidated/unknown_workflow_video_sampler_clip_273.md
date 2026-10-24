---
name: unknown_workflow_video_sampler_clip_273
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.876
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerSelect, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/DG_H3 单采 高清放大_2087776547884331009.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2087124477195931649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_273

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/DG_H3 单采 高清放大_2087776547884331009.json、视频生成/文生视频/MiniMax H3 导演台全能工作流_2087124477195931649.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Getter` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `MiniMaxH3Director` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `Setter` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
