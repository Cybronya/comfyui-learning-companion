---
name: unknown_workflow_video_sampler_unet_58
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8046
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/video_minimax_h3_i2v_fast_2085261516613443585.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json, 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_i2v_fast_2085261516613443585.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json、视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json、视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json、视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
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
- `BasicGuider` —— 3/5 个有
- `EasyCache` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `SolAttnPatch` —— 3/5 个有
- `CFGGuider` —— 2/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `ResolutionSelector` —— 2/5 个有
- `DisableNoise` —— 1/5 个有
- `SplitSigmas` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
