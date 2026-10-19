---
name: text_to_image_lora_sampler_clip_187
type: Text To Image
frequency: 5
level: strong
coverage: 0.877
common_nodes: [AudioCrop, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, SaveAudio, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Index-tts2 语音克隆｜单人双人对话都能做｜数字人音频生成_2096838123635433473.json, 音频生成/音频生成/Index-tts双人对话语音合成｜数字人音频生成制作_2096644358408851458.json, 音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110250401802047489.json, 音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110364673857114114.json, 音频生成/音频生成/声音克隆Qwen3 TTS 音色复刻方案_2109779921815031809.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_187

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/Index-tts2 语音克隆｜单人双人对话都能做｜数字人音频生成_2096838123635433473.json、音频生成/音频生成/Index-tts双人对话语音合成｜数字人音频生成制作_2096644358408851458.json、音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110250401802047489.json、音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110364673857114114.json、音频生成/音频生成/声音克隆Qwen3 TTS 音色复刻方案_2109779921815031809.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `SaveAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 3/5 个有
- `Qwen3TTSModelLoader` —— 3/5 个有
- `Qwen3TTSVoiceClone` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `AudioSeparation` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `IndexTTS2Run` —— 2/5 个有
- `String` —— 2/5 个有
- `Text Multiline` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
