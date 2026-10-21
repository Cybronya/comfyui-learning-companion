---
name: text_to_image_lora_sampler_clip_332
type: Text To Image
frequency: 3
level: strong
coverage: 0.867667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/电商友好型Seedance2.0多参视频生成｜平价好用_2095291656303104002.json, 音频生成/音频生成/indexTTS2高保真语音克隆｜文本转语音音色复刻_2089443854935220225.json, 音频生成/音频生成/多人音色克隆情绪TTS｜VOXCPM2.0音频自动生成_2092613191384780802.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_332

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/电商友好型Seedance2.0多参视频生成｜平价好用_2095291656303104002.json、音频生成/音频生成/indexTTS2高保真语音克隆｜文本转语音音色复刻_2089443854935220225.json、音频生成/音频生成/多人音色克隆情绪TTS｜VOXCPM2.0音频自动生成_2092613191384780802.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CR Text` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `IndexTTS2_Basic` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `Seedance_Config` —— 1/3 个有
- `Seedance_MultimodalVideo` —— 1/3 个有
- `WujiVoiceActorVoxCPM` —— 1/3 个有

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
