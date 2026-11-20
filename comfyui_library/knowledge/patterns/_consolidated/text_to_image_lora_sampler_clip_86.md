---
name: text_to_image_lora_sampler_clip_86
type: Text To Image
frequency: 15
level: strong
coverage: 0.872267
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json, 视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json, 视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2089308419999223810.json, 视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2090728184093437953.json, 视频生成/图生视频/8步加速首帧参考｜MiniMax H3写实图生视频战斗特效_2089381704552247298.json, 视频生成/图生视频/9图3视频3音频多参考｜Minimax H3开源版音视频生成_2089469135704117249.json, 视频生成/图生视频/9图3视频3音频｜海螺H3全能多参开源版音视频生成_2090229409646202881.json, 视频生成/图生视频/H3 FACE REFINE面部重绘修复崩脸｜图生视频画质修复_2090410678174707713.json, 视频生成/图生视频/H3单图生视频_2102656768471031809.json, 视频生成/图生视频/MiniMax H3多参图像音频生视频｜Singulari极速加速版_2107645905364152321.json, 视频生成/图生视频/加速版 MiniMax H3｜多参图像音频极速生视频_2096900307132444673.json, 视频生成/图生视频/加速版MiniMax H3多参图像音频极速生视频Singulari工作流，图生视频方案_2107951250322059266.json, 视频生成/图生视频/加速版MiniMax_H3多参生视频｜图像音频一起喂，出片速度起飞_2099442755004096513.json, 视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json, 视频生成/文生视频/多参图像音频极速生视频｜加速版MiniMax H3生成_2096328491850625026.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_86

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/8step加速开源版｜MinimaxH3参考生视频图生视频_2093224901363720194.json、视频生成/图生视频/8步加速1.0正式版｜minimax 1.0视频生视频图生视频工作流_2088345029642379265.json、视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2089308419999223810.json、视频生成/图生视频/8步加速全能参考｜minimax 视频生成_2090728184093437953.json、视频生成/图生视频/8步加速首帧参考｜MiniMax H3写实图生视频战斗特效_2089381704552247298.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `孤海注释` —— 13/15 个有
- `LoadAudio` —— 11/15 个有
- `CreateVideo` —— 10/15 个有
- `PathchSageAttentionKJ` —— 10/15 个有
- `SaveVideo` —— 10/15 个有
- `CR Prompt Text` —— 7/15 个有
- `GetVideoComponents` —— 7/15 个有
- `LoadVideo` —— 7/15 个有
- `PrimitiveStringMultiline` —— 7/15 个有
- `EasyCache` —— 6/15 个有
- `ImpactSwitch` —— 6/15 个有
- `ShowAnything|Mie` —— 6/15 个有
- `VHS_VideoCombine` —— 6/15 个有
- `PainterVRAM` —— 3/15 个有
- `VHS_LoadVideo` —— 3/15 个有
- `easy showAnything` —— 3/15 个有
- `DF_Int_to_Float` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/15 个有
- `EmptyImage` —— 1/15 个有
- `H3FaceStitch` —— 1/15 个有
- `H3FaceTrackCrop` —— 1/15 个有
- `H3InjectVideoLatent` —— 1/15 个有
- `H3PerFrameDenoise` —— 1/15 个有
- `MiniMaxH3ImageToVideo` —— 1/15 个有
- `MiniMaxH3NativeAudioLock` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `SolAttnPatch` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
