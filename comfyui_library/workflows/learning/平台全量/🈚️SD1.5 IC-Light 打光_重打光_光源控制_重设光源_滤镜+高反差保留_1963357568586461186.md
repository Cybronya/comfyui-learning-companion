---
key: 平台全量/🈚️SD1.5 IC-Light 打光_重打光_光源控制_重设光源_滤镜+高反差保留_1963357568586461186.json
name: 🈚️SD1.5 IC-Light 打光_重打光_光源控制_重设光源_滤镜+高反差保留_1963357568586461186
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/🈚️SD1.5 IC-Light 打光_重打光_光源控制_重设光源_滤镜+高反差保留_1963357568586461186.json
hash: a1d09ed5767371b2
coverage: 0.72
learned_at: 2026-11-14 02:54:24
nodes: [VAEEncode, CLIPVisionLoader, IPAdapterModelLoader, GetNode, SetNode, PatchModelAddDownscale, PreviewImage, easy imageDetailTransfer, Image High Pass Filter, Image High Pass Filter, SetNode, PreviewImage, GetNode, SetNode, SetNode, SetNode, GetNode, DetailTransfer, DetailTransfer, easy imageColorMatch, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, IPAdapterAdvanced, Anything Everywhere, LoadAndApplyICLightUnet, CheckpointLoaderSimple, Anything Everywhere3, CLIPTextEncode, SetNode, GetNode, LoadImage, LayerColor: Brightness & Contrast, LoadImage, ImageBlend, ICLightConditioning, KSampler, ImageScale, FastCanvasTool, workflow>深度检查2, RebatchLatents, LoadImage, LoadImage, CLIPTextEncode, PreviewImage, easy imageRemBg, ImageBatchMulti, workflow>深度检查3, LayerMask: Shadow & Highlight Mask, GetNode, AIO_Preprocessor, FastCanvas, easy imageRemBg, GetNode, LayerUtility: ColorPicker, PreviewImage, VAEEncode, RepeatLatentBatch, ImpactSwitch, ImageInvert, LayerStyle: Gradient Map, workflow>简易光源, LayerStyle: Gradient Map, SimpleMathSlider+, LayerColor: Color of Shadow & Highlight, MaskToImage, ImageScale, PreviewImage, ImageScale, LoadImage, GetNode, LayerUtility: ColorPicker, LayerUtility: ColorPicker, SaveImage, SaveImage, easy imageDetailTransfer]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2, "checkpoint": "写实 realisticVisionV50_v50VAE.safetensors", "denoise": 0.9000000000000001, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 957594817948241, "steps": 12}
---

# 平台全量/🈚️SD1.5 IC-Light 打光_重打光_光源控制_重设光源_滤镜+高反差保留_1963357568586461186.json

> 来源文件 `comfyui_library/workflows/平台全量/🈚️SD1.5 IC-Light 打光_重打光_光源控制_重设光源_滤镜+高反差保留_1963357568586461186.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `VAEEncode` ★核心
- `CLIPVisionLoader`
- `IPAdapterModelLoader`
- `GetNode`
- `SetNode`
- `PatchModelAddDownscale`
- `PreviewImage`
- `easy imageDetailTransfer`
- `Image High Pass Filter`
- `Image High Pass Filter`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `DetailTransfer`
- `DetailTransfer`
- `easy imageColorMatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `IPAdapterAdvanced`
- `Anything Everywhere`
- `LoadAndApplyICLightUnet`
- `CheckpointLoaderSimple` ★核心
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `LoadImage`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `ImageBlend`
- `ICLightConditioning`
- `KSampler` ★核心
- `ImageScale`
- `FastCanvasTool`
- `workflow>深度检查2`
- `RebatchLatents`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `easy imageRemBg`
- `ImageBatchMulti`
- `workflow>深度检查3`
- `LayerMask: Shadow & Highlight Mask`
- `GetNode`
- `AIO_Preprocessor`
- `FastCanvas`
- `easy imageRemBg`
- `GetNode`
- `LayerUtility: ColorPicker`
- `PreviewImage`
- `VAEEncode` ★核心
- `RepeatLatentBatch`
- `ImpactSwitch`
- `ImageInvert`
- `LayerStyle: Gradient Map`
- `workflow>简易光源`
- `LayerStyle: Gradient Map`
- `SimpleMathSlider+`
- `LayerColor: Color of Shadow & Highlight`
- `MaskToImage`
- `ImageScale`
- `PreviewImage`
- `ImageScale`
- `LoadImage`
- `GetNode`
- `LayerUtility: ColorPicker`
- `LayerUtility: ColorPicker`
- `SaveImage`
- `SaveImage`
- `easy imageDetailTransfer`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `写实 realisticVisionV50_v50VAE.safetensors`
- `seed` = `957594817948241`
- `steps` = `12`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.9000000000000001`

## 知识

覆盖率 **72%**（54/75）

**有卡**：`VAEEncode`、`CLIPVisionLoader`、`IPAdapterModelLoader`、`PatchModelAddDownscale`、`easy imageDetailTransfer`、`Image High Pass Filter`、`DetailTransfer`、`easy imageColorMatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`IPAdapterAdvanced`、`LoadAndApplyICLightUnet`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LoadImage`、`LayerColor: Brightness & Contrast`、`ImageBlend`、`ICLightConditioning`、`KSampler`、`ImageScale`、`FastCanvasTool`、`workflow>深度检查2`、`RebatchLatents`、`easy imageRemBg`、`ImageBatchMulti`、`workflow>深度检查3`、`LayerMask: Shadow & Highlight Mask`、`AIO_Preprocessor`、`FastCanvas`、`LayerUtility: ColorPicker`、`RepeatLatentBatch`、`ImageInvert`、`LayerStyle: Gradient Map`、`workflow>简易光源`、`SimpleMathSlider+`、`LayerColor: Color of Shadow & Highlight`、`MaskToImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、RebatchLatents、RepeatLatentBatch、VAEEncode
