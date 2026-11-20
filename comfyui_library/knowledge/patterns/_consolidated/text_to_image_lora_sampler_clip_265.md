---
name: text_to_image_lora_sampler_clip_265
type: Text To Image
frequency: 8
level: strong
coverage: 0.902875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, SaveAudio, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/IndexTTS2声线克隆 音色复刻音频生成方案_2108611918436069378.json, 数字人/数字人/IndexTTS2声线克隆神器｜一键复刻原声的数字人配音工作流_2108367981469323266.json, 数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110245936260796418.json, 数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110372280114176002.json, 音频生成/音频生成/Index TTS 2.5语音合成合集｜高质量音频生成制作_2096747098271207425.json, 音频生成/音频生成/IndexTTS2.5多角色配音工作流｜SRT剧本自动语音合成_2097427732920619009.json, 音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json, 音频生成/音频生成/index TTS 2.5双人对话 音频生成方案_2109721870319837185.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_265

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/IndexTTS2声线克隆 音色复刻音频生成方案_2108611918436069378.json、数字人/数字人/IndexTTS2声线克隆神器｜一键复刻原声的数字人配音工作流_2108367981469323266.json、数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110245936260796418.json、数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110372280114176002.json、音频生成/音频生成/Index TTS 2.5语音合成合集｜高质量音频生成制作_2096747098271207425.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
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
- `PreviewAudio` —— 5/8 个有
- `easy downloadIndexTTSAndLoadModel` —— 5/8 个有
- `easy indexTTSGenerateSimple` —— 5/8 个有
- `T8_IndexTTS25_DialogueGenerate` —— 4/8 个有
- `T8_IndexTTS25_DialogueScript` —— 4/8 个有
- `T8_IndexTTS25_ModelLoader` —— 4/8 个有
- `T8_IndexTTS25_RoleLibrary` —— 4/8 个有
- `T8_IndexTTS25_VoiceProfile` —— 4/8 个有
- `easy indexTTSEmotionVector` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `Fast Groups Muter (rgthree)` —— 2/8 个有
- `T8_IndexTTS25_SamplingConfig` —— 2/8 个有
- `easy indexTTSEmotionMerge` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
