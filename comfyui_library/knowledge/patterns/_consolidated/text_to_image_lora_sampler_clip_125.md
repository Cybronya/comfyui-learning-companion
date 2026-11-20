---
name: text_to_image_lora_sampler_clip_125
type: Text To Image
frequency: 12
level: strong
coverage: 0.734417
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3 V4 加速版｜8步便宜高分辨率 Lightx2v 新版_2096848305606184962.json, 图片生成/图生图/V4加速8步Lightx2v新版｜MiniMax H3便宜高分辨率图生图_2096688541081366530.json, 视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json, 视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json, 视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json, 视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2106873837555113985.json, 视频生成/图生视频/Minimax图生视频I2V工作流含首尾帧，图生视频高效创作工具_2109810746019373058.json, 视频生成/图生视频/Minimax图生视频I2V工作流，图生视频官方图生视频处理工具_2107908610960486402.json, 视频生成/图生视频/Minimax图生视频I2V方案，图生视频高效直出_2111192151311872002.json, 视频生成/图生视频/Minimax图生视频I2V方案｜图片动起来就这么简单_2107697471907516418.json, 视频生成/图生视频/Minimax图生视频I2V｜单图驱动动态画面生成稳定流_2112893548440936450.json, 视频生成/文生视频/MiniMax T2V文生视频 写实Lora开关latent续写处理工具_2112967836275658753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 V4 加速版｜8步便宜高分辨率 Lightx2v 新版_2096848305606184962.json、图片生成/图生图/V4加速8步Lightx2v新版｜MiniMax H3便宜高分辨率图生图_2096688541081366530.json、视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json、视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json、视频生成/图生视频/MinimaxH3海螺4步lightx2v加速lora-多重提速转场运镜图生视频_2087374035620556802.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `BasicScheduler` —— 9/12 个有
- `ComfySwitchNode` —— 9/12 个有
- `KSamplerSelect` —— 9/12 个有
- `PrimitiveBoolean` —— 9/12 个有
- `GetImageSize` —— 8/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `GetNode` —— 7/12 个有
- `LoadAudio` —— 7/12 个有
- `PrimitiveInt` —— 7/12 个有
- `SetNode` —— 7/12 个有
- `AudioCrop` —— 5/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/12 个有
- `SaveImage` —— 5/12 个有
- `easy minimaxH3AudioLock` —— 5/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/12 个有
- `MiniMaxH3SaveLatent` —— 3/12 个有
- `Any Switch (rgthree)` —— 2/12 个有
- `AudioConcat` —— 2/12 个有
- `AudioInfo` —— 2/12 个有
- `EmptyAudio` —— 2/12 个有
- `Fast Bypasser (rgthree)` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `ImpactConditionalBranch` —— 2/12 个有
- `MiniMaxH3AudioLock` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `TrimAudioDuration` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `EmptyImage` —— 1/12 个有
- `LoraLoaderBypassModelOnly` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

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
