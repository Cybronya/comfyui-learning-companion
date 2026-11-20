---
name: text_to_image_lora_sampler_clip_346
type: Text To Image
frequency: 6
level: strong
coverage: 0.8085
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3快速动作一镜到底多图参考，文生图图生视频高效创作工具_2103959005801574402.json, 数字人/数字人/MiniMax H3 MV造梦机 超快数字人低显存音乐节拍处理工具_2113020217671639041.json, 数字人/数字人/老王房产专用流｜Minimax+H3双模双采数字人_2097974073354702849.json, 视频生成/图生视频/4K加二采新condition加同模双采加H3加动态修复 视频生成优化_2108981922180452354.json, 视频生成/图生视频/LMS二采新Condition同模双采语义桥图生视频处理工具_2101405530886598657.json, 视频生成/图生视频/LMS二采新condition测试｜同模双采语义桥实战_2101147756453785601.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_346

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/MiniMax H3快速动作一镜到底多图参考，文生图图生视频高效创作工具_2103959005801574402.json、数字人/数字人/MiniMax H3 MV造梦机 超快数字人低显存音乐节拍处理工具_2113020217671639041.json、数字人/数字人/老王房产专用流｜Minimax+H3双模双采数字人_2097974073354702849.json、视频生成/图生视频/4K加二采新condition加同模双采加H3加动态修复 视频生成优化_2108981922180452354.json、视频生成/图生视频/LMS二采新Condition同模双采语义桥图生视频处理工具_2101405530886598657.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 5/6 个有
- `LTXVSeparateAVLatent` —— 5/6 个有
- `MiniMaxChunkFeedForward` —— 5/6 个有
- `MinimaxH3LatentUpscaler3D` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `SplitSigmas` —— 5/6 个有
- `VAEDecodeAudio` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `H3SigmaRefiner` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `ModelPreviewOverrideKJ` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `ConcatTextOfUtils` —— 3/6 个有
- `CreateVideo` —— 3/6 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/6 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/6 个有
- `MiniMaxH3TurboLoRA` —— 3/6 个有
- `SaveVideo` —— 3/6 个有
- `Seed (rgthree)` —— 3/6 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 3/6 个有
- `SolAttnMiniMax` —— 3/6 个有
- `SolAttnPatch` —— 2/6 个有
- `Astra` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/6 个有
- `MiniMaxH3VAEDecodeFast` —— 1/6 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 1/6 个有
- `ModelPatchTorchSettings` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `VHS_LoadAudioUpload` —— 1/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/6 个有

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
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
