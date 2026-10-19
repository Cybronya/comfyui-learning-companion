---
name: text_to_image_lora_sampler_clip_240
type: Text To Image
frequency: 3
level: strong
coverage: 0.927
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, GetVideoComponents, JjkText, KSampler, LoadAudio, LoadVideo, LoraLoaderModelOnly, Qwen3ASRLoader, Qwen3ASRTranscribe, RH_HeyGemNode, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441.json, 数字人/数字人/数字人工作流2.0版本｜数字人口播视频轻松做_2100841377956458497.json, 数字人/数字人/数字人工作流3.0升级版｜数字人视频一站式生成_2100823288216903681.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_240

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/HeyGem+IndexTTS2.5数字人｜视频生视频快速语音迁移_2096324334888509441.json、数字人/数字人/数字人工作流2.0版本｜数字人口播视频轻松做_2100841377956458497.json、数字人/数字人/数字人工作流3.0升级版｜数字人视频一站式生成_2100823288216903681.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `GetVideoComponents`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `RH_HeyGemNode`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 2/3 个有
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有
- `SoundFlow_TrimAudio` —— 1/3 个有
- `WujiCleaner` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

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
