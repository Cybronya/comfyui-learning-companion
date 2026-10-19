---
name: text_to_image_lora_sampler_clip_98
type: Text To Image
frequency: 9
level: strong
coverage: 0.902556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, T8_BreezeTTS_Generate, T8_BreezeTTS_GenerationSettings, T8_BreezeTTS_ModelLoader, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/声音克隆上传参考音频生成语音数字人处理工具_2101412401496285186.json, 视频生成/文生视频/Breeze_TTS_2声音导演工作流，视频生视频音频生成处理工具_2107329668998320130.json, 视频生成/文生视频/Breeze_TTS_2声音导演工作流，视频生视频音频生成处理工具_2107441806513369089.json, 音频生成/音频生成/Breeze TTS 2声音设计 AI语音克隆音频生成_2098859602187210753.json, 音频生成/音频生成/Breeze TTS 2声音设计工作流｜一句话定制专属数字人音色｜音频生成_2099141974749179905.json, 音频生成/音频生成/Breeze TTS2 Clone语音克隆工作流，音频生成工具_2106527599907393538.json, 音频生成/音频生成/Breeze TTS2声音设计工作流｜音频生成自定义音色_2108419117261873153.json, 音频生成/音频生成/Breeze-TTS2-Clone声音克隆｜音频生成复刻音色超像_2106271449236459521.json, 音频生成/音频生成/开源TTS标杆｜Breeze 2高质量声音设计生成_2096571329003741185.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/声音克隆上传参考音频生成语音数字人处理工具_2101412401496285186.json、视频生成/文生视频/Breeze_TTS_2声音导演工作流，视频生视频音频生成处理工具_2107329668998320130.json、视频生成/文生视频/Breeze_TTS_2声音导演工作流，视频生视频音频生成处理工具_2107441806513369089.json、音频生成/音频生成/Breeze TTS 2声音设计 AI语音克隆音频生成_2098859602187210753.json、音频生成/音频生成/Breeze TTS 2声音设计工作流｜一句话定制专属数字人音色｜音频生成_2099141974749179905.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `T8_BreezeTTS_Generate`
- `T8_BreezeTTS_GenerationSettings`
- `T8_BreezeTTS_ModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 7/9 个有
- `孤海注释` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `Apply Whisper` —— 5/9 个有
- `LoadAudio` —— 5/9 个有
- `T8_BreezeTTS_DesignRequest` —— 4/9 个有
- `T8_BreezeTTS_CloneRequest` —— 3/9 个有
- `EmptyImage` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `PreviewAudio` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `SaveAudioMP3` —— 2/9 个有
- `T8_BreezeTTS_DirectionRequest` —— 2/9 个有
- `MuyeTextEditOutput` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
