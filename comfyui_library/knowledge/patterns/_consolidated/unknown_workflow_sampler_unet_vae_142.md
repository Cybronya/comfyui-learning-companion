---
name: unknown_workflow_sampler_unet_vae_142
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.814625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json, 视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json, 视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V2_2084645452783382530.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084908134719643649.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084998635074445314.json, 视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2085402316232019969.json, 视频生成/文生视频/DG_H3 文生视频 BF16高质量_2085624042417123330.json, 视频生成/文生视频/MiniMax H3 lightx2v 4步加速图生视频工作流_2086324212742049794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_142

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2085731924324216833.json、视频生成/图生视频/电商尾帧生视频  minimax h3 加速版_2087164469729386498.json、视频生成/文生视频/(2倍速！量化加速版)Minimax文生视频V2_2084645452783382530.json、视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084908134719643649.json、视频生成/文生视频/(768P)Minimax文生视频BF16高质量加速版V2_2084998635074445314.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/8 个有
- `SaveVideo` —— 6/8 个有
- `CR Prompt Text` —— 5/8 个有
- `EasyCache` —— 4/8 个有
- `MiniMaxH3BlockCacheT8` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `JjkText` —— 2/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `SolAttnPatch` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `MiniMaxH3AVDecodeT8` —— 1/8 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/8 个有
- `SpectrumSDXL` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
