---
name: text_to_image_lora_sampler_clip_65
type: Text To Image
frequency: 12
level: strong
coverage: 0.849583
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3高质感低显存文生视频｜16G_24G显卡可跑，真人感优化_2107307665390133250.json, 视频生成/图生视频/FastVideo FastH3图生视频 8步加速视频生成工具_2100636893338759170.json, 视频生成/图生视频/FastVideo FastH3图生视频工作流，图生视频高效视频生成方案_2107904076905275394.json, 视频生成/图生视频/FastVideo FastH3图生视频｜快速通道高效产出视频_2107686292824879105.json, 视频生成/图生视频/H3图生视频首尾帧控制原生音频两张图变一段电影_2100681745967435778.json, 视频生成/图生视频/MiniMax H3 I2V加速多参考视频生成工作流，图生视频高效创作工具_2106861353209253890.json, 视频生成/图生视频/MiniMax H3 I2V加速首尾帧工作流，图生视频高效创作工具_2106838741942886401.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110252157650956290.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110367355523133442.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110253662495928321.json, 视频生成/图生视频/MiniMax H3图生视频fastH3基础版 trim加速快速直出_2110368880341377026.json, 视频生成/图生视频/minimax h3 i2v fastH3 contextmotion longvideo 图生视频_2105127145923244034.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/MiniMax H3高质感低显存文生视频｜16G_24G显卡可跑，真人感优化_2107307665390133250.json、视频生成/图生视频/FastVideo FastH3图生视频 8步加速视频生成工具_2100636893338759170.json、视频生成/图生视频/FastVideo FastH3图生视频工作流，图生视频高效视频生成方案_2107904076905275394.json、视频生成/图生视频/FastVideo FastH3图生视频｜快速通道高效产出视频_2107686292824879105.json、视频生成/图生视频/H3图生视频首尾帧控制原生音频两张图变一段电影_2100681745967435778.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

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
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `SaveImage` —— 10/12 个有
- `MiniMaxH3SigmaShift` —— 9/12 个有
- `ModelAttentionBackend` —— 9/12 个有
- `ResolutionSelector` —— 9/12 个有
- `BlockSparseAttention` —— 8/12 个有
- `CreateVideo` —— 7/12 个有
- `PrimitiveStringMultiline` —— 7/12 个有
- `SaveVideo` —— 7/12 个有
- `SetNode` —— 5/12 个有
- `VHS_VideoCombine` —— 5/12 个有
- `GetImageSize` —— 3/12 个有
- `GetNode` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 3/12 个有
- `MiniMaxH3AddGuide` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `GetVideoComponents` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `MiniMaxChunkFeedForward` —— 1/12 个有
- `MiniMaxH3MotionContext` —— 1/12 个有
- `MiniMaxH3MotionContextChain` —— 1/12 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/12 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/12 个有
- `MiniMaxH3MotionContextTrim` —— 1/12 个有
- `MiniMaxLowVRAMAttention` —— 1/12 个有
- `SeedVR2LoadDiTModel` —— 1/12 个有
- `SeedVR2LoadVAEModel` —— 1/12 个有
- `SeedVR2VideoUpscaler` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

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
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
