---
key: 图片生成/图生图/老照片修复_Stage.3.面部修复上色_1891419129482715137.json
name: 老照片修复_Stage.3.面部修复上色_1891419129482715137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老照片修复_Stage.3.面部修复上色_1891419129482715137.json
hash: 9c2ae2bef29408ec
coverage: 0.875
learned_at: 2026-10-23 13:22:56
nodes: [Stage2_load, Stage1_load, SelfAttentionGuidance, DifferentialDiffusion, GrowMaskWithBlur, LayerMask: HumanPartsUltra, BNK_CLIPTextEncodeAdvanced, BNK_CLIPTextEncodeAdvanced, StringFunction|pysssss, StringFunction|pysssss, PreviewImage, PowerPaint, CR Apply Multi-ControlNet, RepeatLatentBatch, KSamplerAdvanced //Inspire, DiffBIR_sample_advanced, AIO_Preprocessor, AIO_Preprocessor, AIO_Preprocessor, Reroute, GoogleTranslateTextNode, PreviewImage, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, FaceRestoreCFWithModel, FaceRestoreModelLoader, FaceRestoreModelLoader, FaceRestoreCFWithModel, BrushNetLoader, PowerPaintCLIPLoader, CR Multi-ControlNet Stack, VAEDecode, SaveImage, GoogleTranslateTextNode, Textbox, CheckpointLoader|pysssss, VAEEncode, VAEDecode, Note]
patterns: []
missing: []
parameters: {"cfg": 20, "checkpoint": "majicmixRealistic_v7.safetensors", "denoise": "karras", "sampler_name": 8, "scheduler": "dpmpp_2m_sde", "seed": true, "steps": "randomize"}
---

# 图片生成/图生图/老照片修复_Stage.3.面部修复上色_1891419129482715137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老照片修复_Stage.3.面部修复上色_1891419129482715137.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `Stage2_load`
- `Stage1_load`
- `SelfAttentionGuidance`
- `DifferentialDiffusion`
- `GrowMaskWithBlur`
- `LayerMask: HumanPartsUltra`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `PreviewImage`
- `PowerPaint`
- `CR Apply Multi-ControlNet`
- `RepeatLatentBatch`
- `KSamplerAdvanced //Inspire` ★核心
- `DiffBIR_sample_advanced`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `Reroute`
- `GoogleTranslateTextNode`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FaceRestoreCFWithModel`
- `FaceRestoreModelLoader`
- `FaceRestoreModelLoader`
- `FaceRestoreCFWithModel`
- `BrushNetLoader`
- `PowerPaintCLIPLoader`
- `CR Multi-ControlNet Stack`
- `VAEDecode` ★核心
- `SaveImage`
- `GoogleTranslateTextNode`
- `Textbox`
- `CheckpointLoader|pysssss` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Note`

## 关键参数

- `seed` = `True`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `8`
- `scheduler` = `dpmpp_2m_sde`
- `denoise` = `karras`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`Stage2_load`、`Stage1_load`、`SelfAttentionGuidance`、`DifferentialDiffusion`、`GrowMaskWithBlur`、`LayerMask: HumanPartsUltra`、`BNK_CLIPTextEncodeAdvanced`、`StringFunction|pysssss`、`PowerPaint`、`CR Apply Multi-ControlNet`、`RepeatLatentBatch`、`KSamplerAdvanced //Inspire`、`DiffBIR_sample_advanced`、`AIO_Preprocessor`、`GoogleTranslateTextNode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`FaceRestoreCFWithModel`、`FaceRestoreModelLoader`、`BrushNetLoader`、`PowerPaintCLIPLoader`、`CR Multi-ControlNet Stack`、`VAEDecode`、`SaveImage`、`Textbox`、`CheckpointLoader|pysssss`、`VAEEncode`

**用到的条目**：VAEDecode、LoadImage、CR Apply Multi-ControlNet、CR Multi-ControlNet Stack、KSamplerAdvanced //Inspire、SelfAttentionGuidance、RepeatLatentBatch、VAEEncode
