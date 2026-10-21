---
key: 图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json
name: FLUX3.0 Klein 全套工作流精品_2112068071841157122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json
hash: 2751837f3d2278c2
coverage: 0.99
learned_at: 2026-10-21 02:51:55
nodes: [CLIPLoader, VAELoader, CLIPLoader, VAELoader, KSamplerSelect, ManualSigmas, EmptyFlux2LatentImage, RandomNoise, BasicGuider, SamplerCustomAdvanced, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, ReferenceMultiLatent, LoadImage, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, MuyeTextEditOutput, EmptyFlux2LatentImage, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, LoadImage, CLIPLoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, LoadImage, LoadImage, VAELoader, MuyeTextEditOutput, 孤海注释, MuyeTextEditOutput, CLIPLoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, LoadImage, VAELoader, MuyeTextEditOutput, CLIPLoader, CLIPTextEncode, BasicGuider, KSamplerSelect, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, SaveImage, LoadImage, ReferenceMultiLatent, LoadImage, VAELoader, MuyeTextEditOutput, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 忽略多组孤海, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX3.0 Klein 全套工作流精品_2112068071841157122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
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
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 知识

覆盖率 **99%**（99/100）

**有卡**：`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`ManualSigmas`、`EmptyFlux2LatentImage`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ReferenceMultiLatent`、`LoadImage`、`MuyeTextEditOutput`、`忽略多组孤海`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage、KSamplerSelect
