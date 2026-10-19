---
name: text_to_image_lora_sampler_clip_52
type: Text To Image
frequency: 14
level: strong
coverage: 0.669214
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/9图3音频3视频全能参考2倍速量化加速｜MiniMax-H3数字人口播带货AI漫剧图生视频_2087231453745737730.json, 视频生成/图生视频/Dasiwa V1 SLA加速｜MiniMax H3角色一致图生视频_2092080079957483522.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json, 视频生成/图生视频/MiniMax H3智能反推提示词免手写｜角色一致性人物替换图生视频_2089722342904778753.json, 视频生成/图生视频/Minimax H3人物替换角色一致性图生视频 智能反推提示词免手写方案_2093214087969853442.json, 视频生成/图生视频/Minimax H3人物替换｜智能反推提示词动作迁移_2095295954445496321.json, 视频生成/图生视频/Minimax H3智能反推提示词｜人物替换动作迁移角色一致_2089448022911569922.json, 视频生成/图生视频/Minimax H3角色一致动作迁移图生视频 人物替换智能反推提示词方案_2090070222895144961.json, 视频生成/图生视频/Minimax H3角色一致动作迁移图生视频 人物替换智能反推提示词方案_2090822999573356546.json, 视频生成/图生视频/人物替换免手写提示词｜MiniMax H3角色一致性图生视频_2093478631329849345.json, 视频生成/图生视频/极速sigma强化二采｜H3九图三音频全能参考小脸不崩_2091020677938765825.json, 视频生成/图生视频/音频驱动多图多分镜数字人MV MinimaxH3 lightx2v量化加速单人版_2094230825721229314.json, 视频生成/图生视频/音频驱动数字人MV｜MinimaxH3多图分镜lightx2v量化加速_2094352514467586049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/9图3音频3视频全能参考2倍速量化加速｜MiniMax-H3数字人口播带货AI漫剧图生视频_2087231453745737730.json、视频生成/图生视频/Dasiwa V1 SLA加速｜MiniMax H3角色一致图生视频_2092080079957483522.json、视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json、视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json、视频生成/图生视频/MiniMax H3智能反推提示词免手写｜角色一致性人物替换图生视频_2089722342904778753.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 14 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 13/14 个有
- `PrimitiveFloat` —— 13/14 个有
- `ResolutionSelector` —— 13/14 个有
- `CreateVideo` —— 12/14 个有
- `SaveVideo` —— 12/14 个有
- `VAEDecodeAudio` —— 12/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/14 个有
- `VHS_LoadVideo` —— 11/14 个有
- `RHHiddenNodes` —— 10/14 个有
- `PrimitiveInt` —— 9/14 个有
- `EasyCache` —— 7/14 个有
- `easy showAnything` —— 7/14 个有
- `LoadAudio` —— 6/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/14 个有
- `ModelAttentionBackend` —— 4/14 个有
- `PreviewAudio` —— 4/14 个有
- `SolAttnMiniMax` —— 4/14 个有
- `easy seed` —— 4/14 个有
- `Any Switch (rgthree)` —— 3/14 个有
- `ImageResizeKJv2` —— 3/14 个有
- `LayerUtility: PurgeVRAM` —— 3/14 个有
- `MiniMaxH3SigmaShift` —— 3/14 个有
- `ModelPreviewOverrideKJ` —— 3/14 个有
- `PreviewAny` —— 3/14 个有
- `PreviewImage` —— 3/14 个有
- `ZNGB_ImageBatchMulti` —— 3/14 个有
- `easy int` —— 3/14 个有
- `llama_cpp_instruct_adv` —— 3/14 个有
- `llama_cpp_model_loader` —— 3/14 个有
- `llama_cpp_parameters` —— 3/14 个有
- `llama_cpp_unload_model` —— 3/14 个有
- `Any To String (mtb)` —— 2/14 个有
- `AudioCrop` —— 2/14 个有
- `CR Prompt Text` —— 2/14 个有
- `MathExpression|pysssss` —— 2/14 个有
- `SoundFlow_GetLength` —— 2/14 个有
- `TrimAudioDuration` —— 2/14 个有
- `VHS_VideoCombine` —— 2/14 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/14 个有
- `easy clearCacheAll` —— 2/14 个有
- `easy float` —— 2/14 个有
- `H3SigmaRefiner` —— 1/14 个有
- `LTXVConcatAVLatent` —— 1/14 个有
- `LTXVSeparateAVLatent` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `LoadVideo` —— 1/14 个有
- `LoraLoaderBypassModelOnly` —— 1/14 个有
- `SplitSigmas` —— 1/14 个有

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
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
