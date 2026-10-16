---
key: 视频生成/图生视频/LTX-2.3 4宫格V3.0 红果短剧特调版 半自动(镜头硬切版)_2069688707870978050.json
name: LTX-2.3 4宫格V3.0 红果短剧特调版 半自动(镜头硬切版)_2069688707870978050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069688707870978050.json
hash: 2cf436403e8d4294
coverage: 0.551724
learned_at: 2026-10-15 22:40:32
nodes: [SimpleMath+, SetNode, GetNode, PrimitiveFloat, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, CR Float To Integer, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAELoader, LatentUpscaleModelLoader, SetNode, VAELoaderKJ, DualCLIPLoader, SetNode, SetNode, SetNode, CFGGuider, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConditioning, GetNode, easy cleanGpuUsed, VAEDecodeTiled, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, SamplerCustomAdvanced, ManualSigmas, SetNode, UNETLoader, TD_LTXVAddGuideFromGrid, TTResolutionSelector, ParseJsonNode, ShowText|pysssss, ParseJsonNode, ParseJsonNode, VHS_VideoCombine, ParseJsonNode, LoadImage, JWString, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3 4宫格V3.0 红果短剧特调版 半自动(镜头硬切版)_2069688707870978050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069688707870978050.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（58 个）：
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAELoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `GetNode`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `SetNode`
- `UNETLoader` ★核心
- `TD_LTXVAddGuideFromGrid`
- `TTResolutionSelector`
- `ParseJsonNode`
- `ShowText|pysssss`
- `ParseJsonNode`
- `ParseJsonNode`
- `VHS_VideoCombine`
- `ParseJsonNode`
- `LoadImage`
- `JWString`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（32/58）

**有卡**：`SimpleMath+`、`LTXVAudioVAEDecode`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAELoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`ManualSigmas`、`UNETLoader`、`TD_LTXVAddGuideFromGrid`、`TTResolutionSelector`、`ParseJsonNode`、`VHS_VideoCombine`、`LoadImage`、`JWString`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
