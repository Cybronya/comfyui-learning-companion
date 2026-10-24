---
name: text_to_image_lora_sampler_clip_463
type: Text To Image
frequency: 4
level: strong
coverage: 0.86225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json, 音频生成/音频生成/AI配音工作流｜一句话描述音色自动生成创意玩法_2100831844735471617.json, 音频生成/音频生成/FireRed TTS语音克隆｜参考音色复刻工作流_2094566446364979201.json, 音频生成/音频生成/FireRed语音理解AI问答｜听音识别智能对话_2094565126929215490.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_463

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json、音频生成/音频生成/AI配音工作流｜一句话描述音色自动生成创意玩法_2100831844735471617.json、音频生成/音频生成/FireRed TTS语音克隆｜参考音色复刻工作流_2094566446364979201.json、音频生成/音频生成/FireRed语音理解AI问答｜听音识别智能对话_2094565126929215490.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `RH_FireRedAudioLoader` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 1/4 个有
- `RH_FireRedAudioTTS` —— 1/4 个有
- `RH_FireRedAudioUnderstand` —— 1/4 个有
- `RH_FireRedAudioVoiceDesign` —— 1/4 个有
- `SaveAudioAdvanced` —— 1/4 个有
- `SaveAudioMP3` —— 1/4 个有
- `SaveText` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `WanVideoTeaCacheKJ` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
