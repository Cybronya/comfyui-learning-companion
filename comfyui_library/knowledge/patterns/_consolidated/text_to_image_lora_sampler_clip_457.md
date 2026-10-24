---
name: text_to_image_lora_sampler_clip_457
type: Text To Image
frequency: 4
level: strong
coverage: 0.89725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/heygem口播数字人电商带货｜LLM文案Index-TTS2.0声音克隆_2100803633888714753.json, 数字人/数字人/超快HEYGEN数字人口播｜真人形象快速生成制作_2096317248427352065.json, 音频生成/音频生成/Index-tts2 语音克隆｜单人双人对话都能做｜数字人音频生成_2096838123635433473.json, 音频生成/音频生成/Index-tts双人对话语音合成｜数字人音频生成制作_2096644358408851458.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_457

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/heygem口播数字人电商带货｜LLM文案Index-TTS2.0声音克隆_2100803633888714753.json、数字人/数字人/超快HEYGEN数字人口播｜真人形象快速生成制作_2096317248427352065.json、音频生成/音频生成/Index-tts2 语音克隆｜单人双人对话都能做｜数字人音频生成_2096838123635433473.json、音频生成/音频生成/Index-tts双人对话语音合成｜数字人音频生成制作_2096644358408851458.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
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
- `IndexTTS2Run` —— 3/4 个有
- `SaveAudio` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `AudioSeparation` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `RH_HeyGemNode` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `String` —— 2/4 个有
- `JWStringReplace` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
