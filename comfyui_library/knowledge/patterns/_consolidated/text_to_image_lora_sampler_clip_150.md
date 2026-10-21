---
name: text_to_image_lora_sampler_clip_150
type: Text To Image
frequency: 8
level: strong
coverage: 0.73175
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2103271632474300417.json, 视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2105721669728956418.json, 视频生成/图生视频/H3打斗工作流，图生视频高动态动作场景创作工具_2106489548766269442.json, 视频生成/图生视频/H3打斗工作流｜图生视频 打造拳拳到肉的打斗名场面_2105501306726207490.json, 视频生成/图生视频/H3打斗特效视频生成 武打动作画面直出方案_2110369061031989249.json, 视频生成/图生视频/minimax h3最强动作迁移｜视频图生视频直出_2092048558504628226.json, 视频生成/文生视频/H3突破15秒长视频不劣化工作流拆解系列_2100272112148766722.json, 视频生成/文生视频/H3突破15秒长视频不劣化｜工作流拆解系列生成_2095301463194034178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2103271632474300417.json、视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2105721669728956418.json、视频生成/图生视频/H3打斗工作流，图生视频高动态动作场景创作工具_2106489548766269442.json、视频生成/图生视频/H3打斗工作流｜图生视频 打造拳拳到肉的打斗名场面_2105501306726207490.json、视频生成/图生视频/H3打斗特效视频生成 武打动作画面直出方案_2110369061031989249.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ExtendIntermediateSigmas` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `SolAttnMiniMax` —— 7/8 个有
- `VAEDecodeAudio` —— 6/8 个有
- `DisableNoise` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `SplitSigmasDenoise` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `INTConstant` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `ResizeShortestToNode` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `LoadAudio` —— 3/8 个有
- `MiniMaxH3AddGuide` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `GetImageRangeFromBatch` —— 2/8 个有
- `H3SigmaRefiner` —— 2/8 个有
- `MiniMaxH3AVDecodeT8` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有
- `UniBlockSwapTE` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
