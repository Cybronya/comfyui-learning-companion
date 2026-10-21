---
name: text_to_image_lora_sampler_clip_156
type: Text To Image
frequency: 8
level: strong
coverage: 0.8275
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveAudioAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/YuE2 AI歌曲制作四合一文生翻唱改词音频处理工具_2102538511558729729.json, 音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109370620222992385.json, 音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109375224738308098.json, 音频生成/音频生成/YuE2音乐翻唱堪比闭源模型的开源工作流，音频生成音乐翻唱工具_2107551333124497410.json, 音频生成/音频生成/YuE2音乐翻唱音频生成方案高质量稳定 音频生成方案_2109757822031450113.json, 音频生成/音频生成/Yue2 AI歌曲制作多合一，文生歌曲翻唱改词音频生成工作流_2103240173130706945.json, 音频生成/音频生成/Yue2最强AI歌曲制作四合一，文生翻唱改词音频生成工作流_2103904945815773186.json, 音频生成/音频生成/Yue2最强AI歌曲四合一工作站｜文生翻唱改词音频一步到位_2103683344578990082.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（音频生成/音频生成/YuE2 AI歌曲制作四合一文生翻唱改词音频处理工具_2102538511558729729.json、音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109370620222992385.json、音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109375224738308098.json、音频生成/音频生成/YuE2音乐翻唱堪比闭源模型的开源工作流，音频生成音乐翻唱工具_2107551333124497410.json、音频生成/音频生成/YuE2音乐翻唱音频生成方案高质量稳定 音频生成方案_2109757822031450113.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptyYuE2LatentAudio`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioEncoderLoader` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `PreviewAudio` —— 4/8 个有
- `RH_Screenwriter` —— 4/8 个有
- `SeedNode` —— 4/8 个有
- `SheetSage2AudioToABC` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `YuE2ReferenceVoiceCover` —— 4/8 个有
- `JWStringToFloat` —— 3/8 个有
- `WujiYue2Lyricist` —— 3/8 个有
- `YuE2ModelLoader` —— 3/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `WujiLyricist3` —— 1/8 个有
- `YuE2CoverTranscribe` —— 1/8 个有
- `YuE2GenerateABC` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
