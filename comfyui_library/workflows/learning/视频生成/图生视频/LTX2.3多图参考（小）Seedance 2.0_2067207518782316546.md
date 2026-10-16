---
key: 视频生成/图生视频/LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json
name: LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067207518782316546.json
hash: d682f452c5b63fbc
coverage: 0.615385
learned_at: 2026-10-15 22:39:58
nodes: [UNETLoader, VAELoader, VAELoader, LTXICLoRALoaderModelOnly, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, CLIPTextEncode, LTXVConditioning, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, INTConstant, CFGGuider, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CreateVideo, VAEDecode, LTXVCropGuides, LTXVEmptyLatentAudio, ManualSigmas, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, LTXVConcatAVLatent, LTXAddVideoICLoRAGuide, SetNode, LiconMSR, DualCLIPLoader, SetNode, LoadImage, MuyeTextEditOutput, GetNode, SaveVideo, INTConstant, INTConstant, SetNode, LoadImage, SetNode, SetNode, SetNode, SetNode, LoadImage, SetNode, Note, LoadImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067207518782316546.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（52 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `INTConstant`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXAddVideoICLoRAGuide`
- `SetNode`
- `LiconMSR`
- `DualCLIPLoader`
- `SetNode`
- `LoadImage`
- `MuyeTextEditOutput`
- `GetNode`
- `SaveVideo`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `Note`
- `LoadImage`
- `Note`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（32/52）

**有卡**：`UNETLoader`、`VAELoader`、`LTXICLoRALoaderModelOnly`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`INTConstant`、`CFGGuider`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`CreateVideo`、`VAEDecode`、`LTXVCropGuides`、`LTXVEmptyLatentAudio`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`LiconMSR`、`DualCLIPLoader`、`LoadImage`、`MuyeTextEditOutput`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
