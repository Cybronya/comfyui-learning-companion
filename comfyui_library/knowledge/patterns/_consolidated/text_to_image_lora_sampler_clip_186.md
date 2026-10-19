---
name: text_to_image_lora_sampler_clip_186
type: Text To Image
frequency: 5
level: strong
coverage: 0.8876
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveAudioMP3, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Index TTS2加Qwen3 TTS声音克隆二合一，音色语气情感控制音频生成_2105746631021916162.json, 音频生成/音频生成/IndexTTS2参考音色克隆｜音频生成拿来做配音神器_2097213028491161601.json, 音频生成/音频生成/IndexTTS2声音克隆情感版｜给配音注入真实情绪_2097211652537147394.json, 音频生成/音频生成/IndexTTS2情感声音克隆｜参考音色秒变同款嗓音_2097209913914249218.json, 音频生成/音频生成/声音克隆二合一｜Index TTS2+Qwen3 TTS音色参考情感控制_2095297314482118657.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_186

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/Index TTS2加Qwen3 TTS声音克隆二合一，音色语气情感控制音频生成_2105746631021916162.json、音频生成/音频生成/IndexTTS2参考音色克隆｜音频生成拿来做配音神器_2097213028491161601.json、音频生成/音频生成/IndexTTS2声音克隆情感版｜给配音注入真实情绪_2097211652537147394.json、音频生成/音频生成/IndexTTS2情感声音克隆｜参考音色秒变同款嗓音_2097209913914249218.json、音频生成/音频生成/声音克隆二合一｜Index TTS2+Qwen3 TTS音色参考情感控制_2095297314482118657.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 2/5 个有
- `AudioCrop` —— 2/5 个有
- `FB_Qwen3TTSVoiceClone` —— 2/5 个有
- `IndexTTS2Run` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `Text` —— 2/5 个有
- `IndexTTS2BaseNode` —— 1/5 个有
- `IndexTTS2EmotionTextNode` —— 1/5 个有
- `IndexTTS2EmotionVectorNode` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

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
