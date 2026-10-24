---
name: unknown_workflow_upscale_latent_upscale_lora_44
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.853857
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json, 视频生成/图生视频/【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json, 视频生成/图生视频/多人语音克隆+LTX2.3 音画同步 一步到位视频创作_2034546381762863105.json, 视频生成/图生视频/短剧工作流！FishAudio S2 + LTX-2.3生产力版_2034612488255315970.json, 视频生成/图生视频/输入台词就能生成短剧！（LTX-2.3配音术升级版）_2036083633810837505.json, 视频生成/文生视频/LTX-2.3配音术升级版：输入台词就能生成短剧！FishAudio S2 + LTX-2.3实战_2034068608220930049.json, 视频生成/文生视频/【LTX-2.3唱歌术】输入歌词就能生成MV？SongGeneration2+LTX2.3工作流实测_2033104945955741697.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_44

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/【LTX-2.3唱歌术】SongGeneration2+LTX2.3工作流_2046184684832428034.json、视频生成/图生视频/【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json、视频生成/图生视频/多人语音克隆+LTX2.3 音画同步 一步到位视频创作_2034546381762863105.json、视频生成/图生视频/短剧工作流！FishAudio S2 + LTX-2.3生产力版_2034612488255315970.json、视频生成/图生视频/输入台词就能生成短剧！（LTX-2.3配音术升级版）_2036083633810837505.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
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
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `SaveAudio` —— 6/7 个有
- `FishS2MultiSpeakerTTS` —— 4/7 个有
- `Label (rgthree)` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `SongGeneration_Loader` —— 2/7 个有
- `SongGeneration_Sampler` —— 2/7 个有
- `SongGeneration_Stage1` —— 2/7 个有
- `SongGeneration_Stage2` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `Float` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `LoadWhisperModel_` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有
- `Text` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `WhisperTranscribe_` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
