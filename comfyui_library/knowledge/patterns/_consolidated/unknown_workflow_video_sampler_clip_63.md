---
name: unknown_workflow_video_sampler_clip_63
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.678667
common_nodes: [AudioConcat, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, FL_IntToFloat, FL_RIFE, ImageScale, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVNormalizingSampler, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveFloat, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, RandomNoise, VAEDecodeTiled, VHS_SelectImages, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/005.LTX2.3音视融合005.LTX2.3首尾帧图生视频_2035377516814278657.json, 视频生成/图生视频/LTX2.0 4模型对比_2018295552026349570.json, 视频生成/图生视频/LTX2.3首尾帧工作流_2030224729138798593.json, 视频生成/图生视频/Ltx-2最强图生视频智能提示词无限长度版V1（脸部稳定版）_2018359643973619714.json, 视频生成/图生视频/Ltx2自动提示词图生视频V1（脸部稳定SFW版）_2018362245423570945.json, 视频生成/图生视频/Ltx2自动提示词图生视频V1（脸部稳定SFW版）_2054445027421638658.json, 视频生成/图生视频/（自用）LTXV-2 AIO V41图生视频_2016472662767312898.json, 视频生成/图生视频/（自用）LTXV-2 AIO V41首尾帧_2016460941017227265.json, 视频生成/图生视频/（自用）Ltx-2自动提示词版图生视频V1_2018361169383264257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/005.LTX2.3音视融合005.LTX2.3首尾帧图生视频_2035377516814278657.json、视频生成/图生视频/LTX2.0 4模型对比_2018295552026349570.json、视频生成/图生视频/LTX2.3首尾帧工作流_2030224729138798593.json、视频生成/图生视频/Ltx-2最强图生视频智能提示词无限长度版V1（脸部稳定版）_2018359643973619714.json、视频生成/图生视频/Ltx2自动提示词图生视频V1（脸部稳定SFW版）_2018362245423570945.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioConcat`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `FL_IntToFloat`
- `FL_RIFE`
- `ImageScale`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVNormalizingSampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `VAEDecodeTiled`
- `VHS_SelectImages`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 7/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `DualCLIPLoader` —— 7/9 个有
- `VAELoaderKJ` —— 7/9 个有
- `Float to Int` —— 6/9 个有
- `CR Prompt Text` —— 5/9 个有
- `DuckHideNode` —— 5/9 个有
- `JWInteger` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `RH_LLMAPI_Pro_Node` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `TT_img_enc` —— 5/9 个有
- `TT_img_enc_v2` —— 5/9 个有
- `easy anythingIndexSwitch` —— 5/9 个有
- `UNETLoader` —— 4/9 个有
- `LTXAVTextEncoderLoader` —— 3/9 个有
- `LTXVAudioVAELoader` —— 3/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `RH_Utils` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `BasicGuider` —— 2/9 个有
- `LTX2AttentionTunerPatch` —— 2/9 个有
- `MemoryCleaner` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `Any To Any` —— 1/9 个有
- `Any To String (mtb)` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `KSampler` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有
- `ReplaceText` —— 1/9 个有
- `VHS_SelectFilename` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 93 | 93 - 93 | 9 | 100% |
| 高度 | 20 | 20 - 20 | 9 | 100% |
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | lcm | - | 1 | 100% |
| 调度器 | sgm_uniform | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/9 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 93，观测区间 93 - 93，9 个样本，取值集中（一致性 100%）
- 高度 中位数 20，观测区间 20 - 20，9 个样本，取值集中（一致性 100%）
