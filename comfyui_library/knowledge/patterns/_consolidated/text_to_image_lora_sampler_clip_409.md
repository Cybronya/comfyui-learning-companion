---
name: text_to_image_lora_sampler_clip_409
type: Text To Image
frequency: 5
level: strong
coverage: 0.902
common_nodes: [BreezeTTS2LoadModel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewAudio, SaveAudioAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2108375633033256962.json, 数字人/数字人/魔术剪辑声音克隆配音｜克隆音色自动生成旁白_2106634621160091649.json, 音频生成/音频生成/Breeze TTS 2多人对话音色克隆｜最强语音合成生成_2095927945859780610.json, 音频生成/音频生成/Breeze TTS 2情景控制音色克隆｜情感语音合成生成_2095929357150801921.json, 音频生成/音频生成/多人对话音色一键克隆｜Breeze TTS 2 九月音频生成强档_2096195742212902913.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_409

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2108375633033256962.json、数字人/数字人/魔术剪辑声音克隆配音｜克隆音色自动生成旁白_2106634621160091649.json、音频生成/音频生成/Breeze TTS 2多人对话音色克隆｜最强语音合成生成_2095927945859780610.json、音频生成/音频生成/Breeze TTS 2情景控制音色克隆｜情感语音合成生成_2095929357150801921.json、音频生成/音频生成/多人对话音色一键克隆｜Breeze TTS 2 九月音频生成强档_2096195742212902913.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `BreezeTTS2LoadModel`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAudio`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `Apply Whisper` —— 3/5 个有
- `BreezeTTS2VoiceDirection` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `NormalizeAudioLoudness` —— 3/5 个有
- `BreezeTTS2MultiSpeaker` —— 2/5 个有
- `BreezeTTS2Speaker` —— 2/5 个有
- `EmptyImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
