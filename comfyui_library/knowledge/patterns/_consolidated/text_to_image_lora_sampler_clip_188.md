---
name: text_to_image_lora_sampler_clip_188
type: Text To Image
frequency: 7
level: strong
coverage: 0.884571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Index-tts2 语音克隆｜单人双人对话都能做｜数字人音频生成_2096838123635433473.json, 音频生成/音频生成/Index-tts双人对话语音合成｜数字人音频生成制作_2096644358408851458.json, 音频生成/音频生成/IndexTTS2史上最强音色克隆｜带语气情感生成_2095601584188252161.json, 音频生成/音频生成/IndexTTS2声音克隆情感版｜给配音注入真实情绪_2097211652537147394.json, 音频生成/音频生成/IndexTTS2情感声音克隆｜参考音色秒变同款嗓音_2097209913914249218.json, 音频生成/音频生成/史上最强音色克隆｜IndexTTS2声音克隆数字人音频_2092898751957524481.json, 音频生成/音频生成/音色克隆歌曲翻唱｜Seed-VC数字人音频生成_2089483938376011778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_188

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（音频生成/音频生成/Index-tts2 语音克隆｜单人双人对话都能做｜数字人音频生成_2096838123635433473.json、音频生成/音频生成/Index-tts双人对话语音合成｜数字人音频生成制作_2096644358408851458.json、音频生成/音频生成/IndexTTS2史上最强音色克隆｜带语气情感生成_2095601584188252161.json、音频生成/音频生成/IndexTTS2声音克隆情感版｜给配音注入真实情绪_2097211652537147394.json、音频生成/音频生成/IndexTTS2情感声音克隆｜参考音色秒变同款嗓音_2097209913914249218.json…）

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
- `SaveAudio` —— 5/7 个有
- `AudioCrop` —— 4/7 个有
- `IndexTTS2Run` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `SaveAudioMP3` —— 4/7 个有
- `AudioSeparation` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `String` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `AudioCombine` —— 1/7 个有
- `IndexTTS2EmotionTextNode` —— 1/7 个有
- `IndexTTS2EmotionVectorNode` —— 1/7 个有
- `SeedVCRun` —— 1/7 个有

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
