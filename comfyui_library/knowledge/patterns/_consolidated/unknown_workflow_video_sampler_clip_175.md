---
name: unknown_workflow_video_sampler_clip_175
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.917333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ImageResizeKJv2, KSamplerSelect, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3单独放大工作流_2086693326912311298.json, 视频生成/文生视频/DG_H3 单采 高清放大_2087776547884331009.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流_2087124477195931649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/H3单独放大工作流_2086693326912311298.json、视频生成/文生视频/DG_H3 单采 高清放大_2087776547884331009.json、视频生成/文生视频/MiniMax H3 导演台全能工作流_2087124477195931649.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
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
- `VHS_LoadVideo` —— 2/3 个有
- `CreateVideo` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `Getter` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `MiniMaxH3Director` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `Setter` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
