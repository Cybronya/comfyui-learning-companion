---
name: text_to_image_lora_sampler_clip_223
type: Text To Image
frequency: 9
level: strong
coverage: 0.749778
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2103271632474300417.json, 视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2105721669728956418.json, 视频生成/图生视频/H3打斗工作流，图生视频高动态动作场景创作工具_2106489548766269442.json, 视频生成/图生视频/H3打斗工作流｜图生视频 打造拳拳到肉的打斗名场面_2105501306726207490.json, 视频生成/图生视频/H3打斗特效视频生成 武打动作画面直出方案_2110369061031989249.json, 视频生成/图生视频/minimax h3最强动作迁移｜视频图生视频直出_2092048558504628226.json, 视频生成/图生视频/高质量打斗视频专用双采无加速 文生图生视频处理工具_2112970802692972545.json, 视频生成/文生视频/H3突破15秒长视频不劣化工作流拆解系列_2100272112148766722.json, 视频生成/文生视频/H3突破15秒长视频不劣化｜工作流拆解系列生成_2095301463194034178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_223

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2103271632474300417.json、视频生成/图生视频/H3打斗双采工作流，动作场景视频生视频高动态方案_2105721669728956418.json、视频生成/图生视频/H3打斗工作流，图生视频高动态动作场景创作工具_2106489548766269442.json、视频生成/图生视频/H3打斗工作流｜图生视频 打造拳拳到肉的打斗名场面_2105501306726207490.json、视频生成/图生视频/H3打斗特效视频生成 武打动作画面直出方案_2110369061031989249.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ExtendIntermediateSigmas` —— 8/9 个有
- `GetNode` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `SolAttnMiniMax` —— 7/9 个有
- `VAEDecodeAudio` —— 7/9 个有
- `DisableNoise` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `SplitSigmasDenoise` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `ModelPreviewOverrideKJ` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `INTConstant` —— 4/9 个有
- `LoadAudio` —— 4/9 个有
- `ResizeShortestToNode` —— 4/9 个有
- `MiniMaxH3AddGuide` —— 3/9 个有
- `BlockSparseAttention` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `Fast Groups Muter (rgthree)` —— 2/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `H3SigmaRefiner` —— 2/9 个有
- `ImageScaleToTotalPixels` —— 2/9 个有
- `MiniMaxH3AVDecodeT8` —— 2/9 个有
- `Text Concatenate` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RTXVideoSuperResolution` —— 1/9 个有
- `UniBlockSwapTE` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
