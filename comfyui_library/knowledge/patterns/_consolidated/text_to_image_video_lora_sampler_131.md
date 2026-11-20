---
name: text_to_image_video_lora_sampler_131
type: Text To Image
frequency: 6
level: strong
coverage: 0.909333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3文生视频二采增强 可选三采电影1080P工具_2114077376165539841.json, 视频生成/文生视频/MiniMax H3通用视频二阶高清重绘｜文生视频视频生视频图生视频_2090422244605513729.json, 视频生成/文生视频/万能高清重绘｜MiniMax H3 一键生成式视频放大_2089253796429000705.json, 视频生成/文生视频/二阶高清重绘｜MiniMax H3通用视频画质提升_2093068327055876098.json, 视频生成/文生视频/二阶高清重绘｜MiniMax H3通用视频画质提升_2093226286721359873.json, 视频生成/文生视频/通用视频二阶高清重绘｜MiniMax H3画质增强直出_2090150745961230337.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_131

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3文生视频二采增强 可选三采电影1080P工具_2114077376165539841.json、视频生成/文生视频/MiniMax H3通用视频二阶高清重绘｜文生视频视频生视频图生视频_2090422244605513729.json、视频生成/文生视频/万能高清重绘｜MiniMax H3 一键生成式视频放大_2089253796429000705.json、视频生成/文生视频/二阶高清重绘｜MiniMax H3通用视频画质提升_2093068327055876098.json、视频生成/文生视频/二阶高清重绘｜MiniMax H3通用视频画质提升_2093226286721359873.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 5/6 个有
- `H3InjectVideoLatent` —— 5/6 个有
- `LTXVConcatAVLatent` —— 5/6 个有
- `LTXVSeparateAVLatent` —— 5/6 个有
- `LoadVideoUI` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `MiniMaxH3NativeAudioLock` —— 5/6 个有
- `MinimaxH3LatentUpscaler3D` —— 3/6 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/6 个有
- `DiffusionModelLoaderKJ` —— 1/6 个有
- `ImageCrop` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SetLatentNoiseMask` —— 1/6 个有
- `SolidMask` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `VAEDecodeAudio` —— 1/6 个有
- `Yuan_RTXVideoUpscaleH3` —— 1/6 个有

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
