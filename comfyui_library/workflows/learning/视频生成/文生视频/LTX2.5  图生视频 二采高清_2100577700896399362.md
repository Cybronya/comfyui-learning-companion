---
key: 视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json
name: LTX2.5  图生视频 二采高清_2100577700896399362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json
hash: 64d5d0f02271c786
coverage: 0.9375
learned_at: 2026-10-11 22:12:35
nodes: [CLIPLoader, PrimitiveBoolean, UNETLoader, Int, PrimitiveBoolean, VAELoader, VAELoader, CLIPLoader, KSamplerSelect, RandomNoise, ManualSigmas, Int, LatentUpscaleModelLoader, RandomNoise, ManualSigmas, KSamplerSelect, Int, CLIPTextEncode, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, LTXVPreprocess, GetImageSize, TextGenerateLTX2Prompt, EmptyLTXVLatentVideo, ComfySwitchNode, LTXVImgToVideoInplace, CLIPTextEncode, PreviewAny, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, PurgeVRAM_UTK, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, ResizeImageMaskNode, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5  图生视频 二采高清_2100577700896399362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `CLIPLoader`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `Int`
- `PrimitiveBoolean`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `Int`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `Int`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `GetImageSize`
- `TextGenerateLTX2Prompt`
- `EmptyLTXVLatentVideo`
- `ComfySwitchNode`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `PurgeVRAM_UTK`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ResizeImageMaskNode`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（45/48）

**有卡**：`CLIPLoader`、`PrimitiveBoolean`、`UNETLoader`、`Int`、`VAELoader`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`GetImageSize`、`TextGenerateLTX2Prompt`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`PurgeVRAM_UTK`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ResizeImageMaskNode`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
