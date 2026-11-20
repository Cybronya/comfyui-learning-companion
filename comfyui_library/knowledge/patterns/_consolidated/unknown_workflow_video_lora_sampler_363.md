---
name: unknown_workflow_video_lora_sampler_363
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.558375
common_nodes: [CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/【API】MiniMaxH3 selflift采样工作流_2119627037374771202.json, 平台全量/【Minimax H3】pika极速出片版（8g可跑）_2117983774901366785.json, 平台全量/【Minimax H3】【API画布级工作流】【带音频】_2119709345268195330.json, 数字人/数字人/MiniMax H3_爱宠发布会_2112925200072396801.json, 数字人/数字人/写英文工作流_2113520537002663937.json, 视频生成/图生视频/minimaxh3的selflift+二采+音频参考_2105937177262772225.json, 视频生成/文生视频/1-Aiden-MiniMax-H3-疯狂测试工作流！！！！_2093054855547015170.json, 视频生成/文生视频/minimaxh3的selflift+二采_2101192695308963842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_363

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/【API】MiniMaxH3 selflift采样工作流_2119627037374771202.json、平台全量/【Minimax H3】pika极速出片版（8g可跑）_2117983774901366785.json、平台全量/【Minimax H3】【API画布级工作流】【带音频】_2119709345268195330.json、数字人/数字人/MiniMax H3_爱宠发布会_2112925200072396801.json、数字人/数字人/写英文工作流_2113520537002663937.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 7/8 个有
- `BasicScheduler` —— 7/8 个有
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `RandomNoise` —— 7/8 个有
- `SamplerCustomAdvanced` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `忽略多组孤海` —— 6/8 个有
- `BlockSparseAttention` —— 5/8 个有
- `MiniMaxChunkFeedForward` —— 5/8 个有
- `MiniMaxLowVRAMAttention` —— 5/8 个有
- `ManualSigmas` —— 4/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `CreateVideo` —— 3/8 个有
- `H3SigmaRefiner` —— 3/8 个有
- `LTXVConcatAVLatent` —— 3/8 个有
- `LTXVSeparateAVLatent` —— 3/8 个有
- `MinimaxH3LatentUpscaler3D` —— 3/8 个有
- `SelfLiftAvatarH3Sampler` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `MiniMaxH3SigmaShift` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `GetVideoComponents` —— 1/8 个有
- `InversionDemoLazyIndexSwitch` —— 1/8 个有
- `QZ_ResolutionPreset` —— 1/8 个有
- `RH_Astra` —— 1/8 个有
- `SplitSigmas` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy positive` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
