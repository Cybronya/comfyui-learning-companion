---
name: text_to_image_video_lora_sampler_49
type: Text To Image
frequency: 13
level: strong
coverage: 0.683308
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, JjkText, JoinStringMulti, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, PurgeVRAM_UTK, RandomNoise, SamplerCustomAdvanced, SetNode, StringConcatenate, ToString, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3参考生视频720P高清图生视频处理工具_2101024037894975490.json, 视频生成/图生视频/V1.2两次采样8步加速MiniMax H3参考生视频音频参考自动提示词优化_2088370421749080065.json, 视频生成/图生视频/lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425.json, 视频生成/图生视频/两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810.json, 视频生成/图生视频/两次采样8步加速音频参考自动提示词优化V1.2｜MiniMax H3参考生视频图生视频_2088337657226153985.json, 视频生成/图生视频/参考生视频完美版1080P｜MiniMax H3多图多音频自动提示词V1.2_2091668802529480706.json, 视频生成/图生视频/绘影MiniMax H3参考生视频1080P高清版V2 高质量视频输出_2105055271889494017.json, 视频生成/图生视频/绘影MiniMax H3参考生视频720P图生视频处理工具_2102106591196700674.json, 视频生成/图生视频/绘影MiniMax H3参考生视频in 混合模型，720P加速LoRA四步出图方案_2103224330846031873.json, 视频生成/图生视频/绘影MiniMax H3参考生视频ref2va in 720P V2 视频生成方案_2105061454188732418.json, 视频生成/图生视频/绘影出品｜MiniMax H3参考生视频720P V1｜图生视频一键出片_2101843591164424193.json, 视频生成/图生视频/绘影打造｜MiniMax H3参考生视频fl2va int8量化720P V1_2103021430949629954.json, 视频生成/文生视频/MiniMax H3 Ref2VA多参考素材生视频1080P高清版处理工具_2101718572941795330.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_49

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3参考生视频720P高清图生视频处理工具_2101024037894975490.json、视频生成/图生视频/V1.2两次采样8步加速MiniMax H3参考生视频音频参考自动提示词优化_2088370421749080065.json、视频生成/图生视频/lightx2v 4步加速｜MiniMax H3参考生视频自动提示词优化V1.3_2089847613943271425.json、视频生成/图生视频/两次采样1080P｜MiniMax H3参考生视频音频参考提示词优化V1.3_2089794956117495810.json、视频生成/图生视频/两次采样8步加速音频参考自动提示词优化V1.2｜MiniMax H3参考生视频图生视频_2088337657226153985.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 13 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `JjkText`
- `JoinStringMulti`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringConcatenate`
- `ToString`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 11/13 个有
- `MiniMaxH3SigmaShift` —— 11/13 个有
- `ZNGB_ImageBatchMulti` —— 11/13 个有
- `Int` —— 9/13 个有
- `ratio_selector` —— 9/13 个有
- `MiniMaxChunkFeedForward` —— 7/13 个有
- `MiniMaxLowVRAMAttention` —— 7/13 个有
- `LTXVConcatAVLatent` —— 6/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/13 个有
- `SaveImage` —— 6/13 个有
- `PDRatioSelector` —— 5/13 个有
- `ComfyNumberConvert` —— 4/13 个有
- `ComfySwitchNode` —— 4/13 个有
- `Compare` —— 4/13 个有
- `ConvertAny2Int` —— 4/13 个有
- `LTXVSeparateAVLatent` —— 4/13 个有
- `ResolutionSelector` —— 4/13 个有
- `SplitSigmas` —— 4/13 个有
- `SplitStringByDelimiter` —— 4/13 个有
- `easy ifElse` —— 4/13 个有
- `MinimaxH3LatentUpscaler3D` —— 3/13 个有
- `ModelPreviewOverrideKJ` —— 3/13 个有
- `SolAttnMiniMax` —— 3/13 个有
- `BatchImagesNode` —— 2/13 个有
- `ImageResizeKJv2` —— 2/13 个有
- `MiniMaxH3AVDecodeT8` —— 2/13 个有
- `VAEEncode` —— 2/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `CreateVideo` —— 1/13 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/13 个有
- `SaveVideo` —— 1/13 个有
- `SetReserveVRAM` —— 1/13 个有
- `TrimAudioDuration` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
