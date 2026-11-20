---
name: unknown_workflow_sampler_unet_vae_129
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8234
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageScaleToTotalPixels, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/video_minimax_h3_i2v_2087451619603603457.json, 视频生成/图生视频/video_minimax_h3_i2v_RH_2096548199573049346.json, 视频生成/图生视频/video_minimax_h3_i2v_fast_2085261516613443585.json, 视频生成/图生视频/【开源】minimax_h3 图生视频_2084171369004232706.json, 视频生成/图生视频/【老金驿站】MinimaxH3超级加速40%i2v工作流_2087177800716476417.json, 视频生成/图生视频/【老金驿站】MinimaxH3首尾帧视频工作流_2084263524121014274.json, 视频生成/图生视频/海螺图生视频_2085524828332843010.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json, 视频生成/文生视频/Fasth3图生视频_2100129417984036866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_129

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_i2v_2087451619603603457.json、视频生成/图生视频/video_minimax_h3_i2v_RH_2096548199573049346.json、视频生成/图生视频/video_minimax_h3_i2v_fast_2085261516613443585.json、视频生成/图生视频/【开源】minimax_h3 图生视频_2084171369004232706.json、视频生成/图生视频/【老金驿站】MinimaxH3超级加速40%i2v工作流_2087177800716476417.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `GetImageSize` —— 8/10 个有
- `CreateVideo` —— 7/10 个有
- `SaveVideo` —— 7/10 个有
- `PathchSageAttentionKJ` —— 4/10 个有
- `EasyCache` —— 3/10 个有
- `SolAttnPatch` —— 3/10 个有
- `VHS_VideoCombine` —— 3/10 个有
- `JjkText` —— 2/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `BlockSparseAttention` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `MiniMaxH3TurboLoRA` —— 1/10 个有
- `Text` —— 1/10 个有
- `YK_LoadImageFromURL` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
