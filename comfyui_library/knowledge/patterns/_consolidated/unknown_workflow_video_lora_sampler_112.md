---
name: unknown_workflow_video_lora_sampler_112
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.598267
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json, 数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json, 数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json, 数字人/数字人/MiniMax-H3开源 数字人视频带货 H3多图生视频_2114678453109874689.json, 数字人/数字人/MiniMax-H3开源 数字人视频带货 H3多图生视频_2114686420479725569.json, 数字人/数字人/MiniMaxH3  数字人视频带货  H3多图生视频_2099428215952596994.json, 数字人/数字人/优化版本新版口播_2108152027493785602.json, 数字人/数字人/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2098017732544524289.json, 数字人/数字人/新版本口播_2107771154403520513.json, 数字人/数字人/电影_2105166179148066817.json, 数字人/数字人/电影_2113898825818660866.json, 数字人/数字人/视频带货+Images+into+Videos—Digital+Avatars+Drive_2111625660065206273.json, 数字人/数字人/视频编辑-替换视频中的元素_2114576787442327553.json, 视频生成/图生视频/2采五段加速流_2104580181368336385.json, 视频生成/图生视频/MiniMax H3-多参考生视频（8.31最佳）无限流-五段二采串联_2101529087469768706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json、数字人/数字人/MiniMax-H3_Digital_Avatars_for_Video_E-co数字人视频带货_2111730699559587842.json、数字人/数字人/MiniMax-H3_数字人视频带货_2097140288111341570.json、数字人/数字人/MiniMax-H3开源 数字人视频带货 H3多图生视频_2114678453109874689.json、数字人/数字人/MiniMax-H3开源 数字人视频带货 H3多图生视频_2114686420479725569.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `VAEDecode` —— 14/15 个有
- `VAEDecodeAudio` —— 14/15 个有
- `LTXVConcatAVLatent` —— 12/15 个有
- `LTXVSeparateAVLatent` —— 12/15 个有
- `MinimaxH3LatentUpscaler3D` —— 12/15 个有
- `LoadAudio` —— 8/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/15 个有
- `Text` —— 8/15 个有
- `JjkText` —— 7/15 个有
- `ManualSigmas` —— 7/15 个有
- `VHS_LoadVideo` —— 7/15 个有
- `SplitSigmas` —— 5/15 个有
- `easy float` —— 5/15 个有
- `MiniMaxH3AddGuide` —— 4/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/15 个有
- `ModelAttentionBackend` —— 3/15 个有
- `忽略多组孤海` —— 3/15 个有
- `AudioConcat` —— 2/15 个有
- `CreateVideo` —— 2/15 个有
- `GetImageRangeFromBatch` —— 2/15 个有
- `ImageBatchMulti` —— 2/15 个有
- `SaveAudio` —— 2/15 个有
- `SaveVideo` —— 2/15 个有
- `TrimAudioDuration` —— 2/15 个有
- `BlockSparseAttention` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `LayerColor: ColorAdapter` —— 1/15 个有
- `LoadImageFromUrl` —— 1/15 个有
- `MiniMaxH3AVDecodeT8` —— 1/15 个有
- `MiniMaxH3SigmaShift` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
