---
name: text_to_image_lora_sampler_clip_156
type: Text To Image
frequency: 11
level: strong
coverage: 0.757182
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json, 视频生成/图生视频/MiniMax H3 Ref顶级多参V2 短剧图生视频不偏色处理工具_2112988405880676353.json, 视频生成/图生视频/MiniMax H3 Ref顶级多参不偏色不油光图生视频处理工具_2102134491904036866.json, 视频生成/图生视频/MiniMax H3六图可选图生视频混合模型潜空间高清直出工作流，图生视频方案_2107977180578930690.json, 视频生成/图生视频/MiniMax H3双采潜空间放大图生视频处理工作流_2101380889010855937.json, 视频生成/图生视频/minimaxh3selflift二采音频参考｜三重加持稳定出片_2106239244355325953.json, 视频生成/图生视频/minimaxh3音频参考加持，selflift二采流程一键出片_2110442485200809985.json, 视频生成/图生视频/minimaxh3音频参考加持，selflift二采流程一键出片_2113817190343471105.json, 视频生成/图生视频/显存终极优化｜MINIMAX-H3视频图生视频工作流_2090556860897259521.json, 视频生成/图生视频/武打戏特化制作｜MINIMAX-H3视频生视频图生视频_2092210437902393346.json, 视频生成/文生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json、视频生成/图生视频/MiniMax H3 Ref顶级多参V2 短剧图生视频不偏色处理工具_2112988405880676353.json、视频生成/图生视频/MiniMax H3 Ref顶级多参不偏色不油光图生视频处理工具_2102134491904036866.json、视频生成/图生视频/MiniMax H3六图可选图生视频混合模型潜空间高清直出工作流，图生视频方案_2107977180578930690.json、视频生成/图生视频/MiniMax H3双采潜空间放大图生视频处理工作流_2101380889010855937.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 10/11 个有
- `PrimitiveStringMultiline` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `BasicGuider` —— 9/11 个有
- `CreateVideo` —— 9/11 个有
- `LTXVConcatAVLatent` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 9/11 个有
- `GetNode` —— 8/11 个有
- `MiniMaxChunkFeedForward` —— 8/11 个有
- `MiniMaxLowVRAMAttention` —— 8/11 个有
- `MinimaxH3LatentUpscaler3D` —— 8/11 个有
- `SaveImage` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `LoadAudio` —— 7/11 个有
- `MiniMaxH3SigmaShift` —— 7/11 个有
- `ModelPreviewOverrideKJ` —— 7/11 个有
- `ModelAttentionBackend` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `SaveVideo` —— 5/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/11 个有
- `PlaySound|pysssss` —— 4/11 个有
- `SelfLiftAvatarH3Sampler` —— 4/11 个有
- `SplitSigmas` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `CFGGuider` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `QwenH3PromptLocal` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `YC_ShowText` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/11 个有
- `RTXTrueHDR` —— 1/11 个有
- `RTXVideoFrameGeneration` —— 1/11 个有
- `RTXVideoSuperResolutionV2` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `Textbox` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
