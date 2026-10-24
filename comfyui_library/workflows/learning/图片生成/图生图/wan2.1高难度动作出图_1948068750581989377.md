---
key: 图片生成/图生图/wan2.1高难度动作出图_1948068750581989377.json
name: wan2.1高难度动作出图_1948068750581989377
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1高难度动作出图_1948068750581989377.json
hash: 685182ee746f8655
coverage: 0.894737
learned_at: 2026-10-23 11:45:53
nodes: [InstructPixToPixConditioning, DualCLIPLoader, CLIPTextEncode, CLIPTextEncode, TeaCache, easy imagePixelPerfect, DepthAnythingV2Preprocessor, PreviewImage, VAELoader, PatchModelPatcherOrder, PathchSageAttentionKJ, PreviewImage, KSampler, VAEDecode, FluxGuidance, KSampler, VAEEncode, CLIPTextEncode, LayerUtility: ImageScaleRestore V2, CLIPVisionLoader, ReduxAdvanced, CLIPTextEncode, LayerUtility: Florence2Image2Prompt, LoraLoaderModelOnly, VAELoader, StyleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, VAEDecode, ShowText|pysssss, LayerMask: LoadFlorence2Model, SaveImage, PreviewImage, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.23000000000000004, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 736902951375876, "steps": 10}
---

# 图片生成/图生图/wan2.1高难度动作出图_1948068750581989377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1高难度动作出图_1948068750581989377.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `InstructPixToPixConditioning`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `TeaCache`
- `easy imagePixelPerfect`
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `VAELoader`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleRestore V2`
- `CLIPVisionLoader`
- `ReduxAdvanced`
- `CLIPTextEncode` ★核心
- `LayerUtility: Florence2Image2Prompt`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `StyleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `LayerMask: LoadFlorence2Model`
- `SaveImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `736902951375876`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `0.23000000000000004`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`InstructPixToPixConditioning`、`DualCLIPLoader`、`CLIPTextEncode`、`TeaCache`、`easy imagePixelPerfect`、`DepthAnythingV2Preprocessor`、`VAELoader`、`PatchModelPatcherOrder`、`PathchSageAttentionKJ`、`KSampler`、`VAEDecode`、`FluxGuidance`、`VAEEncode`、`LayerUtility: ImageScaleRestore V2`、`CLIPVisionLoader`、`ReduxAdvanced`、`LayerUtility: Florence2Image2Prompt`、`LoraLoaderModelOnly`、`StyleModelLoader`、`UNETLoader`、`CLIPLoader`、`LayerMask: LoadFlorence2Model`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
