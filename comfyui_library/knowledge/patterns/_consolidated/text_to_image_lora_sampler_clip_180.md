---
name: text_to_image_lora_sampler_clip_180
type: Text To Image
frequency: 10
level: strong
coverage: 0.7909
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, EmptyYuE2LatentAudio, JjkText, KSampler, LoraLoaderModelOnly, PreviewAny, PrimitiveStringMultiline, SaveAudioAdvanced, SeedNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, YuE2GenerateMusic, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2114263696510898178.json, 音频生成/音频生成/YuE2官方文生音乐工作流｜AI作曲生成原创音乐_2106992486311874561.json, 音频生成/音频生成/YuE2文本转音乐｜一句话描述生成完整曲子，配乐创作零门槛_2107313406511501314.json, 音频生成/音频生成/YuE2文生音乐ComfyUI官方版音频生成处理工作流_2101389597929459714.json, 音频生成/音频生成/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2110539658919759874.json, 音频生成/音频生成/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2110890424977158146.json, 音频生成/音频生成/YuE2音乐翻唱ComfyUI官方版音频生成处理工作流_2101391122361839617.json, 音频生成/音频生成/Yue2音乐翻唱官方工作流，音频生成音乐翻唱处理工具_2107246415910105090.json, 音频生成/音频生成/audio_yue2_music_cover音频生成｜AI翻唱一键搞定_2106987749390770177.json, 音频生成/音频生成/文本转音乐YuE2工作流，音频生成文本到音乐创作工具_2107596310319816705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_180

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2114263696510898178.json、音频生成/音频生成/YuE2官方文生音乐工作流｜AI作曲生成原创音乐_2106992486311874561.json、音频生成/音频生成/YuE2文本转音乐｜一句话描述生成完整曲子，配乐创作零门槛_2107313406511501314.json、音频生成/音频生成/YuE2文生音乐ComfyUI官方版音频生成处理工作流_2101389597929459714.json、音频生成/音频生成/YuE2文生音乐ComfyUI官方版，音频生成好听又好用_2110539658919759874.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptyYuE2LatentAudio`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveAudioAdvanced`
- `SeedNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `YuE2GenerateMusic`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `孤海注释` —— 8/10 个有
- `PrimitiveString` —— 7/10 个有
- `YuE2GenerateABC` —— 7/10 个有
- `PrimitiveFloat` —— 5/10 个有
- `AudioEncoderLoader` —— 3/10 个有
- `LoadAudio` —— 3/10 个有
- `LoadImage` —— 3/10 个有
- `PrimitiveInt` —— 3/10 个有
- `SheetSage2AudioToABC` —— 3/10 个有
- `Audio Duration (mtb)` —— 2/10 个有
- `EmptyImage` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `RepeatImageBatch` —— 2/10 个有
- `SaveImage` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
