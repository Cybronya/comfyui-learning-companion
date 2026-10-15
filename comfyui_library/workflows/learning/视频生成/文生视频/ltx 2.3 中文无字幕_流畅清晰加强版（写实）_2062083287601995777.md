---
key: 视频生成/文生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777.json
name: ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777.json
hash: e5db9c4ac33ef979
coverage: 0.848485
learned_at: 2026-10-15 22:47:21
nodes: [PrimitiveInt, LTXVSeparateAVLatent, LTXVAudioVAEEncode, SetNode, GetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVConditioning, LTXVCropGuides, MarkdownNote, CreateVideo, PrimitiveInt, SimpleMath+, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, UNETLoader, LTXLikenessGuide, Reroute, LTXFaceDetector, ImageScaleByAspectRatio_UTK, ComfyMathExpression, PrimitiveInt, PrimitiveBoolean, ResizeImageMaskNode, ResizeImagesByLongerEdge, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, LTXVLatentUpsampler, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXICLoRALoaderModelOnly, LTXVConcatAVLatent, LTXVPreprocess, LoadAudio, NormalizeAudioLoudness, TrimAudioDuration, PreviewAudio, AudioConcat, SetNode, VAEDecodeTiled, LTXVAudioVAEDecode, SaveVideo, MarkdownNote, ComfyMathExpression, PrimitiveInt, INTConstant, Text Multiline, CLIPTextEncode, Text Multiline, LoadImage, Prompt_Text, PromptRelayEncodeTimeline, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx 2.3 中文无字幕_流畅清晰加强版（写实）_2062083287601995777.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVCropGuides`
- `MarkdownNote`
- `CreateVideo`
- `PrimitiveInt`
- `SimpleMath+`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `LTXLikenessGuide`
- `Reroute`
- `LTXFaceDetector`
- `ImageScaleByAspectRatio_UTK`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `LoadAudio`
- `NormalizeAudioLoudness`
- `TrimAudioDuration`
- `PreviewAudio`
- `AudioConcat`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `MarkdownNote`
- `ComfyMathExpression`
- `PrimitiveInt`
- `INTConstant`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `LoadImage`
- `Prompt_Text`
- `PromptRelayEncodeTimeline`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（56/66）

**有卡**：`LTXVSeparateAVLatent`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVCropGuides`、`CreateVideo`、`SimpleMath+`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`LTXLikenessGuide`、`LTXFaceDetector`、`ImageScaleByAspectRatio_UTK`、`ComfyMathExpression`、`PrimitiveBoolean`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`SamplerCustomAdvanced`、`RandomNoise`、`LTXVLatentUpsampler`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXICLoRALoaderModelOnly`、`LTXVPreprocess`、`LoadAudio`、`NormalizeAudioLoudness`、`TrimAudioDuration`、`PreviewAudio`、`AudioConcat`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SaveVideo`、`INTConstant`、`Text Multiline`、`CLIPTextEncode`、`LoadImage`、`Prompt_Text`、`PromptRelayEncodeTimeline`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
