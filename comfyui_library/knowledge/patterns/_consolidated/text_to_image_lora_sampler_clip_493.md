---
name: text_to_image_lora_sampler_clip_493
type: Text To Image
frequency: 4
level: strong
coverage: 0.78375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109855265834225666.json, 音频生成/音频生成/Suno单曲模式音乐生成 高质量歌曲创作直出_2110363898913312770.json, 音频生成/音频生成/Suno自定义模式音乐生成 歌曲风格定制方案_2110365492958552066.json, 音频生成/音频生成/文生音乐工作流｜MiniMax Music 2.6一句话生成专属配乐｜音频生成_2099151761704579073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_493

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109855265834225666.json、音频生成/音频生成/Suno单曲模式音乐生成 高质量歌曲创作直出_2110363898913312770.json、音频生成/音频生成/Suno自定义模式音乐生成 歌曲风格定制方案_2110365492958552066.json、音频生成/音频生成/文生音乐工作流｜MiniMax Music 2.6一句话生成专属配乐｜音频生成_2099151761704579073.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

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

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RH_MinimaxMusic26` —— 1/4 个有
- `RH_RhartAudioSunoV55Custom` —— 1/4 个有
- `RH_RhartAudioSunoV55Single` —— 1/4 个有
- `SaveAudioAdvanced` —— 1/4 个有

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
