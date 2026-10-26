---
name: text_to_image_video_sampler_clip_2
type: Text To Image
frequency: 4
level: weak
coverage: 0.923
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, KSampler, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Infinite Talk对口型数字人｜说话唱歌单人版无限长V3_2093131573515350018.json, 视频生成/图生视频/Infinitetalk图片数字人｜最新优化版口型更自然_2097148990650413057.json, 视频生成/图生视频/图生语音视频｜InfiniteTalk数字人角色表演_2091230403377061890.json, 视频生成/文生视频/视频生成_2108532387113160705.json]
source: knowledge_consolidation
---

# text_to_image_video_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Infinite Talk对口型数字人｜说话唱歌单人版无限长V3_2093131573515350018.json、视频生成/图生视频/Infinitetalk图片数字人｜最新优化版口型更自然_2097148990650413057.json、视频生成/图生视频/图生语音视频｜InfiniteTalk数字人角色表演_2091230403377061890.json、视频生成/文生视频/视频生成_2108532387113160705.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `KSampler`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `Int` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoSampler` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `solarL_SaveImagesToZip` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `Audio Duration (mtb)` —— 2/4 个有
- `LoadWanVideoT5TextEncoder` —— 2/4 个有
- `ToInt` —— 2/4 个有
- `WanVideoTextEncode` —— 2/4 个有
- `WanVideoTextEncodeCached` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RH_GetAudioDuration` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `VAEEncode` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有
- `WanVideoSamplerExtraArgs` —— 1/4 个有
- `WanVideoSamplerv2` —— 1/4 个有
- `WanVideoSchedulerv2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 4 | 59% |
| Prompt 约束强度(CFG) | 4.5 | 0 - 4.5 | 4 | 42% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 1024 | 4 | 0% |
| 高度 | 80 | 80 - 1024 | 4 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 0 - 4.5，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 0%
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
