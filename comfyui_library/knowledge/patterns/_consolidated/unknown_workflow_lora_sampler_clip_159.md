---
name: unknown_workflow_lora_sampler_clip_159
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.802
common_nodes: [AudioCrop, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoadAudio, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, UnetLoaderGGUF, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3-Image-Audio-Video-GGUF_2031903098767155201.json, 视频生成/图生视频/LTX2.3 图像+独立音频+人物对口型+去字幕视频_2035354281682935809.json, 视频生成/文生视频/LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362.json, 视频生成/文生视频/LTX-2.3-文生视频 GGUF版_2032080178574266370.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3-Image-Audio-Video-GGUF_2031903098767155201.json、视频生成/图生视频/LTX2.3 图像+独立音频+人物对口型+去字幕视频_2035354281682935809.json、视频生成/文生视频/LTX-2.3-Text-Audio-Video-GGUF_2031898345630863362.json、视频生成/文生视频/LTX-2.3-文生视频 GGUF版_2032080178574266370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `Float` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImageScaleBy` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LTXVLatentUpsampler` —— 2/4 个有
- `LTXVPreprocess` —— 2/4 个有
- `LatentUpscaleModelLoader` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `LTX2_NAG` —— 1/4 个有
- `MaskPreview` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
