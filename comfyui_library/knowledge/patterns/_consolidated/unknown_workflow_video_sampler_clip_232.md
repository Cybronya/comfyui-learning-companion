---
name: unknown_workflow_video_sampler_clip_232
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.961
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConfigureModifiedWan, DisableNoise, ImageConcanate, ImageScale, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanFetaEnhance, WanFlowEditGuiderCFGAdv, WanFlowEditSampler, WanReverseModelSamplingPred]
problems: []
missing: []
members: [平台全量/Wan2.1视频编辑_1897279382044495874.json, 平台全量/万相2.1 Flowedit+vid2vid视频转绘编辑工作流_1895725377748860930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_232

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Wan2.1视频编辑_1897279382044495874.json、平台全量/万相2.1 Flowedit+vid2vid视频转绘编辑工作流_1895725377748860930.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConfigureModifiedWan`
- `DisableNoise`
- `ImageConcanate`
- `ImageScale`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanFetaEnhance`
- `WanFlowEditGuiderCFGAdv`
- `WanFlowEditSampler`
- `WanReverseModelSamplingPred`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `WanVideoDecode` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoModelLoader` —— 1/2 个有
- `WanVideoSampler` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoVAELoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
