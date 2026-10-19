---
name: text_to_image_lora_sampler_clip_211
type: Text To Image
frequency: 4
level: strong
coverage: 0.82975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Qwen3TTS声音克隆剪辑后期补救音频生成处理工具_2101729163018326017.json, 音频生成/音频生成/VOXCPM2声音克隆语音克隆 音色复刻音频生成_2104716560517656577.json, 音频生成/音频生成/VoxCPM2基础工作流｜语音合成音频生成_2095137648078839810.json, 音频生成/音频生成/VoxCPM2基础工作流｜音频生成语音合成处理_2095112468350717954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_211

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3TTS声音克隆剪辑后期补救音频生成处理工具_2101729163018326017.json、音频生成/音频生成/VOXCPM2声音克隆语音克隆 音色复刻音频生成_2104716560517656577.json、音频生成/音频生成/VoxCPM2基础工作流｜语音合成音频生成_2095137648078839810.json、音频生成/音频生成/VoxCPM2基础工作流｜音频生成语音合成处理_2095112468350717954.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

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
- `RunningHub_VoxCPM_Generate` —— 3/4 个有
- `RunningHub_VoxCPM_LoadModel` —— 3/4 个有
- `SaveAudio` —— 3/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Qwen3ASRLoader` —— 2/4 个有
- `Qwen3ASRTranscribe` —— 2/4 个有
- `AudioCrop` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LongCatVoiceCloneTTS` —— 1/4 个有
- `NormalizeAudioLoudness` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `SaveAudioMP3` —— 1/4 个有
- `SetNode` —— 1/4 个有

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
