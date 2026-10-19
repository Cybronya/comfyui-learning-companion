---
key: 图片生成/文生图/Z-Image-Controlnet-2.1-2601-文生图_2011731536432865281.json
name: Z-Image-Controlnet-2.1-2601-文生图_2011731536432865281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-2601-文生图_2011731536432865281.json
hash: 1c47fb1b6c5c33f4
coverage: 0.84
learned_at: 2026-10-19 22:01:00
nodes: [DetailDaemonSamplerNode, RandomNoise, SamplerEulerAncestral, CLIPLoader, ConditioningZeroOut, CFGGuider, CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, UNETLoader, PrimitiveNode, Note, VAELoader, SamplerCustomAdvanced, PreviewImage, LayerUtility: PurgeVRAM V2, PreviewImage, SDPoseOODLoader, YOLOModelLoader, easy ifElse, RandomNoise, ModelSamplingAuraFlow, SamplerEulerAncestral, VAEDecode, SamplerCustomAdvanced, VAEDecode, CFGGuider, DetailDaemonSamplerNode, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, LatentUpscaleBy, String Literal, PreviewImage, LoraLoaderModelOnly, SDPoseOODProcessor, LoraLoaderModelOnly, ImageResizeKJv2, easy int, SplitSigmas, ZImageFunControlnet, VAEEncode, PreviewImage, PreviewImage, AIO_Preprocessor, ImageLoader, String Literal, ModelPatchLoader, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/Z-Image-Controlnet-2.1-2601-文生图_2011731536432865281.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Controlnet-2.1-2601-文生图_2011731536432865281.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
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
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `SDPoseOODLoader`
- `YOLOModelLoader`
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
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `SDPoseOODProcessor`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `easy int`
- `SplitSigmas`
- `ZImageFunControlnet`
- `VAEEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `ImageLoader`
- `String Literal`
- `ModelPatchLoader`
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **84%**（42/50）

**有卡**：`DetailDaemonSamplerNode`、`RandomNoise`、`SamplerEulerAncestral`、`CLIPLoader`、`ConditioningZeroOut`、`CFGGuider`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`UNETLoader`、`VAELoader`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM V2`、`SDPoseOODLoader`、`YOLOModelLoader`、`VAEDecode`、`BasicScheduler`、`LatentUpscaleBy`、`String Literal`、`LoraLoaderModelOnly`、`SDPoseOODProcessor`、`ImageResizeKJv2`、`easy int`、`SplitSigmas`、`ZImageFunControlnet`、`VAEEncode`、`AIO_Preprocessor`、`ImageLoader`、`ModelPatchLoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、ZImageFunControlnet
