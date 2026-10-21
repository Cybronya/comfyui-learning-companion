---
name: text_to_image_lora_sampler_clip_179
type: Text To Image
frequency: 7
level: strong
coverage: 0.880143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Heygem真人对口型数字人｜口播长视频快速生成书评国学情感_2110692840987783169.json, 数字人/数字人/IndexTTS2史上最强声音克隆｜音色语气双还原｜数字人配音新选择_2102280819787255810.json, 数字人/数字人/情绪角色配音生成｜数字人语音音频克隆直出_2093828167814443010.json, 数字人/数字人/音色克隆带语气｜IndexTTS2 史上最强声音克隆_2089347718471831553.json, 视频生成/图生视频/真人对口型口播｜Heygem书评国学情感数字人超长视频_2091209074963730434.json, 音频生成/音频生成/Index TTS2加Qwen3 TTS声音克隆二合一，音色语气情感控制音频生成_2105746631021916162.json, 音频生成/音频生成/声音克隆二合一｜Index TTS2+Qwen3 TTS音色参考情感控制_2095297314482118657.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_179

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/Heygem真人对口型数字人｜口播长视频快速生成书评国学情感_2110692840987783169.json、数字人/数字人/IndexTTS2史上最强声音克隆｜音色语气双还原｜数字人配音新选择_2102280819787255810.json、数字人/数字人/情绪角色配音生成｜数字人语音音频克隆直出_2093828167814443010.json、数字人/数字人/音色克隆带语气｜IndexTTS2 史上最强声音克隆_2089347718471831553.json、视频生成/图生视频/真人对口型口播｜Heygem书评国学情感数字人超长视频_2091209074963730434.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `AudioCrop` —— 6/7 个有
- `IndexTTS2Run` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `SaveAudioMP3` —— 4/7 个有
- `Apply Whisper` —— 2/7 个有
- `CreateVideo` —— 2/7 个有
- `FB_Qwen3TTSVoiceClone` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `RH_HeyGemNode` —— 2/7 个有
- `SaveVideo` —— 2/7 个有
- `Text` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `SaveAudio` —— 1/7 个有
- `SaveAudioAdvanced` —— 1/7 个有
- `忽略多组孤海` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
