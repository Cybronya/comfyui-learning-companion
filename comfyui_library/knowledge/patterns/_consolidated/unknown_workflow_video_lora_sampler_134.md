---
name: unknown_workflow_video_lora_sampler_134
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.632417
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json, 图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json, 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json, 数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json, 数字人/数字人/MiniMaxH3  数字人视频带货  H3多图生视频_2099428215952596994.json, 数字人/数字人/优化版本新版口播_2108152027493785602.json, 数字人/数字人/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2098017732544524289.json, 数字人/数字人/新版本口播_2107771154403520513.json, 数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json, 视频生成/图生视频/-MiniMax H3-多参考生视频-优化版_2106660994788446209.json, 视频生成/图生视频/2采五段加速流_2104580181368336385.json, 视频生成/图生视频/MiniMax H3-多参考生视频（8.31最佳）无限流-五段二采串联_2101529087469768706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_134

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json、图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json、数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json、数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json、数字人/数字人/MiniMaxH3  数字人视频带货  H3多图生视频_2099428215952596994.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `VAEDecode` —— 11/12 个有
- `VAEDecodeAudio` —— 11/12 个有
- `LTXVConcatAVLatent` —— 8/12 个有
- `LTXVSeparateAVLatent` —— 8/12 个有
- `MinimaxH3LatentUpscaler3D` —— 8/12 个有
- `LoadAudio` —— 7/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/12 个有
- `Text` —— 7/12 个有
- `JjkText` —— 5/12 个有
- `ManualSigmas` —— 5/12 个有
- `VHS_LoadVideo` —— 5/12 个有
- `MiniMaxH3AddGuide` —— 4/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `ModelAttentionBackend` —— 3/12 个有
- `SplitSigmas` —— 3/12 个有
- `easy float` —— 3/12 个有
- `忽略多组孤海` —— 3/12 个有
- `AudioConcat` —— 2/12 个有
- `GetImageRangeFromBatch` —— 2/12 个有
- `ImageBatchMulti` —— 2/12 个有
- `SaveAudio` —— 2/12 个有
- `TrimAudioDuration` —— 2/12 个有
- `BlockSparseAttention` —— 1/12 个有
- `Float` —— 1/12 个有
- `LayerColor: ColorAdapter` —— 1/12 个有
- `MiniMaxH3AVDecodeT8` —— 1/12 个有
- `MiniMaxH3SigmaShift` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `SaveImage` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
