---
name: text_to_image_lora_sampler_clip_279
type: Text To Image
frequency: 4
level: strong
coverage: 0.8665
common_nodes: [Apply Whisper, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, SaveAudio, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110250401802047489.json, 音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110364673857114114.json, 音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音数字人音频生成_2087396027186900994.json, 音频生成/音频生成/声音克隆Qwen3 TTS 音色复刻方案_2109779921815031809.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_279

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110250401802047489.json、音频生成/音频生成/Qwen3 TTS声音克隆音色复刻 语音生成定制方案_2110364673857114114.json、音频生成/音频生成/Qwen3 TTS语音克隆-一键克隆声音数字人音频生成_2087396027186900994.json、音频生成/音频生成/声音克隆Qwen3 TTS 音色复刻方案_2109779921815031809.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `Apply Whisper`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `SaveAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `AudioSeparation` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Float` —— 1/4 个有
- `HeartMuLa_Transcribe` —— 1/4 个有
- `Int` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `ShowAnything|Mie` —— 1/4 个有
- `ShowText` —— 1/4 个有

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
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
