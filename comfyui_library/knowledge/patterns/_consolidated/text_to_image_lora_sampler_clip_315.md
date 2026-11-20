---
name: text_to_image_lora_sampler_clip_315
type: Text To Image
frequency: 7
level: strong
coverage: 0.878
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json, 视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json, 视频生成/图生视频/双采去油优化版工作流，图生视频高质量文戏创作方案_2106138649183211522.json, 视频生成/文生视频/MiniMax H3 latent放大双采+8步lora｜全能参考顶级质速_2089440965449834498.json, 视频生成/文生视频/MiniMax H3全能参考｜latent放大双采+8步lora质量速度兼得_2089466163435761666.json, 视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能_2090837902199709697.json, 视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能流_2090657292453769218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_315

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 8.22版｜图生视频工作流直出_2091303991069204482.json、视频生成/图生视频/MiniMax H3 NVIDIA VFX HDR 4倍FPS 视频超采样处理工具_2113007348188016641.json、视频生成/图生视频/双采去油优化版工作流，图生视频高质量文戏创作方案_2106138649183211522.json、视频生成/文生视频/MiniMax H3 latent放大双采+8步lora｜全能参考顶级质速_2089440965449834498.json、视频生成/文生视频/MiniMax H3全能参考｜latent放大双采+8步lora质量速度兼得_2089466163435761666.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `SplitSigmas` —— 6/7 个有
- `H3LatentUpscaleByJingchen573` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `SolAttnMiniMax` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `ExtendIntermediateSigmas` —— 3/7 个有
- `MiniMaxLowVRAMAttention` —— 3/7 个有
- `MinimaxH3LatentUpscaler3D` —— 3/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `DisableNoise` —— 2/7 个有
- `LatentUpscaleBy` —— 2/7 个有
- `MiniMaxH3HybridLoader` —— 2/7 个有
- `MiniMaxH3SigmaShift` —— 2/7 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/7 个有
- `ModelPatchTorchSettings` —— 2/7 个有
- `Lora Loader Stack (rgthree)` —— 1/7 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/7 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 1/7 个有
- `PixaromaSaveMp4` —— 1/7 个有
- `RTXTrueHDR` —— 1/7 个有
- `RTXVideoFrameGeneration` —— 1/7 个有
- `RTXVideoSuperResolutionV2` —— 1/7 个有
- `SigmasToFloat` —— 1/7 个有
- `Textbox` —— 1/7 个有
- `WujiAudioLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
