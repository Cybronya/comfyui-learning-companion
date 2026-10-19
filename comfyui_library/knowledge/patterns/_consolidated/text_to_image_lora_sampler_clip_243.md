---
name: text_to_image_lora_sampler_clip_243
type: Text To Image
frequency: 3
level: strong
coverage: 0.886333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadVideo, LoraLoaderModelOnly, RH_HeyGemNode, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/heygem口播数字人电商带货｜LLM文案Index-TTS2.0声音克隆_2100803633888714753.json, 数字人/数字人/超快HEYGEN数字人口播｜真人形象快速生成制作_2096317248427352065.json, 音频生成/音频生成/Heygem数字人带货对口型｜IndexTTS文字生成音频工作流_2097050749023903746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_243

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/heygem口播数字人电商带货｜LLM文案Index-TTS2.0声音克隆_2100803633888714753.json、数字人/数字人/超快HEYGEN数字人口播｜真人形象快速生成制作_2096317248427352065.json、音频生成/音频生成/Heygem数字人带货对口型｜IndexTTS文字生成音频工作流_2097050749023903746.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `RH_HeyGemNode`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/3 个有
- `IndexTTS2Run` —— 1/3 个有
- `IndexTTSRun` —— 1/3 个有
- `JWStringReplace` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SaveAudio` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
