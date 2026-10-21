---
name: text_to_image_lora_sampler_clip_120
type: Text To Image
frequency: 9
level: strong
coverage: 0.901778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Index TTS 2.5情感文本控制语音克隆工作流，单人语音生成工具_2106152553548443650.json, 数字人/数字人/IndexTTS 2.5文本控制情感语音克隆｜数字人配音_2105831291030687746.json, 数字人/数字人/IndexTTS2声线克隆 音色复刻音频生成方案_2108611918436069378.json, 数字人/数字人/IndexTTS2声线克隆神器｜一键复刻原声的数字人配音工作流_2108367981469323266.json, 数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110245936260796418.json, 数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110372280114176002.json, 音频生成/音频生成/2608情感文本控制｜IndexTTS 2.5语音克隆音频生成_2095098000753385473.json, 音频生成/音频生成/Index TTS 2.5语音合成合集｜高质量音频生成制作_2096747098271207425.json, 音频生成/音频生成/IndexTTS 2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2106887580888428546.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/Index TTS 2.5情感文本控制语音克隆工作流，单人语音生成工具_2106152553548443650.json、数字人/数字人/IndexTTS 2.5文本控制情感语音克隆｜数字人配音_2105831291030687746.json、数字人/数字人/IndexTTS2声线克隆 音色复刻音频生成方案_2108611918436069378.json、数字人/数字人/IndexTTS2声线克隆神器｜一键复刻原声的数字人配音工作流_2108367981469323266.json、数字人/数字人/TTS2声音克隆加情感参考 音色复刻自然方案_2110245936260796418.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `PreviewAudio` —— 6/9 个有
- `T8_IndexTTS25_ModelLoader` —— 5/9 个有
- `easy downloadIndexTTSAndLoadModel` —— 5/9 个有
- `easy indexTTSGenerateSimple` —— 5/9 个有
- `Float` —— 4/9 个有
- `T8_IndexTTS25_EmotionControl` —— 4/9 个有
- `T8_IndexTTS25_Generate` —— 4/9 个有
- `T8_IndexTTS25_SamplingConfig` —— 4/9 个有
- `easy indexTTSEmotionVector` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 2/9 个有
- `T8_IndexTTS25_DialogueGenerate` —— 2/9 个有
- `T8_IndexTTS25_DialogueScript` —— 2/9 个有
- `T8_IndexTTS25_RoleLibrary` —— 2/9 个有
- `T8_IndexTTS25_VoiceProfile` —— 2/9 个有
- `easy indexTTSEmotionMerge` —— 2/9 个有
- `PixaromaGroupSwitch` —— 1/9 个有
- `SaveAudioAdvanced` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
