---
name: text_to_image_lora_sampler_clip_44
type: Text To Image
frequency: 19
level: strong
coverage: 0.896368
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, YuE2Generate, YuE2Loader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/YuE2改词翻唱_AI音乐改编_自定义歌词翻唱生成_2107324972157988866.json, 图片生成/文生图/YuE2改词翻唱_AI音乐改编_自定义歌词翻唱生成_2107438753290739713.json, 图片生成/文生图/YuE2翻唱原音改词_音频翻唱创作处理工具_2100745866029129730.json, 图片生成/文生图/YuE2翻唱原音改词_音频翻唱创作处理工具_2101457073044279297.json, 图片生成/文生图/YuE2翻唱原音改词_音频翻唱创作处理工具_2102593195208175617.json, 音频生成/音频生成/(自用品质)YuE2改词翻唱 AI音乐改编 自定义歌词翻唱生成_2107275656441712641.json, 音频生成/音频生成/YuE2 AI文生音乐流｜一句话生成专属背景音乐_2098738092327923714.json, 音频生成/音频生成/YuE2 AI翻唱工作流｜音频生成一键换声翻唱_2098736905457332225.json, 音频生成/音频生成/YuE2 AI翻唱工作流｜音频生成一键翻唱音色媲美原唱_2106255040204861441.json, 音频生成/音频生成/YuE2改词翻唱 AI音乐改编 自定义歌词翻唱生成_2098858058809171969.json, 音频生成/音频生成/YuE2改词翻唱不改曲 AI音乐改编音频生成_2110362171585683458.json, 音频生成/音频生成/YuE2文本生成音乐｜AI作曲一键出完整歌曲_2106572307480272898.json, 音频生成/音频生成/YuE2文生音乐 AI音频生成工作流音乐创作_2098714587007905793.json, 音频生成/音频生成/YuE2文生音乐 AI音频生成工作流音乐创作_2099031790064328705.json, 音频生成/音频生成/YuE2文生音乐工作流，音频生成文本到音乐创作工具_2107590188829601793.json, 音频生成/音频生成/YuE2文生音乐工作流｜文字描述直接生成歌曲_2098704608779657217.json, 音频生成/音频生成/YuE2文生音乐生成流｜一句话歌词直出完整歌曲_2108096959977451522.json, 音频生成/音频生成/YuE2文生音乐自用版｜输入文字一键生成原创音频，音乐创作好帮手_2107286323588587521.json, 音频生成/音频生成/YuE2翻唱原音改词 音频翻唱创作处理工具_2099953122658570241.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/文生图/YuE2改词翻唱_AI音乐改编_自定义歌词翻唱生成_2107324972157988866.json、图片生成/文生图/YuE2改词翻唱_AI音乐改编_自定义歌词翻唱生成_2107438753290739713.json、图片生成/文生图/YuE2翻唱原音改词_音频翻唱创作处理工具_2100745866029129730.json、图片生成/文生图/YuE2翻唱原音改词_音频翻唱创作处理工具_2101457073044279297.json、图片生成/文生图/YuE2翻唱原音改词_音频翻唱创作处理工具_2102593195208175617.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `YuE2Generate`
- `YuE2Loader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `YuE2SamplingConfig` —— 17/19 个有
- `CR Prompt Text` —— 15/19 个有
- `SaveAudio` —— 15/19 个有
- `孤海注释` —— 14/19 个有
- `YuE2CoverTranscribe` —— 11/19 个有
- `LoadAudio` —— 10/19 个有
- `PreviewAny` —— 10/19 个有
- `EmptyImage` —— 5/19 个有
- `PreviewImage` —— 5/19 个有
- `SaveAudioAdvanced` —— 4/19 个有
- `MusicPlayerWithLyricsNode` —— 3/19 个有
- `VHS_LoadAudioUpload` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（20/19 个样本）：Steps较低可能导致细节不足
