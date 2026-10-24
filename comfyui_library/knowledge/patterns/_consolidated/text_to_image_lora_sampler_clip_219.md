---
name: text_to_image_lora_sampler_clip_219
type: Text To Image
frequency: 9
level: strong
coverage: 0.799333
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoraLoaderModelOnly, PreviewAny, SaveAudioAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [音频生成/音频生成/AI音乐自动原创歌曲工作流，音频生成音乐创作处理工具_2108288533705347074.json, 音频生成/音频生成/YuE2官方文生音乐工作流｜AI作曲生成原创音乐_2106992486311874561.json, 音频生成/音频生成/YuE2文本转音乐｜一句话描述生成完整曲子，配乐创作零门槛_2107313406511501314.json, 音频生成/音频生成/YuE2文生音乐ComfyUI官方版音频生成处理工作流_2101389597929459714.json, 音频生成/音频生成/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2110539658919759874.json, 音频生成/音频生成/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2110890424977158146.json, 音频生成/音频生成/YuE2音乐翻唱ComfyUI官方版音频生成处理工作流_2101391122361839617.json, 音频生成/音频生成/Yue2音乐翻唱官方工作流，音频生成音乐翻唱处理工具_2107246415910105090.json, 音频生成/音频生成/audio_yue2_music_cover音频生成｜AI翻唱一键搞定_2106987749390770177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_219

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（音频生成/音频生成/AI音乐自动原创歌曲工作流，音频生成音乐创作处理工具_2108288533705347074.json、音频生成/音频生成/YuE2官方文生音乐工作流｜AI作曲生成原创音乐_2106992486311874561.json、音频生成/音频生成/YuE2文本转音乐｜一句话描述生成完整曲子，配乐创作零门槛_2107313406511501314.json、音频生成/音频生成/YuE2文生音乐ComfyUI官方版音频生成处理工作流_2101389597929459714.json、音频生成/音频生成/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2110539658919759874.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `EmptyYuE2LatentAudio`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `SeedNode` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `YuE2GenerateABC` —— 6/9 个有
- `PrimitiveString` —— 5/9 个有
- `PrimitiveFloat` —— 4/9 个有
- `AudioEncoderLoader` —— 3/9 个有
- `LoadAudio` —— 3/9 个有
- `PrimitiveInt` —— 3/9 个有
- `SheetSage2AudioToABC` —— 3/9 个有
- `Audio Duration (mtb)` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `RepeatImageBatch` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `VHS_VideoCombine` —— 2/9 个有
- `Any Switch (rgthree)` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `EmptyImage` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

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
