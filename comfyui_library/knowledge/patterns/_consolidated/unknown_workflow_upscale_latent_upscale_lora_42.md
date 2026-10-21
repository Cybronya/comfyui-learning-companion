---
name: unknown_workflow_upscale_latent_upscale_lora_42
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.832714
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: [easy imageIndexSwitch]
members: [图片生成/图生图/2084510220184809474.json, 视频生成/图生视频/MiniMax_H3 文生、图生、首尾帧视频+二阶高清_2090367048231776258.json, 视频生成/图生视频/MiniMax_H3_参考生视频(提示词优化+二阶高清)_2091043575055343618.json, 视频生成/文生视频/MiniMax_H3_三图身份_INT8_潜空间二阶高清_融合版_2093154699863220225.json, 视频生成/文生视频/minimax_h3_i2v图生视频(4steps turbo加速版)_2087887557345505282.json, 视频生成/文生视频/vibex使用H3 _文生、图生、首尾帧视频+二阶高清_2099477707083046914.json, 视频生成/文生视频/海螺H3 极速6分钟生成1.5M 10秒视频-标准模式-全能参考生视频_2084582921754730497.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2084510220184809474.json、视频生成/图生视频/MiniMax_H3 文生、图生、首尾帧视频+二阶高清_2090367048231776258.json、视频生成/图生视频/MiniMax_H3_参考生视频(提示词优化+二阶高清)_2091043575055343618.json、视频生成/文生视频/MiniMax_H3_三图身份_INT8_潜空间二阶高清_融合版_2093154699863220225.json、视频生成/文生视频/minimax_h3_i2v图生视频(4steps turbo加速版)_2087887557345505282.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `CreateVideo` —— 5/7 个有
- `MiniMaxH3SigmaShift` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `SplitSigmas` —— 5/7 个有
- `Label (rgthree)` —— 4/7 个有
- `MiniMaxH3ImageToVideo` —— 4/7 个有
- `ModelPreviewOverrideKJ` —— 4/7 个有
- `SpectrumApplyMiniMaxH3` —— 4/7 个有
- `MiniMaxH3ReferenceToVideo` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `AnyBooleanSwitch` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `ResizeImagesByShorterEdge` —— 1/7 个有
- `easy imageIndexSwitch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy imageIndexSwitch
