---
name: text_to_image_lora_sampler_clip_280
type: Text To Image
frequency: 4
level: strong
coverage: 0.83675
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveAudioAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109855265834225666.json, 音频生成/音频生成/YuE2文生音乐音乐生成 音频创作处理工具_2100670555014914049.json, 音频生成/音频生成/YuE2翻唱音乐生成 音频创作处理工具_2100672410268823554.json, 音频生成/音频生成/音乐翻唱工作流｜上传歌曲一键换风格音频生成_2100833449119674370.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_280

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3 TTS语音生成音色设计 音色复刻方案_2109855265834225666.json、音频生成/音频生成/YuE2文生音乐音乐生成 音频创作处理工具_2100670555014914049.json、音频生成/音频生成/YuE2翻唱音乐生成 音频创作处理工具_2100672410268823554.json、音频生成/音频生成/音乐翻唱工作流｜上传歌曲一键换风格音频生成_2100833449119674370.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `LoadAudio` —— 2/4 个有
- `YuE2Generate` —— 2/4 个有
- `YuE2Loader` —— 2/4 个有
- `YuE2SamplingConfig` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_MinimaxMusicCover` —— 1/4 个有
- `YuE2CoverTranscribe` —— 1/4 个有

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
