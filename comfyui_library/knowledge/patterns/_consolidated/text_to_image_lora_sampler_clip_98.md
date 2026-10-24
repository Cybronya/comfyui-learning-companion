---
name: text_to_image_lora_sampler_clip_98
type: Text To Image
frequency: 14
level: strong
coverage: 0.864357
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptyMiniMaxMusic3LatentAudio, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxMusic3TextEncode, SaveAudioAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/Music 3开源音乐模型｜Minimax 最长5分钟音乐生成_2089350682552922114.json, 音频生成/音频生成/audio_minimax_music_3音频生成｜智能作曲轻松出曲_2106957865956237314.json, 音频生成/音频生成/minimax music 3音频生成AI音乐创作工作流_2088384149878042626.json, 音频生成/音频生成/minimax music3文生音乐｜AI歌曲创作歌词输入音频生成_2088733796165316610.json, 音频生成/音频生成/支持提示词歌词音乐生成｜MiniMax Music 3音频创作工作流_2088338837742374913.json, 音频生成/音频生成/文生歌曲工作流带时长参数控制注释版｜MiniMax Music3音频生成_2088377461200482306.json, 音频生成/音频生成/文生音频｜Minimax Music3一键音乐生成_2089793683477585922.json, 音频生成/音频生成/迷你音乐音频生成｜MiniMax Music 3工作流_2088389548484153346.json, 音频生成/音频生成/音乐生成minimax music3音频生成作曲编曲演唱一体工作流_2088397731273461762.json, 音频生成/音频生成/音乐生成神器｜Minimax-Music3开源版一键作曲直出_2089441013067767810.json, 音频生成/音频生成/音乐生成音频创作｜minimax_music3工作流_2088373670057172993.json, 音频生成/音频生成/音乐生成音频生成｜MiniMax Music音频创作工作流_2088333780389023746.json, 音频生成/音频生成/音乐生成｜MiniMax Music 一键作曲_2089301127073460225.json, 音频生成/音频生成/音频生成音乐创作｜minimax-music-3工作流_2088355239786274817.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（音频生成/音频生成/Music 3开源音乐模型｜Minimax 最长5分钟音乐生成_2089350682552922114.json、音频生成/音频生成/audio_minimax_music_3音频生成｜智能作曲轻松出曲_2106957865956237314.json、音频生成/音频生成/minimax music 3音频生成AI音乐创作工作流_2088384149878042626.json、音频生成/音频生成/minimax music3文生音乐｜AI歌曲创作歌词输入音频生成_2088733796165316610.json、音频生成/音频生成/支持提示词歌词音乐生成｜MiniMax Music 3音频创作工作流_2088338837742374913.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptyMiniMaxMusic3LatentAudio`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxMusic3TextEncode`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 13/14 个有
- `SeedNode` —— 12/14 个有
- `VAEDecodeAudioTiled` —— 11/14 个有
- `ComfySwitchNode` —— 10/14 个有
- `Float` —— 5/14 个有
- `PreviewAudio` —— 4/14 个有
- `PrimitiveStringMultiline` —— 4/14 个有
- `CR Prompt Text` —— 2/14 个有
- `LoadImage` —— 2/14 个有
- `PrimitiveFloat` —— 2/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `PrimitiveBoolean` —— 1/14 个有
- `PrimitiveInt` —— 1/14 个有
- `easy seed` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
