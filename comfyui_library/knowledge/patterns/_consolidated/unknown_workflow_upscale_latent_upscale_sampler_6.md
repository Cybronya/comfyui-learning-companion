---
name: unknown_workflow_upscale_latent_upscale_sampler_6
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.837091
common_nodes: [CLIPLoader, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json, 视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json, 视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json, 视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json, 视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json, 视频生成/图生视频/LTX2.5图生视频一致性加强版V1_2087536517580414978.json, 视频生成/图生视频/LTX2.5图生视频一致性强化版+提示词优化_2087504758146949121.json, 视频生成/图生视频/LTX2.5图生视频一致性强化版V1_2087405102549262338.json, 视频生成/图生视频/LTX2.5图生视频（标准版工作流）_2087460376823820290.json, 视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json, 视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json、视频生成/图生视频/LTX2.5-图生视频_2087515101900402690.json、视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json、视频生成/图生视频/LTX2.5图生视频 -高质量直出1K_2087559276465319937.json、视频生成/图生视频/LTX2.5图生视频_2087770942218006530.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
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
- `ResizeImageMaskNode` —— 10/11 个有
- `CLIPTextEncode` —— 9/11 个有
- `LTXVEmptyLatentAudio` —— 8/11 个有
- `ResolutionSelector` —— 8/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `CR Text` —— 6/11 个有
- `CreateVideo` —— 6/11 个有
- `RH_LLMAPI_Pro_Node` —— 6/11 个有
- `SaveVideo` —— 6/11 个有
- `PreviewAny` —— 5/11 个有
- `PrimitiveStringMultiline` —— 4/11 个有
- `easy showAnything` —— 4/11 个有
- `LTXVAudioVAEEncode` —— 3/11 个有
- `LoadAudio` —— 3/11 个有
- `SetLatentNoiseMask` —— 3/11 个有
- `SolidMask` —— 3/11 个有
- `TextGenerateLTX2Prompt` —— 3/11 个有
- `TrimAudioDuration` —— 3/11 个有
- `AudioInfo` —— 2/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `PromptRelaySmartEncode` —— 2/11 个有
- `ResizeImagesByLongerEdge` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `ShellAgentPluginOutputText` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有
- `llama_cpp_parameters` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
