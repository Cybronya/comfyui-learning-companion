---
name: text_to_image_lora_sampler_clip_366
type: Text To Image
frequency: 5
level: strong
coverage: 0.895
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, Float, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_SamplingConfig, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409.json, 数字人/数字人/Index TTS 2.5情感文本控制语音克隆工作流，单人语音生成工具_2106152553548443650.json, 数字人/数字人/IndexTTS 2.5文本控制情感语音克隆｜数字人配音_2105831291030687746.json, 音频生成/音频生成/2608情感文本控制｜IndexTTS 2.5语音克隆音频生成_2095098000753385473.json, 音频生成/音频生成/IndexTTS 2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2106887580888428546.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_366

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/IndexTTS_2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2109099878965137409.json、数字人/数字人/Index TTS 2.5情感文本控制语音克隆工作流，单人语音生成工具_2106152553548443650.json、数字人/数字人/IndexTTS 2.5文本控制情感语音克隆｜数字人配音_2105831291030687746.json、音频生成/音频生成/2608情感文本控制｜IndexTTS 2.5语音克隆音频生成_2095098000753385473.json、音频生成/音频生成/IndexTTS 2.5单人双人情感语音克隆中英文日西语工作流，音频生成_2106887580888428546.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Float`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_SamplingConfig`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `SaveAudio` —— 3/5 个有
- `PixaromaGroupSwitch` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `SaveAudioAdvanced` —— 2/5 个有
- `T8_IndexTTS25_DialogueGenerate` —— 2/5 个有
- `T8_IndexTTS25_DialogueScript` —— 2/5 个有
- `T8_IndexTTS25_RoleLibrary` —— 2/5 个有
- `T8_IndexTTS25_VoiceProfile` —— 2/5 个有
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
