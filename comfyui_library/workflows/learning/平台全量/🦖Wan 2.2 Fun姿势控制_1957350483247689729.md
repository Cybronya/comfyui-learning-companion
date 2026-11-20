---
key: 平台全量/🦖Wan 2.2 Fun姿势控制_1957350483247689729.json
name: 🦖Wan 2.2 Fun姿势控制_1957350483247689729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🦖Wan 2.2 Fun姿势控制_1957350483247689729.json
hash: 61089651b7e8e87b
coverage: 1
learned_at: 2026-11-14 02:55:46
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, Wan22FunControlToVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, Canny, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, VHS_VideoCombine, GetVideoComponents, DWPreprocessor, VAEDecode, ImageConcanate, PDIMAGE_LongerSize, JWInteger, CLIPTextEncode, ACE_ImageGetSize, ResizeLongestToNode, SaveImage, JWInteger, ImageResizeKJv2, JWInteger, LoadImage, CR Prompt Text, RH_Captioner, LoadVideo, VHS_VideoCombine, PDIMAGE_LongerSize, ImageConcanate, PDIMAGE_LongerSize, ImageConcanate]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/🦖Wan 2.2 Fun姿势控制_1957350483247689729.json

> 来源文件 `comfyui_library/workflows/平台全量/🦖Wan 2.2 Fun姿势控制_1957350483247689729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Wan22FunControlToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Canny`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `GetVideoComponents`
- `DWPreprocessor`
- `VAEDecode` ★核心
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `ACE_ImageGetSize`
- `ResizeLongestToNode`
- `SaveImage`
- `JWInteger`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `CR Prompt Text`
- `RH_Captioner`
- `LoadVideo`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `ImageConcanate`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（37/37）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`Wan22FunControlToVideo`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VHS_VideoCombine`、`Canny`、`UNETLoader`、`LoraLoaderModelOnly`、`GetVideoComponents`、`DWPreprocessor`、`VAEDecode`、`ImageConcanate`、`PDIMAGE_LongerSize`、`JWInteger`、`ACE_ImageGetSize`、`ResizeLongestToNode`、`SaveImage`、`ImageResizeKJv2`、`LoadImage`、`CR Prompt Text`、`RH_Captioner`、`LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、Canny
