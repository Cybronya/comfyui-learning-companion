---
name: unknown_workflow_video_upscale_latent_upscale_85
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7804
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json, 视频生成/文生视频/LTX2.3文生视频（自动提示词）工作流_2031313603197935618.json, 视频生成/文生视频/LTX2.3音图生视频工作流_2031546661310308354.json, 视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json, 视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_85

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/LTX2.3图生视频（自动提示词）工作流_2030929565035536385.json、视频生成/文生视频/LTX2.3文生视频（自动提示词）工作流_2031313603197935618.json、视频生成/文生视频/LTX2.3音图生视频工作流_2031546661310308354.json、视频生成/文生视频/LTX2.5-AIO视频工作流_2087430308756017153.json、视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `LTXVAudioVAEEncode` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `RIFEInterpolation` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `TrimAudioDuration` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `Int` —— 2/5 个有
- `LTXVImgToVideoInplace` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `PrimitiveString` —— 2/5 个有
- `ResizeImageMaskNode` —— 2/5 个有
- `ResizeImagesByLongerEdge` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Switch any [Crystools]` —— 2/5 个有
- `TextGenerateLTX2Prompt` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `ComfyUILTX25MSRICLoRALoader` —— 1/5 个有
- `ComfyUILTX25MSRMultiReferenceGuide` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `LTXVImgToVideoInplaceKJ` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `Resize` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
