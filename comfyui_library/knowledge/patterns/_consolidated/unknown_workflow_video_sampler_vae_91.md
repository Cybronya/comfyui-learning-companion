---
name: unknown_workflow_video_sampler_vae_91
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.870667
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/video_minimax_h3_i2v_fast_2085261516613443585.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json, 视频生成/文生视频/Minimax_H3文生视频图生视频_2095439213532639234.json, 视频生成/文生视频/minimax_h3_turbo_lora_4步工作流_2085539352125464578.json, 视频生成/文生视频/【MinimaxH3】首尾帧视频-5倍急速版（25→5分钟）_2087187021684101121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_91

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_i2v_fast_2085261516613443585.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json、视频生成/文生视频/Minimax_H3文生视频图生视频_2095439213532639234.json、视频生成/文生视频/minimax_h3_turbo_lora_4步工作流_2085539352125464578.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `BasicGuider` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `SolAttnPatch` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `GetImageSize` —— 3/6 个有
- `ResolutionSelector` —— 3/6 个有
- `CFGGuider` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `DiffusionModelLoaderKJ` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `ModelPreviewOverrideKJ` —— 2/6 个有
- `DisableNoise` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `SpectrumApplyMiniMaxH3` —— 1/6 个有
- `SplitSigmas` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
