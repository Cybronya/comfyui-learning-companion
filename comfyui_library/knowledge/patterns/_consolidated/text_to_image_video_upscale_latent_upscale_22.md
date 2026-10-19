---
name: text_to_image_video_upscale_latent_upscale_22
type: Text To Image
frequency: 3
level: weak
coverage: 0.519
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Float, GetNode, H3SigmaRefiner, KSampler, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AITUDOU-MiniMax H3 双采样 潜空间放大_2089754898287124481.json, 视频生成/图生视频/双采样潜空间放大DSW｜MiniMax H3二次优化生成_2095951614468251650.json, 视频生成/图生视频/潜空间放大二次优化｜MiniMax H3 双采样DSW图生视频_2096239277662363650.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/AITUDOU-MiniMax H3 双采样 潜空间放大_2089754898287124481.json、视频生成/图生视频/双采样潜空间放大DSW｜MiniMax H3二次优化生成_2095951614468251650.json、视频生成/图生视频/潜空间放大二次优化｜MiniMax H3 双采样DSW图生视频_2096239277662363650.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Float`
- `GetNode`
- `H3SigmaRefiner`
- `KSampler`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `LoraLoaderBypassModelOnly` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `SolAttnMiniMax` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `WujiCleaner` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 3 | 9% |
| 高度 | 80 | 80 - 512 | 3 | 9% |
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，3 个样本，取值分散，一致性仅 9%
- 高度 中位数 80，观测区间 80 - 512，3 个样本，取值分散，一致性仅 9%
- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
