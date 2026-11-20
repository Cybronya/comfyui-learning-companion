---
name: text_to_image_lora_sampler_clip_278
type: Text To Image
frequency: 8
level: strong
coverage: 0.82
common_nodes: [AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoadAudio, LoraLoaderModelOnly, PreviewAny, SaveAudioAdvanced, SeedNode, SheetSage2AudioToABC, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109370620222992385.json, 音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109375224738308098.json, 音频生成/音频生成/YuE2音乐翻唱ComfyUI官方版音频生成处理工作流_2101391122361839617.json, 音频生成/音频生成/YuE2音乐翻唱堪比闭源模型的开源工作流，音频生成音乐翻唱工具_2107551333124497410.json, 音频生成/音频生成/YuE2音乐翻唱音频生成方案高质量稳定 音频生成方案_2109757822031450113.json, 音频生成/音频生成/Yue2音乐翻唱官方工作流，音频生成音乐翻唱处理工具_2107246415910105090.json, 音频生成/音频生成/audio_yue2_music_cover音频生成｜AI翻唱一键搞定_2106987749390770177.json, 音频生成/音频生成/音乐翻唱YuE2工作流，音频生成音乐翻唱处理工具_2107536345215361026.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_278

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109370620222992385.json、音频生成/音频生成/YuE2音乐翻唱 音频生成方案高质量稳定_2109375224738308098.json、音频生成/音频生成/YuE2音乐翻唱ComfyUI官方版音频生成处理工作流_2101391122361839617.json、音频生成/音频生成/YuE2音乐翻唱堪比闭源模型的开源工作流，音频生成音乐翻唱工具_2107551333124497410.json、音频生成/音频生成/YuE2音乐翻唱音频生成方案高质量稳定 音频生成方案_2109757822031450113.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioEncoderLoader`
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
- `PreviewAny`
- `SaveAudioAdvanced`
- `SeedNode`
- `SheetSage2AudioToABC`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 7/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `Audio Duration (mtb)` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `RepeatImageBatch` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有

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
