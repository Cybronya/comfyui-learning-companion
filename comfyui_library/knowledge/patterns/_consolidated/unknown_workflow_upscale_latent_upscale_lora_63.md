---
name: unknown_workflow_upscale_latent_upscale_lora_63
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.897
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/一张图片，简单台词，就能出片了_2039634307186171905.json, 视频生成/文生视频/LTX 2.3 ComfyUI：三阶段 4K 工作流程（修复视频失真）_2038095391647862786.json, 视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json, 视频生成/文生视频/LTX-2.3+Qwen3.5生成武打电影视频_2030549062293921794.json, 视频生成/文生视频/LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_63

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/一张图片，简单台词，就能出片了_2039634307186171905.json、视频生成/文生视频/LTX 2.3 ComfyUI：三阶段 4K 工作流程（修复视频失真）_2038095391647862786.json、视频生成/文生视频/LTX-2.3+Qwen3.5生成宠物播客视频_2030535698637398018.json、视频生成/文生视频/LTX-2.3+Qwen3.5生成武打电影视频_2030549062293921794.json、视频生成/文生视频/LTX-2.3配音术：实现播客录音变视频🔥_2032093186700615681.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `ResizeImageMaskNode` —— 4/5 个有
- `llama_cpp_instruct_adv` —— 4/5 个有
- `llama_cpp_model_loader` —— 4/5 个有
- `llama_cpp_parameters` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `LTXVCropGuides` —— 3/5 个有
- `LTXVImgToVideoInplace` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `ResizeImagesByLongerEdge` —— 3/5 个有
- `CM_FloatToInt` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `LTXVImgToVideoConditionOnly` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `AudioInfoNode` —— 1/5 个有
- `Bjornulf_ShowInt` —— 1/5 个有
- `FB_Qwen3TTSDialogueInference` —— 1/5 个有
- `FB_Qwen3TTSRoleBank` —— 1/5 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 1/5 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/5 个有
- `GuiderParameters` —— 1/5 个有
- `LTXVAudioVAEEncode` —— 1/5 个有
- `LTXVChunkFeedForward` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `MultimodalGuider` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `SolidMask` —— 1/5 个有
- `TextConcatenator` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `数学运算_孤海` —— 1/5 个有

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
