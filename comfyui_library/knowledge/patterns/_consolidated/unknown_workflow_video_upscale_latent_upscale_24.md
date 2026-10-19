---
name: unknown_workflow_video_upscale_latent_upscale_24
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.568769
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MiniMax H3-多参考生视频-666_2106965266444935170.json, 数字人/数字人/H3二采_2111323289078550530.json, 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json, 数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json, 数字人/数字人/MiniMaxH3  数字人视频带货  H3多图生视频_2099428215952596994.json, 数字人/数字人/【MINIMAX-H3】八月最强文戏-低配版_2100034371259555842.json, 数字人/数字人/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2098017732544524289.json, 数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json, 视频生成/图生视频/-MiniMax H3-多参考生视频-优化版_2106660994788446209.json, 视频生成/图生视频/2采五段加速流_2104580181368336385.json, 视频生成/图生视频/H3短剧工作流-低配版9.12_2099422256219906050.json, 视频生成/图生视频/MINIMAX-H3-全自动打斗武戏-15秒8分钟_2097790484570796033.json, 视频生成/图生视频/MiniMax H3-多参考生视频（8.31最佳）无限流-五段二采串联_2101529087469768706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_24

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/MiniMax H3-多参考生视频-666_2106965266444935170.json、数字人/数字人/H3二采_2111323289078550530.json、数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json、数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json、数字人/数字人/MiniMaxH3  数字人视频带货  H3多图生视频_2099428215952596994.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 9/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/13 个有
- `忽略多组孤海` —— 8/13 个有
- `VHS_LoadVideo` —— 6/13 个有
- `JjkText` —— 5/13 个有
- `ManualSigmas` —— 5/13 个有
- `SplitSigmas` —— 5/13 个有
- `Text` —— 5/13 个有
- `easy float` —— 5/13 个有
- `ModelAttentionBackend` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `ExtendIntermediateSigmas` —— 3/13 个有
- `H3SigmaRefiner` —— 3/13 个有
- `INTConstant` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `AudioConcat` —— 2/13 个有
- `GetImageRangeFromBatch` —— 2/13 个有
- `ImageBatchMulti` —— 2/13 个有
- `MiniMaxH3AddGuide` —— 2/13 个有
- `SaveAudio` —— 2/13 个有
- `TrimAudioDuration` —— 2/13 个有
- `BlockSparseAttention` —— 1/13 个有
- `LayerColor: ColorAdapter` —— 1/13 个有
- `MiniMaxChunkFeedForward` —— 1/13 个有
- `MiniMaxH3SigmaShift` —— 1/13 个有
- `MiniMaxLowVRAMAttention` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
