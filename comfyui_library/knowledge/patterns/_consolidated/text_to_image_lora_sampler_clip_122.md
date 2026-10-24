---
name: text_to_image_lora_sampler_clip_122
type: Text To Image
frequency: 12
level: strong
coverage: 0.802917
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/多参考latent二采｜minimaxh3反推提示词图生图_2091177125763174402.json, 图片生成/文生图/多参考latent二采｜minimaxh3图生图反推提示词生成_2091246455515336706.json, 图片生成/文生图/真人一致性｜人物一致、细节升级_2098733105417908225.json, 数字人/数字人/7度工作流改版1号｜数字人生成效果升级更自然_2106257948442972161.json, 数字人/数字人/7度工作流改版1数字人生成方案，数字人图像处理工具_2107527180271050754.json, 数字人/数字人/7度工作流改版1，数字人生成图像编辑多场景覆盖处理方案_2106524485028499458.json, 数字人/数字人/7度工作流改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107284908405248002.json, 数字人/数字人/老王房产专用流｜Minimax+H3双模双采数字人_2097974073354702849.json, 视频生成/图生视频/10步+3步Latent Upscaler｜H3参考模式图生视频_2091180204667531265.json, 视频生成/图生视频/4K加二采新condition加同模双采加H3加动态修复 视频生成优化_2108981922180452354.json, 视频生成/图生视频/LMS二采新Condition同模双采语义桥图生视频处理工具_2101405530886598657.json, 视频生成/图生视频/LMS二采新condition测试｜同模双采语义桥实战_2101147756453785601.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/多参考latent二采｜minimaxh3反推提示词图生图_2091177125763174402.json、图片生成/文生图/多参考latent二采｜minimaxh3图生图反推提示词生成_2091246455515336706.json、图片生成/文生图/真人一致性｜人物一致、细节升级_2098733105417908225.json、数字人/数字人/7度工作流改版1号｜数字人生成效果升级更自然_2106257948442972161.json、数字人/数字人/7度工作流改版1数字人生成方案，数字人图像处理工具_2107527180271050754.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
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
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 11/12 个有
- `MiniMaxH3SigmaShift` —— 10/12 个有
- `CreateVideo` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `GetNode` —— 8/12 个有
- `ModelAttentionBackend` —— 8/12 个有
- `ModelPreviewOverrideKJ` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `SplitSigmas` —— 8/12 个有
- `LTXVConcatAVLatent` —— 7/12 个有
- `LTXVSeparateAVLatent` —— 7/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/12 个有
- `VHS_VideoCombine` —— 6/12 个有
- `H3SigmaRefiner` —— 5/12 个有
- `LoadAudio` —— 5/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/12 个有
- `MinimaxH3LatentUpscaler3D` —— 5/12 个有
- `PreviewImage` —— 5/12 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 4/12 个有
- `MiniMaxLowVRAMAttention` —— 4/12 个有
- `SaveImage` —— 4/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `CR Prompt Text` —— 3/12 个有
- `ConcatTextOfUtils` —— 3/12 个有
- `MiniMaxChunkFeedForward` —— 3/12 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/12 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/12 个有
- `MiniMaxH3TurboLoRA` —— 3/12 个有
- `Seed (rgthree)` —— 3/12 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 3/12 个有
- `SolAttnMiniMax` —— 3/12 个有
- `ExtendIntermediateSigmas` —— 2/12 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/12 个有
- `easy int` —— 2/12 个有
- `Astra` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `ManualSigmas` —— 1/12 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/12 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 1/12 个有
- `MiniMaxH3VAEDecodeFast` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
