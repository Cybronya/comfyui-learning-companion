---
key: 平台全量/FLUX.1 Redux（图像混合和重新创造）_1947214474668351489.json
name: FLUX.1 Redux（图像混合和重新创造）_1947214474668351489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1 Redux（图像混合和重新创造）_1947214474668351489.json
hash: 594a2f126590f9dd
coverage: 0.913978
learned_at: 2026-11-14 00:25:03
nodes: [CLIPVisionLoader, StyleModelLoader, CLIPVisionEncode, UNETLoader, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, Seed_, Int2String, FluxSamplerParams+, CLIPVisionLoader, UNETLoader, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, Seed_, Int2String, StyleModelLoader, FluxSamplerParams+, UNETLoader, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, Seed_, Int2String, FluxSamplerParams+, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, EmptyLatentImage, EmptyLatentImage, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, UNETLoader, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, Int2String, CLIPVisionLoader, StyleModelLoader, EmptyLatentImage, CLIPTextEncode, FluxSamplerParams+, Note, Note, Note, StyleModelApplySimple, Note, ReduxAdvanced, Seed_, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, StyleModelApply, Note, UNETLoader, DualCLIPLoader, VAELoader, VAEDecode, SaveImage, Int2String, CLIPVisionLoader, StyleModelLoader, EmptyLatentImage, FluxSamplerParams+, Seed_, ReduxAdvanced, Note, Note, ReduxAdvanced, ReduxAdvanced, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, LoadImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 768}
---

# 平台全量/FLUX.1 Redux（图像混合和重新创造）_1947214474668351489.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1 Redux（图像混合和重新创造）_1947214474668351489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（93 个）：
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Seed_`
- `Int2String`
- `FluxSamplerParams+` ★核心
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Seed_`
- `Int2String`
- `StyleModelLoader`
- `FluxSamplerParams+` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Seed_`
- `Int2String`
- `FluxSamplerParams+` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Int2String`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `FluxSamplerParams+` ★核心
- `Note`
- `Note`
- `Note`
- `StyleModelApplySimple`
- `Note`
- `ReduxAdvanced`
- `Seed_`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `StyleModelApply`
- `Note`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `Int2String`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `EmptyLatentImage` ★核心
- `FluxSamplerParams+` ★核心
- `Seed_`
- `ReduxAdvanced`
- `Note`
- `Note`
- `ReduxAdvanced`
- `ReduxAdvanced`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `Note`

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（85/93）

**有卡**：`CLIPVisionLoader`、`StyleModelLoader`、`CLIPVisionEncode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`Seed_`、`Int2String`、`FluxSamplerParams+`、`EmptyLatentImage`、`CLIPTextEncode`、`StyleModelApplySimple`、`ReduxAdvanced`、`LoadImage`、`StyleModelApply`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxSamplerParams+、Seed_
