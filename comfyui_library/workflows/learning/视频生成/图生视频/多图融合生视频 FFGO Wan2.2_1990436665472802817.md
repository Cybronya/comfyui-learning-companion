---
key: 视频生成/图生视频/多图融合生视频 FFGO Wan2.2_1990436665472802817.json
name: 多图融合生视频 FFGO Wan2.2_1990436665472802817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990436665472802817.json
hash: 3bcc0d1cff5d53d6
coverage: 0.735632
learned_at: 2026-10-15 22:33:10
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VHS_VideoCombine, VHS_VideoCombine, JWInteger, RIFE VFI, Fast Groups Bypasser (rgthree), VAELoader, CLIPLoader, GetNode, GetNode, CombinationText, CLIPTextEncode, CLIPTextEncode, PainterI2V, RH_Translator, AILab_QwenVL, easy cleanGpuUsed, RH_LLMAPI_NODE, easy cleanGpuUsed, LoadImage, TrimVideoLatent, VAEDecode, LoadImage, LoadImage, LoadImage, wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, SetNode, SetNode, LoraLoaderModelOnly, Note, LayerUtility: PurgeVRAM V2, CLIPVisionLoader, CLIPVisionEncode, Reroute, MathExpression|pysssss, PreviewAny, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, LoadImage, UNETLoader, UNETLoader, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, SetNode, RMBG, Reroute, RMBG, RMBG, ImageStitch, PreviewImage, ImageConcatMulti, ImageStitch, PreviewImage, ImageResizeKJv2, CR Text Input Switch (4 way), easy showAnything, Reroute, INTConstant, SetNode, ZML_AnyTypeSwitchFive, Note, CR Text, RMBG, Reroute, Reroute, Reroute, PreviewImage, Note, ImageConcatMulti, VHS_VideoCombine, ImageResizeKJv2, Reroute, Reroute]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/多图融合生视频 FFGO Wan2.2_1990436665472802817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990436665472802817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `RIFE VFI`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `CombinationText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PainterI2V`
- `RH_Translator`
- `AILab_QwenVL`
- `easy cleanGpuUsed`
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `LoadImage`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LayerUtility: PurgeVRAM V2`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `Reroute`
- `MathExpression|pysssss`
- `PreviewAny`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `SetNode`
- `RMBG`
- `Reroute`
- `RMBG`
- `RMBG`
- `ImageStitch`
- `PreviewImage`
- `ImageConcatMulti`
- `ImageStitch`
- `PreviewImage`
- `ImageResizeKJv2`
- `CR Text Input Switch (4 way)`
- `easy showAnything`
- `Reroute`
- `INTConstant`
- `SetNode`
- `ZML_AnyTypeSwitchFive`
- `Note`
- `CR Text`
- `RMBG`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Note`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `Reroute`
- `Reroute`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（64/87）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`VHS_VideoCombine`、`JWInteger`、`RIFE VFI`、`VAELoader`、`CLIPLoader`、`CombinationText`、`CLIPTextEncode`、`PainterI2V`、`RH_Translator`、`AILab_QwenVL`、`easy cleanGpuUsed`、`RH_LLMAPI_NODE`、`LoadImage`、`TrimVideoLatent`、`VAEDecode`、`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM V2`、`CLIPVisionLoader`、`CLIPVisionEncode`、`MathExpression|pysssss`、`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`INTConstant`、`RMBG`、`ImageStitch`、`ImageConcatMulti`、`ImageResizeKJv2`、`CR Text Input Switch (4 way)`、`ZML_AnyTypeSwitchFive`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
