---
key: ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154.json
name: ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154.json
hash: 172b27e7e4b1e92d
coverage: 0.777778
learned_at: 2026-10-10 21:26:54
nodes: [KSamplerSelect, VAEDecode, SaveImage, BasicScheduler, BasicGuider, EmptySD3LatentImage, FluxGuidance, DualCLIPLoader, CLIPTextEncode, PrimitiveNode, PrimitiveNode, SamplerCustomAdvanced, Note, ModelSamplingFlux, VAELoader, Note, UNETLoader, RandomNoise]
patterns: []
missing: []
---

# ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ComfyUI官方示例11：Flux.1文生图工作流 _ ComfyUI从入门到精通_1932779421604401154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `BasicScheduler`
- `BasicGuider`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `ModelSamplingFlux`
- `VAELoader`
- `Note`
- `UNETLoader` ★核心
- `RandomNoise`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`KSamplerSelect`、`VAEDecode`、`SaveImage`、`BasicScheduler`、`BasicGuider`、`EmptySD3LatentImage`、`FluxGuidance`、`DualCLIPLoader`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`ModelSamplingFlux`、`VAELoader`、`UNETLoader`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、DualCLIPLoader
