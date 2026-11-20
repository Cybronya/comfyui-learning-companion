---
name: text_to_image_lora_sampler_clip_240
type: Text To Image
frequency: 8
level: strong
coverage: 0.87825
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Fish Audio S2 TTS｜单人语音克隆实操｜录一段声音就能让他替你说话_2102571193546133506.json, 图片生成/图生图/Index TTS2声音克隆史上最强音色克隆带语气，音频生成工具_2106132641341861889.json, 图片生成/图生图/配音声音克隆IndexTTS2工作流｜高质量语音复刻生成_2097059623751733250.json, 数字人/数字人/IndexTTS2史上最强声音克隆｜音色语气双还原｜数字人配音新选择_2102280819787255810.json, 数字人/数字人/情绪角色配音生成｜数字人语音音频克隆直出_2093828167814443010.json, 数字人/数字人/音色克隆带语气｜IndexTTS2 史上最强声音克隆_2089347718471831553.json, 音频生成/音频生成/Index TTS2加Qwen3 TTS声音克隆二合一，音色语气情感控制音频生成_2105746631021916162.json, 音频生成/音频生成/声音克隆二合一｜Index TTS2+Qwen3 TTS音色参考情感控制_2095297314482118657.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_240

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Fish Audio S2 TTS｜单人语音克隆实操｜录一段声音就能让他替你说话_2102571193546133506.json、图片生成/图生图/Index TTS2声音克隆史上最强音色克隆带语气，音频生成工具_2106132641341861889.json、图片生成/图生图/配音声音克隆IndexTTS2工作流｜高质量语音复刻生成_2097059623751733250.json、数字人/数字人/IndexTTS2史上最强声音克隆｜音色语气双还原｜数字人配音新选择_2102280819787255810.json、数字人/数字人/情绪角色配音生成｜数字人语音音频克隆直出_2093828167814443010.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `IndexTTS2Run` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `SaveAudioMP3` —— 6/8 个有
- `AudioCrop` —— 5/8 个有
- `SaveAudio` —— 3/8 个有
- `Text` —— 3/8 个有
- `Apply Whisper` —— 2/8 个有
- `FB_Qwen3TTSVoiceClone` —— 2/8 个有
- `PreviewAudio` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `FishS2VoiceCloneTTS` —— 1/8 个有
- `LoadWhisperModel_` —— 1/8 个有
- `SaveAudioAdvanced` —— 1/8 个有
- `WhisperTranscribe_` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
