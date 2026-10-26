---
name: unknown_workflow_video_sampler_vae_200
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9075
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DiffusionModelLoaderKJ, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, Label (rgthree), RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881.json, 视频生成/文生视频/LTX2.3 数字人 导演台分镜（新版）_2070676408346693633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_200

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX 2.5 Director 2.0 导演台视频生成工作流_2092109248682618881.json、视频生成/文生视频/LTX2.3 数字人 导演台分镜（新版）_2070676408346693633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
