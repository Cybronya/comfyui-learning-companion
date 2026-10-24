---
name: text_to_image_lora_sampler_clip_276
type: Text To Image
frequency: 7
level: strong
coverage: 0.910286
common_nodes: [BreezeTTS2LoadModel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewAudio, SaveAudioAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2106909169122111490.json, 数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2108375633033256962.json, 数字人/数字人/魔术剪辑声音克隆配音｜克隆音色自动生成旁白_2106634621160091649.json, 音频生成/音频生成/Breeze TTS 2多人对话音色克隆｜最强语音合成生成_2095927945859780610.json, 音频生成/音频生成/Breeze TTS 2情景控制音色克隆｜情感语音合成生成_2095929357150801921.json, 音频生成/音频生成/Breeze TTS 2最强音色参考语音克隆 AI声音复制工具_2098637583520718850.json, 音频生成/音频生成/Breeze TTS 2音色参考语音克隆｜数字人配音神器_2098705779988713473.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_276

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2106909169122111490.json、数字人/数字人/魔术剪辑声音克隆生成配音工作流，数字人语音克隆处理工具_2108375633033256962.json、数字人/数字人/魔术剪辑声音克隆配音｜克隆音色自动生成旁白_2106634621160091649.json、音频生成/音频生成/Breeze TTS 2多人对话音色克隆｜最强语音合成生成_2095927945859780610.json、音频生成/音频生成/Breeze TTS 2情景控制音色克隆｜情感语音合成生成_2095929357150801921.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Apply Whisper` —— 6/7 个有
- `CR Text` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `NormalizeAudioLoudness` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `BreezeTTS2VoiceDirection` —— 4/7 个有
- `BreezeTTS2MultiSpeaker` —— 3/7 个有
- `BreezeTTS2Speaker` —— 3/7 个有
- `BreezeTTS2VoiceClone` —— 2/7 个有
- `BreezeTTS2VoiceDesign` —— 2/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `SaveAudio` —— 2/7 个有
- `T8_BreezeTTS_DirectionRequest` —— 2/7 个有
- `T8_BreezeTTS_Generate` —— 2/7 个有
- `T8_BreezeTTS_GenerationSettings` —— 2/7 个有
- `T8_BreezeTTS_ModelLoader` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
