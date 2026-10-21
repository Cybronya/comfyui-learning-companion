---
name: unknown_workflow_lora_sampler_clip_23
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8142
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/首尾帧ltx2_3_style_transition+全节点注释_2057807645574254594.json, 视频生成/图生视频/2066087069847482370.json, 视频生成/图生视频/2042083663428460545.json, 视频生成/图生视频/2041514210315735041.json, 视频生成/图生视频/2041734587340038146.json, 视频生成/图生视频/2082120324979716097.json, 视频生成/图生视频/2038207302813097986.json, 视频生成/图生视频/2030540846281527298.json, 视频生成/图生视频/2030820457208877058.json, 视频生成/图生视频/2042446425367257089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/首尾帧ltx2_3_style_transition+全节点注释_2057807645574254594.json、视频生成/图生视频/2066087069847482370.json、视频生成/图生视频/2042083663428460545.json、视频生成/图生视频/2041514210315735041.json、视频生成/图生视频/2041734587340038146.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ResizeImageMaskNode` —— 9/10 个有
- `KSamplerSelect` —— 8/10 个有
- `LTXVImgToVideoInplace` —— 8/10 个有
- `LTXVLatentUpsampler` —— 8/10 个有
- `LatentUpscaleModelLoader` —— 8/10 个有
- `PrimitiveBoolean` —— 8/10 个有
- `ResizeImagesByLongerEdge` —— 8/10 个有
- `Int` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `LayerUtility: PurgeVRAM V2` —— 5/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `YC_textReplaceNode` —— 3/10 个有
- `llama_cpp_instruct_adv` —— 3/10 个有
- `llama_cpp_model_loader` —— 3/10 个有
- `llama_cpp_parameters` —— 3/10 个有
- `Evaluate Integers` —— 2/10 个有
- `Float` —— 2/10 个有
- `GetImageSize` —— 2/10 个有
- `LTXVAddGuide` —— 2/10 个有
- `LayerUtility: TextBox` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `SDVN Any Show` —— 2/10 个有
- `SamplerEulerAncestral` —— 2/10 个有
- `ImageResizeKJ` —— 1/10 个有
- `LTXVAddGuideMulti` —— 1/10 个有
- `QZ_ResolutionPreset` —— 1/10 个有
- `YC_ShowText` —— 1/10 个有
- `YC_SingleTextNode` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
