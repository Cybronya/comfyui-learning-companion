---
name: unknown_workflow_sampler_unet_vae_30
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.889429
common_nodes: [CFGGuider, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/文生图/LTX2.3 多图控制 提示词分段中继流_2073319635222618113.json, 视频生成/图生视频/2052341800647569410.json, 视频生成/图生视频/2039999501695459329.json, 视频生成/图生视频/2039365637025304577.json, 视频生成/图生视频/2038953510800199682.json, 视频生成/图生视频/2039330537847922689.json, 视频生成/图生视频/2039363002973032450.json, 视频生成/图生视频/2040690570988883969.json, 视频生成/图生视频/2031244973215064065.json, 视频生成/图生视频/2031018191203340289.json, 视频生成/图生视频/2040716663120732161.json, 视频生成/图生视频/2037880867695108098.json, 视频生成/图生视频/2038548270510776322.json, 视频生成/图生视频/2040976928861069314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_30

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/LTX2.3 多图控制 提示词分段中继流_2073319635222618113.json、视频生成/图生视频/2052341800647569410.json、视频生成/图生视频/2039999501695459329.json、视频生成/图生视频/2039365637025304577.json、视频生成/图生视频/2038953510800199682.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 13/14 个有
- `CLIPTextEncode` —— 12/14 个有
- `LTXVLatentUpsampler` —— 12/14 个有
- `LTXVPreprocess` —— 12/14 个有
- `LatentUpscaleModelLoader` —— 12/14 个有
- `ManualSigmas` —— 12/14 个有
- `SimpleMath+` —— 12/14 个有
- `LoraLoaderModelOnly` —— 11/14 个有
- `LTXVAddGuideMulti` —— 10/14 个有
- `ShowText|pysssss` —— 9/14 个有
- `easy cleanGpuUsed` —— 9/14 个有
- `llama_cpp_instruct_adv` —— 9/14 个有
- `llama_cpp_model_loader` —— 9/14 个有
- `Text` —— 7/14 个有
- `AspectRatio` —— 6/14 个有
- `ImageConcanate` —— 5/14 个有
- `BasicScheduler` —— 2/14 个有
- `ConditioningZeroOut` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 2/14 个有
- `PrimitiveFloat` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `PromptRelayEncodeTimeline` —— 2/14 个有
- `easy showAnything` —— 2/14 个有
- `llama_cpp_unload_model` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `Int` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `RH_LLMAPI_Pro_Node` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 601 | 14 | 7% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 601，14 个样本，取值分散，一致性仅 7%
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
