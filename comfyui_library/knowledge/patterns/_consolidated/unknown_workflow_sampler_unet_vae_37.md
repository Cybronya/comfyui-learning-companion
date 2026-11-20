---
name: unknown_workflow_sampler_unet_vae_37
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.666889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMax-H3开源 数字人带货视频 H3多图生视频_2119764971314831362.json, 平台全量/MiniMax-H3开源 数字人带货视频 H3多图生视频_2119767314085277697.json, 平台全量/MiniMax_H3 Singularity V2 + Pika H3 多参考-高动态视频生成工作流11-3_2118000376271171586.json, 平台全量/fastH3_ref2va_2117473692455358465.json, 平台全量/【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394.json, 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json, 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2114896287438041089.json, 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货！_2115216078598135809.json, 数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json, 数字人/数字人/MiniMax-H3开源 数字人视频带货 H3多图生视频_2114678453109874689.json, 数字人/数字人/MiniMax-H3开源 数字人视频带货 H3多图生视频_2114686420479725569.json, 数字人/数字人/MiniMaxH3  数字人视频带货  H3多图生视频_2099428215952596994.json, 数字人/数字人/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2098017732544524289.json, 数字人/数字人/电影_2105166179148066817.json, 数字人/数字人/电影_2113898825818660866.json, 数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json, 视频生成/图生视频/2采五段加速流_2104580181368336385.json, 视频生成/图生视频/MiniMax H3-多参考生视频（8.31最佳）无限流-五段二采串联_2101529087469768706.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_37

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（平台全量/MiniMax-H3开源 数字人带货视频 H3多图生视频_2119764971314831362.json、平台全量/MiniMax-H3开源 数字人带货视频 H3多图生视频_2119767314085277697.json、平台全量/MiniMax_H3 Singularity V2 + Pika H3 多参考-高动态视频生成工作流11-3_2118000376271171586.json、平台全量/fastH3_ref2va_2117473692455358465.json、平台全量/【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 17/18 个有
- `LTXVConcatAVLatent` —— 17/18 个有
- `LTXVSeparateAVLatent` —— 17/18 个有
- `LoraLoaderModelOnly` —— 17/18 个有
- `MinimaxH3LatentUpscaler3D` —— 17/18 个有
- `SetNode` —— 17/18 个有
- `VHS_VideoCombine` —— 17/18 个有
- `ManualSigmas` —— 12/18 个有
- `JjkText` —— 11/18 个有
- `LoadAudio` —— 5/18 个有
- `SplitSigmas` —— 5/18 个有
- `CreateVideo` —— 4/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/18 个有
- `ModelAttentionBackend` —— 4/18 个有
- `SaveVideo` —— 4/18 个有
- `Text` —— 4/18 个有
- `VHS_LoadVideo` —— 4/18 个有
- `easy float` —— 4/18 个有
- `MiniMaxH3SigmaShift` —— 3/18 个有
- `AudioConcat` —— 2/18 个有
- `BlockSparseAttention` —— 2/18 个有
- `GetImageRangeFromBatch` —— 2/18 个有
- `ImageBatchMulti` —— 2/18 个有
- `MiniMaxH3AddGuide` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `SaveAudio` —— 2/18 个有
- `TrimAudioDuration` —— 2/18 个有
- `忽略多组孤海` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `H3AudioRefineSampler` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `LayerColor: ColorAdapter` —— 1/18 个有
- `PrimitiveInt` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
