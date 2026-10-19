---
name: unknown_workflow_upscale_latent_upscale_lora_31
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.874
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2034546381762863105.json, 视频生成/图生视频/2031381886173450241.json, 视频生成/图生视频/2034612488255315970.json, 视频生成/图生视频/2036083633810837505.json, 视频生成/图生视频/（1图 1音频）LTX2.3 图 + 音频数字人对口型_2111327625162612737.json, 视频生成/图生视频/2031928367213187074.json, 视频生成/文生视频/LTX-2.3-Image Audio to Video Workflow_2033716721021886465.json, 视频生成/文生视频/LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049.json, 视频生成/文生视频/LTX2.3-文本音频生视频(口型同步)_2031312855026376705.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_31

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2034546381762863105.json、视频生成/图生视频/2031381886173450241.json、视频生成/图生视频/2034612488255315970.json、视频生成/图生视频/2036083633810837505.json、视频生成/图生视频/（1图 1音频）LTX2.3 图 + 音频数字人对口型_2111327625162612737.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `ResizeImageMaskNode` —— 8/9 个有
- `FishS2MultiSpeakerTTS` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `PreviewAny` —— 4/9 个有
- `SaveAudio` —— 4/9 个有
- `TextGenerateLTX2Prompt` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `SimpleMath+` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `LoadWhisperModel_` —— 1/9 个有
- `Qwen3ASRLoader_DFT` —— 1/9 个有
- `Qwen3ASRTranscribe_DFT` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `WhisperTranscribe_` —— 1/9 个有
- `easy int` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
