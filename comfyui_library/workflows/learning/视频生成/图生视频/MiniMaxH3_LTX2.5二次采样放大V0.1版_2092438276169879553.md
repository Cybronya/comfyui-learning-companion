---
key: 视频生成/图生视频/MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553.json
name: MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553.json
hash: 16ce4c07b6988ee9
coverage: 0.833333
learned_at: 2026-10-16 22:59:13
nodes: [VAELoader, VAELoader, VAEDecodeAudio, KSamplerSelect, BasicScheduler, BasicGuider, PrimitiveInt, MarkdownNote, VAELoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, MarkdownNote, ComfySwitchNode, ComfySwitchNode, SamplerCustomAdvanced, CreateVideo, UNETLoader, VAEDecode, LTXVImgToVideoInplace, LTXAddVideoICLoRAGuide, ImageFromBatch, CreateVideo, GetVideoComponents, RandomNoise, LoadImage, LTXVImgToVideoInplace, LTXVCropGuides, SamplerCustomAdvanced, SaveAudio, VAEDecodeTiled, ComfyMathExpression, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, ResolutionSelector, PrimitiveInt, PrimitiveBoolean, LoadImage, LoadImage, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, PrimitiveFloat, LoraLoaderModelOnly, CLIPLoader, LoadAudio, CLIPLoader, UNETLoader, LTXICLoRALoaderModelOnly, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, MarkdownNote, MarkdownNote, MarkdownNote, SaveVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `PrimitiveInt`
- `MarkdownNote`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LTXVImgToVideoInplace`
- `LTXAddVideoICLoRAGuide`
- `ImageFromBatch`
- `CreateVideo`
- `GetVideoComponents`
- `RandomNoise`
- `LoadImage`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `SaveAudio`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoadAudio`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `SaveVideo`

## 知识

覆盖率 **83%**（55/66）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`CreateVideo`、`UNETLoader`、`VAEDecode`、`LTXVImgToVideoInplace`、`LTXAddVideoICLoRAGuide`、`ImageFromBatch`、`GetVideoComponents`、`LoadImage`、`LTXVCropGuides`、`SaveAudio`、`VAEDecodeTiled`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`CLIPLoader`、`LoadAudio`、`LTXICLoRALoaderModelOnly`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
