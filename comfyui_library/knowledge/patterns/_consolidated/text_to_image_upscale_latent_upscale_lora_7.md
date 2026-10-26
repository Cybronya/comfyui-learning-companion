---
name: text_to_image_upscale_latent_upscale_lora_7
type: Text To Image
frequency: 6
level: strong
coverage: 0.630667
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Int, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, SolAttnPatch, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2106858310698889218.json, 视频生成/图生视频/H3-1080p超高画质8+2方案｜图生视频画质优先_2106592511757217793.json, 视频生成/图生视频/H3_1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2110159798837796865.json, 视频生成/图生视频/H3超高画质8加2工作流，1080P图生视频创作方案_2110874325975920642.json, 视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json, 视频生成/文生视频/文生图参生视频二采放大｜Minimax H3数字人V4.1_2095957755088695298.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3 1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2106858310698889218.json、视频生成/图生视频/H3-1080p超高画质8+2方案｜图生视频画质优先_2106592511757217793.json、视频生成/图生视频/H3_1080P超高画质优先8加2工作流，图生视频高清画质创作方案_2110159798837796865.json、视频生成/图生视频/H3超高画质8加2工作流，1080P图生视频创作方案_2110874325975920642.json、视频生成/文生视频/文生图参双通道｜Minimax H3二采高清放大V4.2_2096580832021540866.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 5/6 个有
- `Astra` —— 4/6 个有
- `CR Prompt Text` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `GetVideoComponents` —— 4/6 个有
- `ImageCrop` —— 4/6 个有
- `ImageScale` —— 4/6 个有
- `ImpactConditionalBranch` —— 4/6 个有
- `布尔孤海` —— 4/6 个有
- `SaveImage` —— 3/6 个有
- `EmptyImage` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `MiniMaxH3ImageToVideo` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `easy boolean` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
