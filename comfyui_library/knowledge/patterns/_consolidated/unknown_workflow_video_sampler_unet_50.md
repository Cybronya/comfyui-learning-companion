---
name: unknown_workflow_video_sampler_unet_50
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.497556
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/MinimaxH3-8步1采音频驱动数字人_2114941734391214082.json, 平台全量/Pika_H3_Flex8步极速去油_2118958712919511041.json, 平台全量/单采最终流！之【风暴虫王】 15步手动拟合特效增强版_2114981456639512577.json, 平台全量/战斗曲线sigma专属流，顶级视效！bf16高配定制版⚠️低配显卡危！_2117184206639026178.json, 数字人/数字人/MM3官流极速3步数字人540P10秒仅需50秒_2109160634083528706.json, 视频生成/图生视频/MinimaxH3单采直出30秒（双重显存优化1.0画质）_2115213653740969985.json, 视频生成/图生视频/【最强单采】双重显存优化1.0画质30秒直出流！_2113599252554407938.json, 视频生成/图生视频/【最强单采】双重显存优化高画质30秒直出流！_2114694719098941442.json, 视频生成/文生视频/【最强单采】双重显存优化高画质30秒直出流！_2114996355134476290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/MinimaxH3-8步1采音频驱动数字人_2114941734391214082.json、平台全量/Pika_H3_Flex8步极速去油_2118958712919511041.json、平台全量/单采最终流！之【风暴虫王】 15步手动拟合特效增强版_2114981456639512577.json、平台全量/战斗曲线sigma专属流，顶级视效！bf16高配定制版⚠️低配显卡危！_2117184206639026178.json、数字人/数字人/MM3官流极速3步数字人540P10秒仅需50秒_2109160634083528706.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `ManualSigmas` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `VAEDecodeAudio` —— 8/9 个有
- `VHS_LoadVideo` —— 8/9 个有
- `忽略多组孤海` —— 8/9 个有
- `BasicScheduler` —— 5/9 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 5/9 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 5/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `LTXVAudioVAEEncode` —— 2/9 个有
- `LTXVConcatAVLatent` —— 2/9 个有
- `LTXVSeparateAVLatent` —— 2/9 个有
- `SetLatentNoiseMask` —— 2/9 个有
- `SolidMask` —— 2/9 个有
- `TrimAudioDuration` —— 2/9 个有
- `ComfySwitchNodeV2` —— 1/9 个有
- `ExtendIntermediateSigmas` —— 1/9 个有
- `LoadAudioUI` —— 1/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
