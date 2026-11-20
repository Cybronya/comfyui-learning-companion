---
name: unknown_workflow_upscale_latent_upscale_lora_42
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.823222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/MiniMax_H3 文生、图生、首尾帧视频+二阶高清_2094682363342184449.json, 图片生成/图生图/单图生视频（修改视频）_2108541199018708994.json, 平台全量/MiniMax_H3_全能2k god 版_2092922843293110274.json, 平台全量/vibex使用_H3_参考生视频(提示词优化+二阶高清)_2099570705221373954.json, 视频生成/图生视频/MiniMax_H3 文生、图生、首尾帧视频+二阶高清_2090367048231776258.json, 视频生成/图生视频/MiniMax_H3_参考生视频(提示词优化+二阶高清)_2091043575055343618.json, 视频生成/文生视频/MiniMax_H3_三图身份_INT8_潜空间二阶高清_融合版_2093154699863220225.json, 视频生成/文生视频/minimax_h3_i2v图生视频(4steps turbo加速版)_2087887557345505282.json, 视频生成/文生视频/vibex使用H3 _文生、图生、首尾帧视频+二阶高清_2099477707083046914.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_42

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/MiniMax_H3 文生、图生、首尾帧视频+二阶高清_2094682363342184449.json、图片生成/图生图/单图生视频（修改视频）_2108541199018708994.json、平台全量/MiniMax_H3_全能2k god 版_2092922843293110274.json、平台全量/vibex使用_H3_参考生视频(提示词优化+二阶高清)_2099570705221373954.json、视频生成/图生视频/MiniMax_H3 文生、图生、首尾帧视频+二阶高清_2090367048231776258.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/9 个有
- `MiniMaxChunkFeedForward` —— 8/9 个有
- `MiniMaxLowVRAMAttention` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `PathchSageAttentionKJ` —— 8/9 个有
- `PrimitiveBoolean` —— 8/9 个有
- `SpectrumApplyMiniMaxH3` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `Label (rgthree)` —— 6/9 个有
- `MiniMaxH3ImageToVideo` —— 5/9 个有
- `MiniMaxH3ReferenceToVideo` —— 4/9 个有
- `VHS_LoadVideo` —— 4/9 个有
- `LoadAudio` —— 3/9 个有
- `ImageFromBatch` —— 2/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `ImpactSleep` —— 1/9 个有
- `LazySwitch2way` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `easy positive` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
