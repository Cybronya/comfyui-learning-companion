---
name: text_to_image_upscale_latent_upscale_lora_15
type: Text To Image
frequency: 4
level: strong
coverage: 0.67875
common_nodes: [Any Switch (rgthree), Astra, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, GetVideoComponents, ImageCrop, ImageScale, ImpactConditionalBranch, Int, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, SolAttnPatch, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 布尔孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2106858310698889218.json, 视频生成/图生视频/H3-1080p超高画质8+2方案｜图生视频画质优先_2106592511757217793.json, 视频生成/图生视频/H3_1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2110159798837796865.json, 视频生成/图生视频/H3超高画质8加2工作流，1080P图生视频创作方案_2110874325975920642.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_15

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/H3 1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2106858310698889218.json、视频生成/图生视频/H3-1080p超高画质8+2方案｜图生视频画质优先_2106592511757217793.json、视频生成/图生视频/H3_1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2110159798837796865.json、视频生成/图生视频/H3超高画质8加2工作流，1080P图生视频创作方案_2110874325975920642.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Astra`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `GetVideoComponents`
- `ImageCrop`
- `ImageScale`
- `ImpactConditionalBranch`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `SolAttnPatch`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `布尔孤海`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
