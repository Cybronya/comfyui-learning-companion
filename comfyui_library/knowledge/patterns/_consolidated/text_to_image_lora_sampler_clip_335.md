---
name: text_to_image_lora_sampler_clip_335
type: Text To Image
frequency: 3
level: strong
coverage: 0.872333
common_nodes: [AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, SaveAudioAdvanced, SheetSage2AudioToABC, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/yue2翻唱工作流｜音频生成一键翻唱｜你的声音唱热门歌曲_2104807379912183809.json, 音频生成/音频生成/音乐翻唱YuE2工作流，音频生成音乐翻唱处理工具_2107536345215361026.json, 音频生成/音频生成/音乐翻唱神器｜YUE2音频生成，一键翻唱任意歌曲_2099895460818411522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_335

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/yue2翻唱工作流｜音频生成一键翻唱｜你的声音唱热门歌曲_2104807379912183809.json、音频生成/音频生成/音乐翻唱YuE2工作流，音频生成音乐翻唱处理工具_2107536345215361026.json、音频生成/音频生成/音乐翻唱神器｜YUE2音频生成，一键翻唱任意歌曲_2099895460818411522.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `EmptyYuE2LatentAudio`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `SaveAudioAdvanced`
- `SheetSage2AudioToABC`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `Audio Duration` —— 1/3 个有
- `AudioCrop` —— 1/3 个有
- `AudioSeparation` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Qwen3ASRLoader` —— 1/3 个有
- `Qwen3ASRTranscribe` —— 1/3 个有
- `SeedNode` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
