---
key: 平台全量/蒙版局部重绘｜Qwen-Image 2.1 ControlNet INT8_2119400757240881153.json
name: 蒙版局部重绘｜Qwen-Image 2.1 ControlNet INT8_2119400757240881153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/蒙版局部重绘｜Qwen-Image 2.1 ControlNet INT8_2119400757240881153.json
hash: 75cfa6abbcf75a2a
coverage: 1
learned_at: 2026-11-14 02:33:06
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, SaveImage, QwenImage21Cache, BasicScheduler, LoadImage, ModelPatchLoader, ZImageFunControlnet, LoadImageMask]
patterns: []
missing: []
---

# 平台全量/蒙版局部重绘｜Qwen-Image 2.1 ControlNet INT8_2119400757240881153.json

> 来源文件 `comfyui_library/workflows/平台全量/蒙版局部重绘｜Qwen-Image 2.1 ControlNet INT8_2119400757240881153.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `BasicScheduler`
- `LoadImage`
- `ModelPatchLoader`
- `ZImageFunControlnet`
- `LoadImageMask`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`BasicScheduler`、`LoadImage`、`ModelPatchLoader`、`ZImageFunControlnet`、`LoadImageMask`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader、ZImageFunControlnet
