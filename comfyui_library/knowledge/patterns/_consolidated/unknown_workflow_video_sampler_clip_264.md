---
name: unknown_workflow_video_sampler_clip_264
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyHunyuanLatentVideo, FluxGuidance, KSamplerSelect, ModelSamplingSD3, RandomNoise, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/1901602052710244354.json, 视频生成/文生视频/1870307237162815489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1901602052710244354.json、视频生成/文生视频/1870307237162815489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `StringConstantMultiline` —— 1/2 个有
- `TeaCacheHunyuanVideoSampler` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
