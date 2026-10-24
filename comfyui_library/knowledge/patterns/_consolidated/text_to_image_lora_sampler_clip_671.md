---
name: text_to_image_lora_sampler_clip_671
type: Text To Image
frequency: 2
level: weak
coverage: 0.7845
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, Qwen3ASRLoader, Qwen3ASRTranscribe, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Qwen3TTS声音克隆剪辑后期补救音频生成处理工具_2101729163018326017.json, 音频生成/音频生成/VOXCPM2声音克隆语音克隆 音色复刻音频生成_2104716560517656577.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_671

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3TTS声音克隆剪辑后期补救音频生成处理工具_2101729163018326017.json、音频生成/音频生成/VOXCPM2声音克隆语音克隆 音色复刻音频生成_2104716560517656577.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `LongCatVoiceCloneTTS` —— 1/2 个有
- `NormalizeAudioLoudness` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `RunningHub_VoxCPM_Generate` —— 1/2 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `SaveAudioMP3` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
