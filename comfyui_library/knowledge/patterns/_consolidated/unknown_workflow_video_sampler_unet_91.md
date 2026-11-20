---
name: unknown_workflow_video_sampler_unet_91
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.957
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3AVLatentSeparateT8, MiniMaxH3AudioLatentControlT8, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveLatent, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/人物原声演唱（5秒短镜头）_2107820469721329665.json, 视频生成/图生视频/MV制作｜歌曲片段生成镜头（H3）_2107818505864302593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_91

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/人物原声演唱（5秒短镜头）_2107820469721329665.json、视频生成/图生视频/MV制作｜歌曲片段生成镜头（H3）_2107818505864302593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3AVLatentSeparateT8`
- `MiniMaxH3AudioLatentControlT8`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveLatent`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
