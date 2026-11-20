---
name: text_to_image_lora_sampler_clip_263
type: Text To Image
frequency: 8
level: strong
coverage: 0.915
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3高质感低显存文生视频16G24G可跑真人感优化，文生视频方案_2107557534063218690.json, 图片生成/文生图/MiniMax H3高质感低显存文生视频｜16G_24G显卡可跑，真人感优化_2107307665390133250.json, 图片生成/文生图/Minimax H3二采提速｜高分辨率生成细节修复修脸去伪影_2088753229877301249.json, 视频生成/文生视频/FastH3 V2首尾帧视频 文生视频图生视频处理_2100685040215740418.json, 视频生成/文生视频/FastH3图生视频 高效视频生成处理工具_2100661665351168002.json, 视频生成/文生视频/FastVideo FastH3文生视频工作流，文生视频高效文本到视频生成方案_2107907010388914178.json, 视频生成/文生视频/FastVideo FastH3文生视频｜提示词直出视频不绕路_2107692375844941826.json, 视频生成/文生视频/H3 LightX2V二采高清文生视频图生视频生成_2088217634990018561.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_263

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/MiniMax H3高质感低显存文生视频16G24G可跑真人感优化，文生视频方案_2107557534063218690.json、图片生成/文生图/MiniMax H3高质感低显存文生视频｜16G_24G显卡可跑，真人感优化_2107307665390133250.json、图片生成/文生图/Minimax H3二采提速｜高分辨率生成细节修复修脸去伪影_2088753229877301249.json、视频生成/文生视频/FastH3 V2首尾帧视频 文生视频图生视频处理_2100685040215740418.json、视频生成/文生视频/FastH3图生视频 高效视频生成处理工具_2100661665351168002.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

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
- `ModelAttentionBackend` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `BlockSparseAttention` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `GetVideoComponents` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `ImageScale` —— 2/8 个有
- `MiniMaxChunkFeedForward` —— 2/8 个有
- `MiniMaxLowVRAMAttention` —— 2/8 个有
- `PT_H3ConcatAVLatent` —— 2/8 个有
- `SeedVR2LoadDiTModel` —— 2/8 个有
- `SeedVR2LoadVAEModel` —— 2/8 个有
- `SeedVR2VideoUpscaler` —— 2/8 个有
- `VAEEncode` —— 2/8 个有
- `VAEEncodeAudio` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `GetImageSize` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有

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
