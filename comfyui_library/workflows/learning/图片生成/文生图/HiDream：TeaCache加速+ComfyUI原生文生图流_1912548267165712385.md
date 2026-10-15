---
key: 图片生成/文生图/HiDream：TeaCache加速+ComfyUI原生文生图流_1912548267165712385.json
name: HiDream：TeaCache加速+ComfyUI原生文生图流_1912548267165712385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HiDream：TeaCache加速+ComfyUI原生文生图流_1912548267165712385.json
hash: 2c2a73fb639dfc7e
coverage: 0.807692
learned_at: 2026-10-15 22:26:32
nodes: [VAEDecode, VAELoader, MarkdownNote, UnetLoaderGGUF, MarkdownNote, EmptySD3LatentImage, CLIPTextEncode, QuadrupleCLIPLoader, CLIPTextEncode, KSampler, RH_Captioner, ModelSamplingSD3, TeaCache, UNETLoader, LoraLoaderModelOnly, SaveImage, Note, Text Multiline, Text Concatenate, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, easy showAnything, Fast Groups Bypasser (rgthree), LoadImage, CR SDXL Aspect Ratio, LayerUtility: JoyCaptionBeta1ExtraOptions]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 469837589725453, "steps": 50}
---

# 图片生成/文生图/HiDream：TeaCache加速+ComfyUI原生文生图流_1912548267165712385.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/HiDream：TeaCache加速+ComfyUI原生文生图流_1912548267165712385.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `MarkdownNote`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `QuadrupleCLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `RH_Captioner`
- `ModelSamplingSD3`
- `TeaCache`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Note`
- `Text Multiline`
- `Text Concatenate`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CR SDXL Aspect Ratio`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`

## 关键参数

- `seed` = `469837589725453`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`VAEDecode`、`VAELoader`、`UnetLoaderGGUF`、`EmptySD3LatentImage`、`CLIPTextEncode`、`QuadrupleCLIPLoader`、`KSampler`、`RH_Captioner`、`ModelSamplingSD3`、`TeaCache`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`Text Multiline`、`Text Concatenate`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`LoadImage`、`CR SDXL Aspect Ratio`、`LayerUtility: JoyCaptionBeta1ExtraOptions`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、CR SDXL Aspect Ratio
