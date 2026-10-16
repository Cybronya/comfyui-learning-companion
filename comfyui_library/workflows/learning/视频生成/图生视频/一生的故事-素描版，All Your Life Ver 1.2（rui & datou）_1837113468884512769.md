---
key: 视频生成/图生视频/一生的故事-素描版，All Your Life Ver 1.2（rui & datou）_1837113468884512769.json
name: 一生的故事-素描版，All Your Life Ver 1.2（rui & datou）_1837113468884512769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1837113468884512769.json
hash: 4a3f5a7879ed62f2
coverage: 0.807018
learned_at: 2026-10-15 22:29:13
nodes: [ShowText|pysssss, Text _O, Display Any (rgthree), Anything Everywhere, easy compare, Text Input Switch, Anything Everywhere3, StyleAlignedBatchAlign, LayerUtility: ImageBlend, VHS_LoadAudio, Anything Everywhere, ImageScaleToTotalPixels, ShowText|pysssss, BatchPromptSchedule, Text _O, Text _O, easy showAnything, LayerUtility: TextJoin, LayerUtility: TextJoin, EmptyLatentImage, easy imageSize, ApplyInstantID, PulidModelLoader, PulidEvaClipLoader, InstantIDFaceAnalysis, InstantIDModelLoader, InstantIDFaceAnalysis, ImageScaleToTotalPixels, DWPreprocessor, PreviewImage, ControlNetApplyAdvanced, Replace Text _O, Text _O, easy showAnything, easy showAnything, LoadImage, ControlNetLoader, ControlNetLoader, LoadImage, RIFE VFI, CheckpointLoaderSimple, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, LoadImage, KSampler (Efficient), PreviewImage, Image Filter Adjustments, KSampler (Efficient), VHS_VideoCombine, MiniCPM_VQA_Polished, Text _O, Text _O, easy cleanGpuUsed, MiniCPM_VQA_Polished, ApplyPulid, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"batch_size": 8, "cfg": 2, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 0.3, "height": 512, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 1, "steps": 8, "width": 512}
---

# 视频生成/图生视频/一生的故事-素描版，All Your Life Ver 1.2（rui & datou）_1837113468884512769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1837113468884512769.json`

## 结构

**生成流程**：Model → Latent → Control → Sampling → Process → Output → Other

**节点**（57 个）：
- `ShowText|pysssss`
- `Text _O`
- `Display Any (rgthree)`
- `Anything Everywhere`
- `easy compare`
- `Text Input Switch`
- `Anything Everywhere3`
- `StyleAlignedBatchAlign`
- `LayerUtility: ImageBlend`
- `VHS_LoadAudio`
- `Anything Everywhere`
- `ImageScaleToTotalPixels`
- `ShowText|pysssss`
- `BatchPromptSchedule`
- `Text _O`
- `Text _O`
- `easy showAnything`
- `LayerUtility: TextJoin`
- `LayerUtility: TextJoin`
- `EmptyLatentImage` ★核心
- `easy imageSize`
- `ApplyInstantID`
- `PulidModelLoader`
- `PulidEvaClipLoader`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `ImageScaleToTotalPixels`
- `DWPreprocessor`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `Replace Text _O`
- `Text _O`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `ControlNetLoader`
- `ControlNetLoader`
- `LoadImage`
- `RIFE VFI`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `KSampler (Efficient)` ★核心
- `PreviewImage`
- `Image Filter Adjustments`
- `KSampler (Efficient)` ★核心
- `VHS_VideoCombine`
- `MiniCPM_VQA_Polished`
- `Text _O`
- `Text _O`
- `easy cleanGpuUsed`
- `MiniCPM_VQA_Polished`
- `ApplyPulid`
- `easy cleanGpuUsed`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `8`
- `controlnet_strength` = `0.7000000000000001`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `seed` = `1`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.3`

## 知识

覆盖率 **81%**（46/57）

**有卡**：`Text _O`、`Display Any (rgthree)`、`easy compare`、`Text Input Switch`、`StyleAlignedBatchAlign`、`LayerUtility: ImageBlend`、`VHS_LoadAudio`、`ImageScaleToTotalPixels`、`BatchPromptSchedule`、`LayerUtility: TextJoin`、`EmptyLatentImage`、`easy imageSize`、`ApplyInstantID`、`PulidModelLoader`、`PulidEvaClipLoader`、`InstantIDFaceAnalysis`、`InstantIDModelLoader`、`DWPreprocessor`、`ControlNetApplyAdvanced`、`Replace Text _O`、`LoadImage`、`ControlNetLoader`、`RIFE VFI`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`KSampler (Efficient)`、`Image Filter Adjustments`、`VHS_VideoCombine`、`MiniCPM_VQA_Polished`、`easy cleanGpuUsed`、`ApplyPulid`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、KSampler (Efficient)、StyleAlignedBatchAlign
