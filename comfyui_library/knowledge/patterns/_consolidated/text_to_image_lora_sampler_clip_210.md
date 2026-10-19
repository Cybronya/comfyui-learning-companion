---
name: text_to_image_lora_sampler_clip_210
type: Text To Image
frequency: 4
level: strong
coverage: 0.8935
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, SaveAudio, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/IndexTTS2.5多角色配音工作流｜SRT剧本自动语音合成_2097427732920619009.json, 音频生成/音频生成/Qwen3TTS声音设计工作流｜音频生成新选择 配音音效一站搞定_2105566645342265345.json, 音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json, 音频生成/音频生成/index TTS 2.5双人对话 音频生成方案_2109721870319837185.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_210

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/IndexTTS2.5多角色配音工作流｜SRT剧本自动语音合成_2097427732920619009.json、音频生成/音频生成/Qwen3TTS声音设计工作流｜音频生成新选择 配音音效一站搞定_2105566645342265345.json、音频生成/音频生成/TTS2.5双人对话工作流，音频生成语音合成处理工具_2107566962367885313.json、音频生成/音频生成/index TTS 2.5双人对话 音频生成方案_2109721870319837185.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `T8_IndexTTS25_DialogueGenerate` —— 3/4 个有
- `T8_IndexTTS25_DialogueScript` —— 3/4 个有
- `T8_IndexTTS25_ModelLoader` —— 3/4 个有
- `T8_IndexTTS25_RoleLibrary` —— 3/4 个有
- `T8_IndexTTS25_VoiceProfile` —— 3/4 个有
- `T8_IndexTTS25_SamplingConfig` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Qwen3TTSModelLoader` —— 1/4 个有
- `Qwen3TTSVoiceDesign` —— 1/4 个有

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
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
