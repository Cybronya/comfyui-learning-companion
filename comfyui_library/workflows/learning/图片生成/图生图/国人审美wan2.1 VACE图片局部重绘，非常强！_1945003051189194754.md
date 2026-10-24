---
key: 图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json
name: 国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json
hash: 0419c72388520d8b
coverage: 1
learned_at: 2026-10-23 12:37:46
nodes: [UNETLoader, KSampler, VAELoader, VAEDecode, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, CLIPTextEncode, InpaintModelConditioning, ModelSamplingSD3, LoadImage, CLIPTextEncode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 124212322639258, "steps": 10}
---

# 图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/国人审美wan2.1 VACE图片局部重绘，非常强！_1945003051189194754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `ModelSamplingSD3`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `124212322639258`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`UNETLoader`、`KSampler`、`VAELoader`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`CLIPTextEncode`、`InpaintModelConditioning`、`ModelSamplingSD3`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
