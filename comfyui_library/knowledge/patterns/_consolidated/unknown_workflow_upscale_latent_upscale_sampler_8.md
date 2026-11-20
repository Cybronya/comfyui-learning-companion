---
name: unknown_workflow_upscale_latent_upscale_sampler_8
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.821364
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json, 视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json, 视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json, 视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json, 视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json, 视频生成/图生视频/LTX2.5图生视频（速度快、像素高）_2087522388522127361.json, 视频生成/图生视频/LTX2.5超精简图生视频480P只要2分钟【推荐新手试用】_2087528931011424257.json, 视频生成/图生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2089012468189323266.json, 视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json, 视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json, 视频生成/文生视频/LTX2.5音画精准匹配+图生视频+尾帧提取+无限时长_2092080500621004801.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json、视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json、视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json、视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json、视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 10/11 个有
- `ResizeImageMaskNode` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `CreateVideo` —— 8/11 个有
- `SaveVideo` —— 8/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `ComfySwitchNode` —— 6/11 个有
- `TextGenerateLTX2Prompt` —— 6/11 个有
- `CR Text` —— 4/11 个有
- `RH_LLMAPI_Pro_Node` —— 4/11 个有
- `llama_cpp_instruct_adv` —— 4/11 个有
- `llama_cpp_model_loader` —— 4/11 个有
- `llama_cpp_parameters` —— 4/11 个有
- `CLIPVisionEncode` —— 2/11 个有
- `CLIPVisionLoader` —— 2/11 个有
- `DisTorchPurgeVRAMV2` —— 2/11 个有
- `Fast Groups Muter (rgthree)` —— 2/11 个有
- `GetVideoComponents` —— 2/11 个有
- `ImageFromBatch+` —— 2/11 个有
- `ImageSizeAndBatchSize` —— 2/11 个有
- `LoadVideo` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `RIFE VFI` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
