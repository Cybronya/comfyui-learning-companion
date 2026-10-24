---
name: text_to_image_lora_sampler_clip_387
type: Text To Image
frequency: 5
level: strong
coverage: 0.8652
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/MegaTTS3音色合成朗读｜海量音色库文本转语音_2106565766538682370.json, 音频生成/音频生成/MegaTTS3音色库朗读｜音色合成语音生成工作流_2095145581671968769.json, 音频生成/音频生成/MiniMax HD文本转语音｜高清音质朗读自然不机械_2097221464729669634.json, 音频生成/音频生成/MiniMax音色设计AI配音 一句话生成专业配音_2098863846709616641.json, 音频生成/音频生成/OmniVoice声音设计，600种语言支持方言的音频生成_2110470753425641474.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_387

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（音频生成/音频生成/MegaTTS3音色合成朗读｜海量音色库文本转语音_2106565766538682370.json、音频生成/音频生成/MegaTTS3音色库朗读｜音色合成语音生成工作流_2095145581671968769.json、音频生成/音频生成/MiniMax HD文本转语音｜高清音质朗读自然不机械_2097221464729669634.json、音频生成/音频生成/MiniMax音色设计AI配音 一句话生成专业配音_2098863846709616641.json、音频生成/音频生成/OmniVoice声音设计，600种语言支持方言的音频生成_2110470753425641474.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 4/5 个有
- `SaveAudioMP3` —— 3/5 个有
- `MegaTTS3` —— 2/5 个有
- `SaveAudio` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `OmniVoiceVoiceDesignTTS` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `RH_MinimaxVoiceDesign` —— 1/5 个有
- `RH_RhartAudioTextToAudioSpeech28Hd` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
