---
name: text_to_image_lora_sampler_clip_496
type: Text To Image
frequency: 4
level: strong
coverage: 0.9045
common_nodes: [AudioSeparation, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/我是歌手翻唱一切歌曲 自制声音模型音频生成工具_2113373218257068033.json, 音频生成/音频生成/音乐分离人声伴奏低音鼓点工作流，音频生成音乐分离处理工具_2106520036323184642.json, 音频生成/音频生成/音乐分离神器｜人声伴奏低音鼓点一键拆分音频生成_2106243974917877761.json, 音频生成/音频生成/音色克隆歌曲翻唱｜Seed-VC数字人音频生成_2089483938376011778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_496

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/我是歌手翻唱一切歌曲 自制声音模型音频生成工具_2113373218257068033.json、音频生成/音频生成/音乐分离人声伴奏低音鼓点工作流，音频生成音乐分离处理工具_2106520036323184642.json、音频生成/音频生成/音乐分离神器｜人声伴奏低音鼓点一键拆分音频生成_2106243974917877761.json、音频生成/音频生成/音色克隆歌曲翻唱｜Seed-VC数字人音频生成_2089483938376011778.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
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
- `AudioCrop` —— 3/4 个有
- `SaveAudioAdvanced` —— 3/4 个有
- `PreviewAudio` —— 2/4 个有
- `SaveAudio` —— 2/4 个有
- `AFL:AudioMixStems` —— 1/4 个有
- `AudioCombine` —— 1/4 个有
- `RunningHubRVCVoiceConversion` —— 1/4 个有
- `RunningHubRVCZipModelLoader` —— 1/4 个有
- `SeedVCRun` —— 1/4 个有

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
