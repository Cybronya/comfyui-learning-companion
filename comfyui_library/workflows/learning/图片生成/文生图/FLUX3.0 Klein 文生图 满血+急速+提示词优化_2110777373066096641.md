---
key: 图片生成/文生图/FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641.json
name: FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641.json
hash: e82a5b46c53e4b46
coverage: 0.757576
learned_at: 2026-10-21 02:51:55
nodes: [VAELoader, CreateBoundingBoxes, Int, PrimitiveStringMultiline, CLIPLoader, CLIPLoader, Int, CLIPTextEncode, KSamplerSelect, CLIPTextEncode, RandomNoise, ManualSigmas, BasicGuider, PrimitiveBoolean, KSampler, SamplerCustomAdvanced, ComfySwitchNode, UNETLoader, UNETLoader, ResolutionSelector, EmptyFlux2LatentImage, AnySwitch, PrimitiveStringMultiline, MarkdownNote, Note, PreviewAny, Fast Bypasser (rgthree), PrimitiveBoolean, VAEDecode, SaveImage, TextGenerate, ComfySwitchNode, PreviewAny]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 442728308303170, "steps": 15}
---

# 图片生成/文生图/FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX3.0 Klein 文生图 满血+急速+提示词优化_2110777373066096641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `VAELoader`
- `CreateBoundingBoxes`
- `Int`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPLoader`
- `Int`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `ManualSigmas`
- `BasicGuider`
- `PrimitiveBoolean`
- `KSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `EmptyFlux2LatentImage`
- `AnySwitch`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `Note`
- `PreviewAny`
- `Fast Bypasser (rgthree)`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SaveImage`
- `TextGenerate`
- `ComfySwitchNode`
- `PreviewAny`

## 关键参数

- `seed` = `442728308303170`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（25/33）

**有卡**：`VAELoader`、`CreateBoundingBoxes`、`Int`、`CLIPLoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`BasicGuider`、`PrimitiveBoolean`、`KSampler`、`SamplerCustomAdvanced`、`UNETLoader`、`ResolutionSelector`、`EmptyFlux2LatentImage`、`AnySwitch`、`Fast Bypasser (rgthree)`、`VAEDecode`、`SaveImage`、`TextGenerate`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、KSamplerSelect
