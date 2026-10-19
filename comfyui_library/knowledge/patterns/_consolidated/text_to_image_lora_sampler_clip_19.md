---
name: text_to_image_lora_sampler_clip_19
type: Text To Image
frequency: 20
level: strong
coverage: 0.8887
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, T8_IndexTTS25_Generate, T8_IndexTTS25_ModelLoader, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769.json, 音频生成/音频生成/IndexTTS 2.5情感参考语音克隆｜音频生成音色复刻_2089398689801523202.json, 音频生成/音频生成/IndexTTS 2.5情感文本语音克隆｜音频生成工作流_2089394591563870210.json, 音频生成/音频生成/IndexTTS 2.5语音克隆V3 数字人音频生成工具_2098700870958534658.json, 音频生成/音频生成/IndexTTS 2.5语音克隆｜情感文本控制音色复刻_2095130769411895298.json, 音频生成/音频生成/IndexTTS 2.5语音克隆｜音色复刻高质量音频生成_2095136179296497665.json, 音频生成/音频生成/IndexTTS2.5多情绪控制语音克隆｜音频生成情感配音_2108385358328197122.json, 音频生成/音频生成/声音克隆 IndexTTS25｜音频生成简单易用效果出色_2096846725301497857.json, 音频生成/音频生成/声音克隆IndexTTS25｜高保真语音复刻音频生成_2096687203647836162.json, 音频生成/音频生成/声音克隆音色参考加情感语气控制IndexTTS 2.5 音色复刻方案_2109405575187619842.json, 音频生成/音频生成/声音克隆音色参考加情感语气控制IndexTTS 2.5 音色复刻方案_2109750095381090306.json, 音频生成/音频生成/情感参考克隆｜IndexTTS 2.5语音音频生成_2093726811753631745.json, 音频生成/音频生成/情感参考声音克隆｜IndexTTS 2.5语音音频生成_2093541875406958593.json, 音频生成/音频生成/情感向量控制｜IndexTTS 2.5语音克隆生成_2093728163061915649.json, 音频生成/音频生成/情感向量控制｜IndexTTS 2.5语音克隆音频生成_2092929322012200961.json, 音频生成/音频生成/情感文本语音克隆｜IndexTTS 2.5音频生成_2093725534109917185.json, 音频生成/音频生成/情感文本音色克隆｜IndexTTS 2.5语音生成_2093408070805319681.json, 音频生成/音频生成/长文本语音克隆｜IndexTTS 2.5音色复刻音频生成_2093406742762835970.json, 音频生成/音频生成/长文本语音克隆｜IndexTTS 2.5音频一键生成_2093724260756975617.json, 音频生成/音频生成/音频向量语音克隆｜IndexTTS2.5音色克隆生成_2092926388964773890.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（音频生成/音频生成/IndexTTS 2.5多音字语音克隆｜中文版多发音支持音频生成_2090445429296160769.json、音频生成/音频生成/IndexTTS 2.5情感参考语音克隆｜音频生成音色复刻_2089398689801523202.json、音频生成/音频生成/IndexTTS 2.5情感文本语音克隆｜音频生成工作流_2089394591563870210.json、音频生成/音频生成/IndexTTS 2.5语音克隆V3 数字人音频生成工具_2098700870958534658.json、音频生成/音频生成/IndexTTS 2.5语音克隆｜情感文本控制音色复刻_2095130769411895298.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_ModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 18/20 个有
- `T8_IndexTTS25_EmotionControl` —— 15/20 个有
- `Float` —— 13/20 个有
- `SaveAudioMP3` —— 11/20 个有
- `NormalizeAudioLoudness` —— 9/20 个有
- `SaveAudio` —— 9/20 个有
- `T8_IndexTTS25_SamplingConfig` —— 5/20 个有
- `PrimitiveStringMultiline` —— 2/20 个有
- `T8_IndexTTS25_Pronunciation` —— 2/20 个有
- `T8_IndexTTS25_TextPreview` —— 2/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（21/20 个样本）：Steps较低可能导致细节不足
