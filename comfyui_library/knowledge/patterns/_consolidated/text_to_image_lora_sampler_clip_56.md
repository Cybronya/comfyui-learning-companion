---
name: text_to_image_lora_sampler_clip_56
type: Text To Image
frequency: 14
level: strong
coverage: 0.899214
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2K加速版文生图｜MiniMaxH3开源美少女写实出图_2089063557869694977.json, 视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json, 视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json, 视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json, 视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json, 视频生成/图生视频/H3 Taomate 3步加速 中远距离不崩脸视频生成_2099588330131382273.json, 视频生成/图生视频/H3多图参考视频生成全注释 多图参考入门级工作流_2099204538879266817.json, 视频生成/图生视频/MiniMax H3参考生视频数字人 图生视频智能体创作_2098639055553646593.json, 视频生成/图生视频/MiniMax H3参考生视频｜数字人动作神态复刻_2098709684097212418.json, 视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json, 视频生成/图生视频/加速版 MiniMax H3｜多参图像音频极速生视频_2096900307132444673.json, 视频生成/图生视频/加速版MiniMax H3多参图像音频极速生视频Singulari工作流，图生视频方案_2107951250322059266.json, 视频生成/图生视频/加速版MiniMax_H3多参生视频｜图像音频一起喂，出片速度起飞_2099442755004096513.json, 视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/2K加速版文生图｜MiniMaxH3开源美少女写实出图_2089063557869694977.json、视频生成/图生视频/6倍加速24GB通用版优化版｜MiniMax H3图生视频数字人工作流_2087156243797471233.json、视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json、视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json、视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 13/14 个有
- `ComfyMathExpression` —— 13/14 个有
- `CreateVideo` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `SaveVideo` —— 13/14 个有
- `VAEDecodeAudio` —— 13/14 个有
- `MiniMaxH3ReferenceToVideo` —— 12/14 个有
- `LoadAudio` —— 11/14 个有
- `EasyCache` —— 8/14 个有
- `PathchSageAttentionKJ` —— 8/14 个有
- `PrimitiveStringMultiline` —— 7/14 个有
- `CR Prompt Text` —— 6/14 个有
- `GetVideoComponents` —— 6/14 个有
- `LoadVideo` —— 6/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/14 个有
- `SaveImage` —— 6/14 个有
- `ImpactSwitch` —— 5/14 个有
- `ShowAnything|Mie` —— 5/14 个有
- `MiniMaxH3SigmaShift` —— 3/14 个有
- `SolAttnPatch` —— 3/14 个有
- `DF_Int_to_Float` —— 2/14 个有
- `MiniMaxH3ImageToVideo` —— 2/14 个有
- `ModelPreviewOverrideKJ` —— 2/14 个有
- `TrimAudioDuration` —— 2/14 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `ImageFromBatch` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `ManualSigmas` —— 1/14 个有
- `MiniMaxChunkFeedForward` —— 1/14 个有
- `MiniMaxLowVRAMAttention` —— 1/14 个有
- `ModelAttentionBackend` —— 1/14 个有
- `PreviewImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
