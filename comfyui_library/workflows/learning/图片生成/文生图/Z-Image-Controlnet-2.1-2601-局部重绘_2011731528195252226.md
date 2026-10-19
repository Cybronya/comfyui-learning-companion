---
key: 图片生成/文生图/Z-Image-Controlnet-2.1-2601-局部重绘_2011731528195252226.json
name: Z-Image-Controlnet-2.1-2601-局部重绘_2011731528195252226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-2601-局部重绘_2011731528195252226.json
hash: 331b3513dd1669fa
coverage: 0.843137
learned_at: 2026-10-19 22:01:00
nodes: [DetailDaemonSamplerNode, RandomNoise, SamplerEulerAncestral, CLIPLoader, ConditioningZeroOut, CFGGuider, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, UNETLoader, PrimitiveNode, Note, VAELoader, SamplerCustomAdvanced, SetLatentNoiseMask, PreviewImage, LayerUtility: PurgeVRAM V2, PreviewImage, SDPoseOODLoader, YOLOModelLoader, AIO_Preprocessor, easy ifElse, RandomNoise, ModelSamplingAuraFlow, SamplerEulerAncestral, VAEDecode, SamplerCustomAdvanced, VAEDecode, CFGGuider, DetailDaemonSamplerNode, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, LatentUpscaleBy, String Literal, SDPoseOODProcessor, String Literal, LoraLoaderModelOnly, ImageResizeKJv2, easy int, SplitSigmas, VAEEncode, PreviewImage, ModelPatchLoader, ImageLoader, LoraLoaderModelOnly, PreviewImage, PreviewImage, ZImageFunControlnet, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/Z-Image-Controlnet-2.1-2601-局部重绘_2011731528195252226.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-2601-局部重绘_2011731528195252226.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `DetailDaemonSamplerNode` ★核心
- `RandomNoise`
- `SamplerEulerAncestral` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PrimitiveNode`
- `Note`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `SetLatentNoiseMask`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `AIO_Preprocessor`
- `easy ifElse`
- `RandomNoise`
- `ModelSamplingAuraFlow`
- `SamplerEulerAncestral` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CFGGuider`
- `DetailDaemonSamplerNode` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleBy`
- `String Literal`
- `SDPoseOODProcessor`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `easy int`
- `SplitSigmas`
- `VAEEncode` ★核心
- `PreviewImage`
- `ModelPatchLoader`
- `ImageLoader`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `PreviewImage`
- `ZImageFunControlnet`
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`DetailDaemonSamplerNode`、`RandomNoise`、`SamplerEulerAncestral`、`CLIPLoader`、`ConditioningZeroOut`、`CFGGuider`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`UNETLoader`、`VAELoader`、`SamplerCustomAdvanced`、`SetLatentNoiseMask`、`LayerUtility: PurgeVRAM V2`、`SDPoseOODLoader`、`YOLOModelLoader`、`AIO_Preprocessor`、`VAEDecode`、`BasicScheduler`、`LatentUpscaleBy`、`String Literal`、`SDPoseOODProcessor`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`easy int`、`SplitSigmas`、`VAEEncode`、`ModelPatchLoader`、`ImageLoader`、`ZImageFunControlnet`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、ZImageFunControlnet
