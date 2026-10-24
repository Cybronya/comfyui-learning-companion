---
key: 图片生成/图生图/最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305.json
name: 最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305.json
hash: 8b22b3b56aee9864
coverage: 0.939394
learned_at: 2026-10-23 13:05:40
nodes: [UNETLoader, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ModelSamplingSD3, LayerUtility: PurgeVRAM, INPAINT_ExpandMask, easy showAnything, BBoxesToSAM2, LayerMask: LoadSAM2Model, VAELoader, InpaintModelConditioning, VAEDecode, PathchSageAttentionKJ, SeedVR2, LayerUtility: PurgeVRAM, LayerMask: SAM2UltraV2, MaskPreview+, InvertMask, CLIPTextEncode, QwenVLDetection, LayerUtility: PurgeVRAM V2, SaveImage, SaveImage, DownloadAndLoadQwenModel, LoadImage, PrimitiveFloat, KSampler, LoraLoaderModelOnly, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10}
---

# 图片生成/图生图/最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `INPAINT_ExpandMask`
- `easy showAnything`
- `BBoxesToSAM2`
- `LayerMask: LoadSAM2Model`
- `VAELoader`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `PathchSageAttentionKJ`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `LayerMask: SAM2UltraV2`
- `MaskPreview+`
- `InvertMask`
- `CLIPTextEncode` ★核心
- `QwenVLDetection`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `SaveImage`
- `DownloadAndLoadQwenModel`
- `LoadImage`
- `PrimitiveFloat`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `CR Prompt Text`

## 关键参数

- `seed` = `965369974524576`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`UNETLoader`、`LayerUtility: PurgeVRAM`、`LoraLoaderModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`INPAINT_ExpandMask`、`BBoxesToSAM2`、`LayerMask: LoadSAM2Model`、`VAELoader`、`InpaintModelConditioning`、`VAEDecode`、`PathchSageAttentionKJ`、`SeedVR2`、`LayerMask: SAM2UltraV2`、`MaskPreview+`、`InvertMask`、`QwenVLDetection`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`DownloadAndLoadQwenModel`、`LoadImage`、`KSampler`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
