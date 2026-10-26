---
name: text_to_image_lora_sampler_clip_19
type: Text To Image
frequency: 27
level: strong
coverage: 0.675333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/9图3音频3视频全能参考2倍速量化加速｜MiniMax-H3数字人口播带货AI漫剧图生视频_2087231453745737730.json, 视频生成/图生视频/Dasiwa V1 SLA加速｜MiniMax H3角色一致图生视频_2092080079957483522.json, 视频生成/图生视频/H3开源全能参考生视频MiniMax视频生视频图生视频_2086445639256330242.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json, 视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2114534802757083137.json, 视频生成/图生视频/MiniMax H3智能反推提示词免手写｜角色一致性人物替换图生视频_2089722342904778753.json, 视频生成/图生视频/Minimax H3人物替换角色一致性图生视频 智能反推提示词免手写方案_2093214087969853442.json, 视频生成/图生视频/Minimax H3人物替换｜智能反推提示词动作迁移_2095295954445496321.json, 视频生成/图生视频/Minimax H3智能反推提示词｜人物替换动作迁移角色一致_2089448022911569922.json, 视频生成/图生视频/Minimax H3角色一致动作迁移图生视频 人物替换智能反推提示词方案_2090070222895144961.json, 视频生成/图生视频/Minimax H3角色一致动作迁移图生视频 人物替换智能反推提示词方案_2090822999573356546.json, 视频生成/图生视频/人物替换免手写提示词｜MiniMax H3角色一致性图生视频_2093478631329849345.json, 视频生成/图生视频/人物替换智能反推｜Minimax H3 角色一致动作迁移图生视频_2089265425245892609.json, 视频生成/图生视频/人物替换角色一致性｜Minimax H3智能反推免手写图生视频_2091251915622539266.json, 视频生成/图生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2095075157848182785.json, 视频生成/图生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2097468927143141377.json, 视频生成/图生视频/智能反推免手写｜Minimax H3人物替换角色一致性图生视频_2093989857021485058.json, 视频生成/图生视频/智能反推提示词 Minimax H3人物替换更省心_2097826550262620161.json, 视频生成/图生视频/智能反推提示词 Minimax H3人物替换更省心_2099639194716033025.json, 视频生成/图生视频/智能反推提示词_Minimax_H3人物替换更省心_2109101235495325697.json, 视频生成/图生视频/智能反推提示词人物替换｜MiniMax H3图生视频_2093459389402411009.json, 视频生成/图生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2094019678422265857.json, 视频生成/图生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2097098707203346434.json, 视频生成/图生视频/极速sigma强化二采｜H3九图三音频全能参考小脸不崩_2091020677938765825.json, 视频生成/图生视频/音频驱动多图多分镜数字人MV MinimaxH3 lightx2v量化加速单人版_2094230825721229314.json, 视频生成/图生视频/音频驱动数字人MV｜MinimaxH3多图分镜lightx2v量化加速_2094352514467586049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/9图3音频3视频全能参考2倍速量化加速｜MiniMax-H3数字人口播带货AI漫剧图生视频_2087231453745737730.json、视频生成/图生视频/Dasiwa V1 SLA加速｜MiniMax H3角色一致图生视频_2092080079957483522.json、视频生成/图生视频/H3开源全能参考生视频MiniMax视频生视频图生视频_2086445639256330242.json、视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2095811312990375938.json、视频生成/图生视频/MiniMax H3动作迁移图生视频 自定义背景人物全能参考_2100008105735184386.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 27 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 26/27 个有
- `PrimitiveFloat` —— 26/27 个有
- `ResolutionSelector` —— 26/27 个有
- `CreateVideo` —— 25/27 个有
- `SaveVideo` —— 25/27 个有
- `VAEDecodeAudio` —— 25/27 个有
- `孤海注释` —— 25/27 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 24/27 个有
- `VHS_LoadVideo` —— 23/27 个有
- `RHHiddenNodes` —— 21/27 个有
- `PrimitiveInt` —— 20/27 个有
- `EasyCache` —— 19/27 个有
- `easy showAnything` —— 18/27 个有
- `LoadAudio` —— 7/27 个有
- `LoadVideo` —— 5/27 个有
- `CR Prompt Text` —— 4/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/27 个有
- `ModelAttentionBackend` —— 4/27 个有
- `PreviewAudio` —— 4/27 个有
- `PreviewImage` —— 4/27 个有
- `SolAttnMiniMax` —— 4/27 个有
- `easy seed` —— 4/27 个有
- `Any Switch (rgthree)` —— 3/27 个有
- `ImageResizeKJv2` —— 3/27 个有
- `LayerUtility: PurgeVRAM` —— 3/27 个有
- `MiniMaxH3SigmaShift` —— 3/27 个有
- `ModelPreviewOverrideKJ` —— 3/27 个有
- `PreviewAny` —— 3/27 个有
- `ZNGB_ImageBatchMulti` —— 3/27 个有
- `easy int` —— 3/27 个有
- `llama_cpp_instruct_adv` —— 3/27 个有
- `llama_cpp_model_loader` —— 3/27 个有
- `llama_cpp_parameters` —— 3/27 个有
- `llama_cpp_unload_model` —— 3/27 个有
- `Any To String (mtb)` —— 2/27 个有
- `AudioCrop` —— 2/27 个有
- `MathExpression|pysssss` —— 2/27 个有
- `SoundFlow_GetLength` —— 2/27 个有
- `TrimAudioDuration` —— 2/27 个有
- `VHS_VideoCombine` —— 2/27 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/27 个有
- `easy clearCacheAll` —— 2/27 个有
- `easy float` —— 2/27 个有
- `EmptyImage` —— 1/27 个有
- `H3SigmaRefiner` —— 1/27 个有
- `LTXVConcatAVLatent` —— 1/27 个有
- `LTXVSeparateAVLatent` —— 1/27 个有
- `LayerUtility: PurgeVRAM V2` —— 1/27 个有
- `LoraLoaderBypassModelOnly` —— 1/27 个有
- `SplitSigmas` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 高发问题（30/27 个样本）：Steps较低可能导致细节不足
