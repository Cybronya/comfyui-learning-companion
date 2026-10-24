---
name: text_to_image_lora_sampler_clip_466
type: Text To Image
frequency: 4
level: strong
coverage: 0.89925
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PreviewAudio, SaveAudioAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/多人对话音色一键克隆｜Breeze TTS 2 九月音频生成强档_2096195742212902913.json, 音频生成/音频生成/腾讯Auk秒级音色复刻16项功能合一支持提示词增强_2100656204337991682.json, 音频生成/音频生成/音乐分离人声伴奏低音鼓点工作流，音频生成音乐分离处理工具_2106520036323184642.json, 音频生成/音频生成/音乐分离神器｜人声伴奏低音鼓点一键拆分音频生成_2106243974917877761.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_466

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/多人对话音色一键克隆｜Breeze TTS 2 九月音频生成强档_2096195742212902913.json、音频生成/音频生成/腾讯Auk秒级音色复刻16项功能合一支持提示词增强_2100656204337991682.json、音频生成/音频生成/音乐分离人声伴奏低音鼓点工作流，音频生成音乐分离处理工具_2106520036323184642.json、音频生成/音频生成/音乐分离神器｜人声伴奏低音鼓点一键拆分音频生成_2106243974917877761.json）

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
- `LoraLoaderModelOnly`
- `PreviewAudio`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `AudioSeparation` —— 2/4 个有
- `AuKGenerateEdit_Doc` —— 1/4 个有
- `AuKLlamaCppSettings_Doc` —— 1/4 个有
- `AuKModelsLoader_Doc` —— 1/4 个有
- `BreezeTTS2LoadModel` —— 1/4 个有
- `BreezeTTS2MultiSpeaker` —— 1/4 个有
- `BreezeTTS2Speaker` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

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
