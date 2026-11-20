---
key: 平台全量/CCAI大猫一键换脸V3.0（支持RH端）_1896746133501435905.json
name: CCAI大猫一键换脸V3.0（支持RH端）_1896746133501435905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/CCAI大猫一键换脸V3.0（支持RH端）_1896746133501435905.json
hash: 92abf2bfee55aeeb
coverage: 0.839286
learned_at: 2026-11-14 00:21:30
nodes: [Note, CutForInpaint, ConstrainImage|pysssss, Unpack SDXL Tuple, Pack SDXL Tuple, InstantIDFaceAnalysis, ImageToMask, ConstrainImage|pysssss, MaskToImage, PreviewImage, ConstrainImage|pysssss, LayerMask: MaskPreview, Joy_caption, CLIPTextEncode, KSamplerSelect, BasicGuider, BasicScheduler, VAEDecode, SamplerCustomAdvanced, Note, Reroute, LoadImage, SaveImage, Note, VAELoader, LayerUtility: ImageRemoveAlpha, FeatheredMask, VAEEncodeForInpaint, VAEDecode, SaveImage, SUPIR_Upscale, BlendInpaint, Any Switch (rgthree), Image Comparer (rgthree), SaveImage, Note, ImageConcatMulti, SaveImage, EmptyLatentImage, TextInput_, Fast Groups Bypasser (rgthree), ttN concat, UNETLoader, Joy_caption_load, Eff. Loader SDXL, InstantIDModelLoader, ControlNetLoader, LayerMask: PersonMaskUltra V2, DualCLIPLoader, SaveImage, KSampler SDXL (Eff.), LoraLoaderModelOnly, LoadImage, LoadImage, RandomNoise, ApplyInstantID]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0, "height": 1280, "sampler_name": "dpmpp_sde", "scheduler": "normal", "seed": 774152991023931, "steps": 6, "width": 960}
---

# 平台全量/CCAI大猫一键换脸V3.0（支持RH端）_1896746133501435905.json

> 来源文件 `comfyui_library/workflows/平台全量/CCAI大猫一键换脸V3.0（支持RH端）_1896746133501435905.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `Note`
- `CutForInpaint`
- `ConstrainImage|pysssss`
- `Unpack SDXL Tuple`
- `Pack SDXL Tuple`
- `InstantIDFaceAnalysis`
- `ImageToMask`
- `ConstrainImage|pysssss`
- `MaskToImage`
- `PreviewImage`
- `ConstrainImage|pysssss`
- `LayerMask: MaskPreview`
- `Joy_caption`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Note`
- `Reroute`
- `LoadImage`
- `SaveImage`
- `Note`
- `VAELoader`
- `LayerUtility: ImageRemoveAlpha`
- `FeatheredMask`
- `VAEEncodeForInpaint` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SUPIR_Upscale`
- `BlendInpaint`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `ImageConcatMulti`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `ttN concat`
- `UNETLoader` ★核心
- `Joy_caption_load`
- `Eff. Loader SDXL`
- `InstantIDModelLoader`
- `ControlNetLoader`
- `LayerMask: PersonMaskUltra V2`
- `DualCLIPLoader`
- `SaveImage`
- `KSampler SDXL (Eff.)` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `ApplyInstantID`

## 关键参数

- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `774152991023931`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `normal`
- `denoise` = `0`

## 知识

覆盖率 **84%**（47/56）

**有卡**：`CutForInpaint`、`ConstrainImage|pysssss`、`Unpack SDXL Tuple`、`Pack SDXL Tuple`、`InstantIDFaceAnalysis`、`ImageToMask`、`MaskToImage`、`LayerMask: MaskPreview`、`Joy_caption`、`CLIPTextEncode`、`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`VAEDecode`、`SamplerCustomAdvanced`、`LoadImage`、`SaveImage`、`VAELoader`、`LayerUtility: ImageRemoveAlpha`、`FeatheredMask`、`VAEEncodeForInpaint`、`SUPIR_Upscale`、`BlendInpaint`、`ImageConcatMulti`、`EmptyLatentImage`、`TextInput_`、`ttN concat`、`UNETLoader`、`Joy_caption_load`、`Eff. Loader SDXL`、`InstantIDModelLoader`、`ControlNetLoader`、`LayerMask: PersonMaskUltra V2`、`DualCLIPLoader`、`KSampler SDXL (Eff.)`、`LoraLoaderModelOnly`、`RandomNoise`、`ApplyInstantID`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader
