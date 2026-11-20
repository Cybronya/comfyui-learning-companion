---
key: 平台全量/Qwen-Edit2509 图像编辑 Pose姿势参考 V1.0_1971098337367756801.json
name: Qwen-Edit2509 图像编辑 Pose姿势参考 V1.0_1971098337367756801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Edit2509 图像编辑 Pose姿势参考 V1.0_1971098337367756801.json
hash: b62eb4864d69f192
coverage: 0.954545
learned_at: 2026-11-14 00:51:22
nodes: [ImageStitch, PreviewImage, SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, CLIPLoader, TextEncodeQwenImageEditPlus_lrzjason, KSampler, ConditioningZeroOut, VAEDecode, ImageConcatMulti, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, Text Multiline, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 618995998918011, "steps": 20}
---

# 平台全量/Qwen-Edit2509 图像编辑 Pose姿势参考 V1.0_1971098337367756801.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Edit2509 图像编辑 Pose姿势参考 V1.0_1971098337367756801.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ImageStitch`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `618995998918011`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`ImageStitch`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImageEditPlus_lrzjason`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`ImageConcatMulti`、`AIO_Preprocessor`、`UNETLoader`、`Text Multiline`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
