---
key: 图片生成/图生图/FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306.json
name: FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306.json
hash: c16560204ccac689
coverage: 0.989899
learned_at: 2026-10-23 10:54:41
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPLoader, VAELoader, KSamplerSelect, ManualSigmas, EmptyFlux2LatentImage, RandomNoise, BasicGuider, SamplerCustomAdvanced, VAEDecode, UNETLoader, SaveImage, CLIPTextEncode, CLIPTextEncode, ReferenceMultiLatent, LoadImage, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, MuyeTextEditOutput, EmptyFlux2LatentImage, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, UNETLoader, LoadImage, CLIPLoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, UNETLoader, LoadImage, LoadImage, VAELoader, MuyeTextEditOutput, 孤海注释, MuyeTextEditOutput, CLIPLoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, LoadImage, VAELoader, MuyeTextEditOutput, CLIPLoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, LoadImage, VAELoader, MuyeTextEditOutput, 忽略多组孤海, UNETLoader, LoadImage, LoadImage, UNETLoader, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX3.0Klein文生图单双多图编辑全套工作流_2110917466762338306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceMultiLatent`
- `LoadImage`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `MuyeTextEditOutput`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `SaveImage`
- `LoadImage`
- `ReferenceMultiLatent`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `SaveImage`
- `LoadImage`
- `ReferenceMultiLatent`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `MuyeTextEditOutput`
- `孤海注释`
- `MuyeTextEditOutput`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `SaveImage`
- `LoadImage`
- `ReferenceMultiLatent`
- `LoadImage`
- `VAELoader`
- `MuyeTextEditOutput`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `SaveImage`
- `LoadImage`
- `ReferenceMultiLatent`
- `LoadImage`
- `VAELoader`
- `MuyeTextEditOutput`
- `忽略多组孤海`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **99%**（98/99）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`ManualSigmas`、`EmptyFlux2LatentImage`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ReferenceMultiLatent`、`LoadImage`、`MuyeTextEditOutput`、`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、KSamplerSelect
