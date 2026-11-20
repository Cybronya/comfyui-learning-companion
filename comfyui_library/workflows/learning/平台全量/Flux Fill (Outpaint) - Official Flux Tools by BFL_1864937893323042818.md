---
key: 平台全量/Flux Fill (Outpaint) - Official Flux Tools by BFL_1864937893323042818.json
name: Flux Fill (Outpaint) - Official Flux Tools by BFL_1864937893323042818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Fill (Outpaint) - Official Flux Tools by BFL_1864937893323042818.json
hash: caaa61fc6a2204f1
coverage: 0.875
learned_at: 2026-11-14 00:27:36
nodes: [UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncodeFlux, CLIPTextEncodeFlux, DifferentialDiffusion, LoadImage, InpaintModelConditioning, ImagePadForOutpaint, KSampler, ImageResizeKJ, SaveImage, MaskPreview+, VAEDecode, PreviewImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 462259889509663, "steps": 35}
---

# 平台全量/Flux Fill (Outpaint) - Official Flux Tools by BFL_1864937893323042818.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Fill (Outpaint) - Official Flux Tools by BFL_1864937893323042818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncodeFlux` ★核心
- `DifferentialDiffusion`
- `LoadImage`
- `InpaintModelConditioning`
- `ImagePadForOutpaint`
- `KSampler` ★核心
- `ImageResizeKJ`
- `SaveImage`
- `MaskPreview+`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `462259889509663`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncodeFlux`、`DifferentialDiffusion`、`LoadImage`、`InpaintModelConditioning`、`ImagePadForOutpaint`、`KSampler`、`ImageResizeKJ`、`SaveImage`、`MaskPreview+`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、LoadImage、CLIPTextEncodeFlux、DualCLIPLoader、InpaintModelConditioning
