---
name: text_to_image_lora_sampler_clip_486
type: Text To Image
frequency: 4
level: strong
coverage: 0.919
common_nodes: [Apply Whisper, BreezeTTS2LoadModel, CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, NormalizeAudioLoudness, PreviewAudio, SaveAudioAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Breeze TTS 2 低声耳语ASMR｜全功能音频生成工作流_2112474568299474945.json, 数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2106909169122111490.json, 音频生成/音频生成/Breeze TTS 2最强音色参考语音克隆 AI声音复制工具_2098637583520718850.json, 音频生成/音频生成/Breeze TTS 2音色参考语音克隆｜数字人配音神器_2098705779988713473.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_486

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/Breeze TTS 2 低声耳语ASMR｜全功能音频生成工作流_2112474568299474945.json、数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2106909169122111490.json、音频生成/音频生成/Breeze TTS 2最强音色参考语音克隆 AI声音复制工具_2098637583520718850.json、音频生成/音频生成/Breeze TTS 2音色参考语音克隆｜数字人配音神器_2098705779988713473.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `Apply Whisper`
- `BreezeTTS2LoadModel`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `NormalizeAudioLoudness`
- `PreviewAudio`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BreezeTTS2MultiSpeaker` —— 3/4 个有
- `BreezeTTS2Speaker` —— 3/4 个有
- `BreezeTTS2VoiceClone` —— 3/4 个有
- `BreezeTTS2VoiceDesign` —— 3/4 个有
- `CR Prompt Text` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `T8_BreezeTTS_DirectionRequest` —— 3/4 个有
- `T8_BreezeTTS_Generate` —— 3/4 个有
- `T8_BreezeTTS_GenerationSettings` —— 3/4 个有
- `T8_BreezeTTS_ModelLoader` —— 3/4 个有
- `SaveAudio` —— 2/4 个有
- `BreezeTTS2VoiceDirection` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
