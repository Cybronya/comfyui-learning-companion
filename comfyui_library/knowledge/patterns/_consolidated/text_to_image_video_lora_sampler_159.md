---
name: text_to_image_video_lora_sampler_159
type: Text To Image
frequency: 3
level: strong
coverage: 0.905333
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Infinite Talk对口型数字人｜说话唱歌单人版无限长V3_2093131573515350018.json, 视频生成/图生视频/Infinitetalk图片数字人｜最新优化版口型更自然_2097148990650413057.json, 视频生成/图生视频/图生语音视频｜InfiniteTalk数字人角色表演_2091230403377061890.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_159

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Infinite Talk对口型数字人｜说话唱歌单人版无限长V3_2093131573515350018.json、视频生成/图生视频/Infinitetalk图片数字人｜最新优化版口型更自然_2097148990650413057.json、视频生成/图生视频/图生语音视频｜InfiniteTalk数字人角色表演_2091230403377061890.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `Int` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `WanVideoSampler` —— 2/3 个有
- `WanVideoTextEncodeCached` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadWanVideoT5TextEncoder` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `ToInt` —— 1/3 个有
- `WanVideoLoraSelectMulti` —— 1/3 个有
- `WanVideoSamplerExtraArgs` —— 1/3 个有
- `WanVideoSamplerv2` —— 1/3 个有
- `WanVideoSchedulerv2` —— 1/3 个有
- `WanVideoTextEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
