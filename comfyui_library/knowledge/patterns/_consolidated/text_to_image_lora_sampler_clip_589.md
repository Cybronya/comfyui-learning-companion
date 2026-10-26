---
name: text_to_image_lora_sampler_clip_589
type: Text To Image
frequency: 3
level: strong
coverage: 0.841667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadAudio, LongCatVoiceCloneTTS, LoraLoaderModelOnly, NormalizeAudioLoudness, Qwen3ASRLoader, Qwen3ASRTranscribe, SaveAudioMP3, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/LongCat语音克隆 真实自然语音合成音频生成工具_2114063226567749634.json, 音频生成/音频生成/LongCat语音克隆工作流｜音频生成克隆音色超像_2114055166155640833.json, 音频生成/音频生成/Qwen3TTS声音克隆剪辑后期补救音频生成处理工具_2101729163018326017.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_589

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/LongCat语音克隆 真实自然语音合成音频生成工具_2114063226567749634.json、音频生成/音频生成/LongCat语音克隆工作流｜音频生成克隆音色超像_2114055166155640833.json、音频生成/音频生成/Qwen3TTS声音克隆剪辑后期补救音频生成处理工具_2101729163018326017.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LongCatVoiceCloneTTS`
- `LoraLoaderModelOnly`
- `NormalizeAudioLoudness`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `SaveAudioMP3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudioUI` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Note _O` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
