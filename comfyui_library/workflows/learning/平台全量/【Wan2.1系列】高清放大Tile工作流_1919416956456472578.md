---
key: 平台全量/【Wan2.1系列】高清放大Tile工作流_1919416956456472578.json
name: 【Wan2.1系列】高清放大Tile工作流_1919416956456472578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.1系列】高清放大Tile工作流_1919416956456472578.json
hash: 25ede5998337c0ae
coverage: 0.636364
learned_at: 2026-11-14 01:22:22
nodes: [CLIPLoader, CLIPTextEncode, Note, ModelSamplingSD3, VHS_VideoCombine, Note, ImageScale, VHS_LoadVideo, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, InstructPixToPixConditioning, VAEDecode, KSampler, Reroute, ImageBlur, PrimitiveNode, PrimitiveNode, UNETLoader, Note, PreviewImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 484124163270679, "steps": 30}
---

# 平台全量/【Wan2.1系列】高清放大Tile工作流_1919416956456472578.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.1系列】高清放大Tile工作流_1919416956456472578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `Note`
- `ImageScale`
- `VHS_LoadVideo`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `InstructPixToPixConditioning`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Reroute`
- `ImageBlur`
- `PrimitiveNode`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `Note`
- `PreviewImage`
- `MarkdownNote`

## 关键参数

- `seed` = `484124163270679`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（14/22）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`VHS_VideoCombine`、`ImageScale`、`VHS_LoadVideo`、`VAELoader`、`LoraLoaderModelOnly`、`InstructPixToPixConditioning`、`VAEDecode`、`KSampler`、`ImageBlur`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、InstructPixToPixConditioning
