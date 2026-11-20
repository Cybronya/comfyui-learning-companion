---
name: unknown_workflow_video_lora_sampler_926
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_926

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DisableNoise` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
