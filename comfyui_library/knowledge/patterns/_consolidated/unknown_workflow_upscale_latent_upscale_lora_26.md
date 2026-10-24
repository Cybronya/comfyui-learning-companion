---
name: unknown_workflow_upscale_latent_upscale_lora_26
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.847182
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 电商专用图文生视频-提示词响应优化_2061384649385009154.json, 视频生成/图生视频/LTX2.3 真人高清一键长视频工作流 V2.3_2038518064030945282.json, 视频生成/图生视频/LTX2.3-图生视频，智能提示词优化_2031273311556079618.json, 视频生成/图生视频/LTX2.3-首中尾帧视频+Qwen3.5自动提示词_2037900927323082754.json, 视频生成/图生视频/LTX2.3-首尾多帧视频生成_2031368415541202945.json, 视频生成/图生视频/LTX2.3真人短剧_2033403811573800961.json, 视频生成/图生视频/LTX2.3自动首尾帧流_2073405314405322753.json, 视频生成/图生视频/fast图生视频_2053653678917206018.json, 视频生成/图生视频/full图生视频_2053653864032813058.json, 视频生成/图生视频/【LTX2.3官方工作流优化】首尾帧控制 _含提示词扩写模板_2033785787984125953.json, 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_26

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 电商专用图文生视频-提示词响应优化_2061384649385009154.json、视频生成/图生视频/LTX2.3 真人高清一键长视频工作流 V2.3_2038518064030945282.json、视频生成/图生视频/LTX2.3-图生视频，智能提示词优化_2031273311556079618.json、视频生成/图生视频/LTX2.3-首中尾帧视频+Qwen3.5自动提示词_2037900927323082754.json、视频生成/图生视频/LTX2.3-首尾多帧视频生成_2031368415541202945.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 10/11 个有
- `RH_LLMAPI_Pro_Node` —— 9/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `ResizeImageMaskNode` —— 8/11 个有
- `PrimitiveBoolean` —— 7/11 个有
- `easy showAnything` —— 7/11 个有
- `LTXVImgToVideoInplaceKJ` —— 4/11 个有
- `SimpleMath+` —— 4/11 个有
- `Text` —— 4/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `PlaySound|pysssss` —— 2/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `BDXTestInt` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `JoinStrings` —— 1/11 个有
- `MultiplicationNode` —— 1/11 个有
- `Qwen3_VQA` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有

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
