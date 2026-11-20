---
name: text_to_image_lora_sampler_clip_120
type: Text To Image
frequency: 13
level: strong
coverage: 0.652538
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/9图3音频3视频全能参考2倍速量化加速｜MiniMax-H3数字人口播带货AI漫剧图生视频_2087231453745737730.json, 视频生成/图生视频/Dasiwa V1 SLA加速｜MiniMax H3角色一致图生视频_2092080079957483522.json, 视频生成/图生视频/H3开源全能参考生视频MiniMax视频生视频图生视频_2086445639256330242.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2114534802757083137.json, 视频生成/图生视频/MiniMax_H3动作迁移图生视频_自定义背景人物全能参考_2101088561767473154.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2089305534913667073.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2090649252212076545.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3自定义背景人物迁移_2090938897554567170.json, 视频生成/图生视频/极速sigma强化二采｜H3九图三音频全能参考小脸不崩_2091020677938765825.json, 视频生成/图生视频/音频驱动多图多分镜数字人MV MinimaxH3 lightx2v量化加速单人版_2094230825721229314.json, 视频生成/图生视频/音频驱动数字人MV｜MinimaxH3多图分镜lightx2v量化加速_2094352514467586049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_120

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/9图3音频3视频全能参考2倍速量化加速｜MiniMax-H3数字人口播带货AI漫剧图生视频_2087231453745737730.json、视频生成/图生视频/Dasiwa V1 SLA加速｜MiniMax H3角色一致图生视频_2092080079957483522.json、视频生成/图生视频/H3开源全能参考生视频MiniMax视频生视频图生视频_2086445639256330242.json、视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json、视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 12/13 个有
- `PrimitiveFloat` —— 12/13 个有
- `ResolutionSelector` —— 12/13 个有
- `CreateVideo` —— 11/13 个有
- `LoadAudio` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `VAEDecodeAudio` —— 11/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/13 个有
- `孤海注释` —— 10/13 个有
- `VHS_LoadVideo` —— 9/13 个有
- `CR Prompt Text` —— 8/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/13 个有
- `ModelAttentionBackend` —— 4/13 个有
- `PreviewAudio` —— 4/13 个有
- `PreviewImage` —— 4/13 个有
- `SolAttnMiniMax` —— 4/13 个有
- `easy seed` —— 4/13 个有
- `Any Switch (rgthree)` —— 3/13 个有
- `ImageResizeKJv2` —— 3/13 个有
- `LayerUtility: PurgeVRAM` —— 3/13 个有
- `MiniMaxH3SigmaShift` —— 3/13 个有
- `ModelPreviewOverrideKJ` —— 3/13 个有
- `PreviewAny` —— 3/13 个有
- `RHHiddenNodes` —— 3/13 个有
- `ZNGB_ImageBatchMulti` —— 3/13 个有
- `easy int` —— 3/13 个有
- `llama_cpp_instruct_adv` —— 3/13 个有
- `llama_cpp_model_loader` —— 3/13 个有
- `llama_cpp_parameters` —— 3/13 个有
- `llama_cpp_unload_model` —— 3/13 个有
- `Any To String (mtb)` —— 2/13 个有
- `AudioCrop` —— 2/13 个有
- `MathExpression|pysssss` —— 2/13 个有
- `PrimitiveInt` —— 2/13 个有
- `SoundFlow_GetLength` —— 2/13 个有
- `TrimAudioDuration` —— 2/13 个有
- `VHS_VideoCombine` —— 2/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/13 个有
- `easy clearCacheAll` —— 2/13 个有
- `easy float` —— 2/13 个有
- `EasyCache` —— 1/13 个有
- `EmptyImage` —— 1/13 个有
- `H3SigmaRefiner` —— 1/13 个有
- `LTXVConcatAVLatent` —— 1/13 个有
- `LTXVSeparateAVLatent` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `LoraLoaderBypassModelOnly` —— 1/13 个有
- `SplitSigmas` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
