---
name: text_to_image_lora_sampler_clip_134
type: Text To Image
frequency: 7
level: strong
coverage: 0.858714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/IndexTTS2史上最强声音克隆｜音色语气双还原｜数字人配音新选择_2102280819787255810.json, 数字人/数字人/情绪角色配音生成｜数字人语音音频克隆直出_2093828167814443010.json, 数字人/数字人/音色克隆带语气｜IndexTTS2 史上最强声音克隆_2089347718471831553.json, 音频生成/音频生成/AI配音工作流｜一句话描述音色自动生成创意玩法_2100831844735471617.json, 音频生成/音频生成/FireRed TTS语音克隆｜参考音色复刻工作流_2094566446364979201.json, 音频生成/音频生成/FireRed语音理解AI问答｜听音识别智能对话_2094565126929215490.json, 音频生成/音频生成/IndexTTS2史上最强音色克隆｜带语气情感生成_2095601584188252161.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_134

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/IndexTTS2史上最强声音克隆｜音色语气双还原｜数字人配音新选择_2102280819787255810.json、数字人/数字人/情绪角色配音生成｜数字人语音音频克隆直出_2093828167814443010.json、数字人/数字人/音色克隆带语气｜IndexTTS2 史上最强声音克隆_2089347718471831553.json、音频生成/音频生成/AI配音工作流｜一句话描述音色自动生成创意玩法_2100831844735471617.json、音频生成/音频生成/FireRed TTS语音克隆｜参考音色复刻工作流_2094566446364979201.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `IndexTTS2Run` —— 4/7 个有
- `SaveAudioMP3` —— 4/7 个有
- `AudioCrop` —— 3/7 个有
- `RH_FireRedAudioLoader` —— 3/7 个有
- `SaveAudio` —— 2/7 个有
- `SaveAudioAdvanced` —— 2/7 个有
- `RH_FireRedAudioTTS` —— 1/7 个有
- `RH_FireRedAudioUnderstand` —— 1/7 个有
- `RH_FireRedAudioVoiceDesign` —— 1/7 个有
- `SaveText` —— 1/7 个有

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
