---
key: 图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json
name: Boogu Image 0.1 Single-Image Edit_2072998833342423040
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json
hash: 91b103555b02a410
coverage: 0.923077
learned_at: 2026-10-20 00:01:05
nodes: [UNETLoader, ModelSamplingAuraFlow, CLIPLoader, KSamplerSelect, VAELoader, BasicScheduler, VAEDecode, SaveImage, LoadImage, PreviewImage, SamplerCustom, EmptyLatentImage, UNETLoader, ModelSamplingAuraFlow, CLIPLoader, KSamplerSelect, VAELoader, BasicScheduler, VAEDecode, SaveImage, SamplerCustom, EmptyLatentImage, PreviewImage, UNETLoader, ModelSamplingAuraFlow, CLIPLoader, KSamplerSelect, VAELoader, BasicScheduler, VAEDecode, SaveImage, PreviewImage, SamplerCustom, EmptyLatentImage, UNETLoader, ModelSamplingAuraFlow, CLIPLoader, KSamplerSelect, VAELoader, BasicScheduler, VAEDecode, SaveImage, SamplerCustom, EmptyLatentImage, PreviewImage, UNETLoader, ModelSamplingAuraFlow, CLIPLoader, KSamplerSelect, VAELoader, BasicScheduler, VAEDecode, SaveImage, PreviewImage, SamplerCustom, EmptyLatentImage, UNETLoader, ModelSamplingAuraFlow, CLIPLoader, KSamplerSelect, VAELoader, BasicScheduler, VAEDecode, SaveImage, SamplerCustom, EmptyLatentImage, PreviewImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeBooguEdit, TextEncodeBooguEdit, TextEncodeBooguEdit, TextEncodeBooguEdit, TextEncodeBooguEdit, TextEncodeBooguEdit]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 720}
---

# 图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu Image 0.1 Single-Image Edit_2072998833342423040.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（78 个）：
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `BasicScheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `SamplerCustom` ★核心
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeBooguEdit`
- `TextEncodeBooguEdit`
- `TextEncodeBooguEdit`
- `TextEncodeBooguEdit`
- `TextEncodeBooguEdit`
- `TextEncodeBooguEdit`

## 关键参数

- `width` = `720`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（72/78）

**有卡**：`UNETLoader`、`ModelSamplingAuraFlow`、`CLIPLoader`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`VAEDecode`、`SaveImage`、`LoadImage`、`SamplerCustom`、`EmptyLatentImage`、`TextEncodeBooguEdit`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
