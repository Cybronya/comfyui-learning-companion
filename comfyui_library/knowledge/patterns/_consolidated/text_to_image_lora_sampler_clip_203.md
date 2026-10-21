---
name: text_to_image_lora_sampler_clip_203
type: Text To Image
frequency: 6
level: strong
coverage: 0.899667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3高质感低显存文生视频16G24G可跑真人感优化，文生视频方案_2107557534063218690.json, 图片生成/文生图/MiniMax H3高质感低显存文生视频｜16G_24G显卡可跑，真人感优化_2107307665390133250.json, 图片生成/文生图/Minimax H3二采提速｜高分辨率生成细节修复修脸去伪影_2088753229877301249.json, 视频生成/图生视频/MiniMax H3 I2V加速多参考视频生成工作流，图生视频高效创作工具_2106861353209253890.json, 视频生成/图生视频/MiniMax H3 I2V加速首尾帧工作流，图生视频高效创作工具_2106838741942886401.json, 视频生成/图生视频/Minimax H3无色差版｜首尾帧参考生视频电商模特展示_2089376588533157889.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_203

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/MiniMax H3高质感低显存文生视频16G24G可跑真人感优化，文生视频方案_2107557534063218690.json、图片生成/文生图/MiniMax H3高质感低显存文生视频｜16G_24G显卡可跑，真人感优化_2107307665390133250.json、图片生成/文生图/Minimax H3二采提速｜高分辨率生成细节修复修脸去伪影_2088753229877301249.json、视频生成/图生视频/MiniMax H3 I2V加速多参考视频生成工作流，图生视频高效创作工具_2106861353209253890.json、视频生成/图生视频/MiniMax H3 I2V加速首尾帧工作流，图生视频高效创作工具_2106838741942886401.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 3/6 个有
- `ModelAttentionBackend` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `GetVideoComponents` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `ImageScale` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `MiniMaxLowVRAMAttention` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `SeedVR2LoadDiTModel` —— 2/6 个有
- `SeedVR2LoadVAEModel` —— 2/6 个有
- `SeedVR2VideoUpscaler` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `MiniMaxH3HybridLoader` —— 1/6 个有
- `PT_H3ConcatAVLatent` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `VAEEncode` —— 1/6 个有
- `VAEEncodeAudio` —— 1/6 个有

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
