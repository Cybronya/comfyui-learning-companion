---
name: text_to_image_lora_sampler_clip_389
type: Text To Image
frequency: 5
level: strong
coverage: 0.8472
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109784858150137858.json, 音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109855265834225666.json, 音频生成/音频生成/Qwen3TTS声音设计工作流｜音频生成新选择 配音音效一站搞定_2105566645342265345.json, 音频生成/音频生成/Suno单曲模式音乐生成 高质量歌曲创作直出_2110363898913312770.json, 音频生成/音频生成/史上最强音色克隆｜IndexTTS2声音克隆数字人音频_2092898751957524481.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_389

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109784858150137858.json、音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109855265834225666.json、音频生成/音频生成/Qwen3TTS声音设计工作流｜音频生成新选择 配音音效一站搞定_2105566645342265345.json、音频生成/音频生成/Suno单曲模式音乐生成 高质量歌曲创作直出_2110363898913312770.json、音频生成/音频生成/史上最强音色克隆｜IndexTTS2声音克隆数字人音频_2092898751957524481.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `FB_Qwen3TTSVoiceDesign` —— 2/5 个有
- `LoadAudio` —— 2/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `IndexTTS2Run` —— 1/5 个有
- `Qwen3TTSModelLoader` —— 1/5 个有
- `Qwen3TTSVoiceDesign` —— 1/5 个有
- `RH_RhartAudioSunoV55Single` —— 1/5 个有
- `SaveAudioAdvanced` —— 1/5 个有
- `SaveAudioMP3` —— 1/5 个有

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
