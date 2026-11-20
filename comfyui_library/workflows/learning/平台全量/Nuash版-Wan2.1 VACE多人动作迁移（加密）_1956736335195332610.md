---
key: 平台全量/Nuash版-Wan2.1 VACE多人动作迁移（加密）_1956736335195332610.json
name: Nuash版-Wan2.1 VACE多人动作迁移（加密）_1956736335195332610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Nuash版-Wan2.1 VACE多人动作迁移（加密）_1956736335195332610.json
hash: 4a2011dbccba9f5e
coverage: 0.774194
learned_at: 2026-11-14 00:47:05
nodes: [LoadImage, ImageResizeKJv2, PreviewImage, VHS_LoadVideo, ImageResizeKJ, VHS_VideoInfo, easy showAnything, VHS_VideoCombine, ModelSamplingSD3, CLIPTextEncode, TrimVideoLatent, VAEDecode, ImageConcatMulti, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, easy int, easy int, Note, Note, CLIPTextEncode, Note, RHHiddenNodes, RHHiddenNodes, WanVaceToVideo, RHHiddenNodes, RHHiddenNodes, Note, VAELoader, Note]
patterns: []
missing: []
---

# 平台全量/Nuash版-Wan2.1 VACE多人动作迁移（加密）_1956736335195332610.json

> 来源文件 `comfyui_library/workflows/平台全量/Nuash版-Wan2.1 VACE多人动作迁移（加密）_1956736335195332610.json`

## 结构

**生成流程**：Model → Condition → Decode → Process → Output → Other

**节点**（31 个）：
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `VHS_VideoInfo`
- `easy showAnything`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `WanVaceToVideo`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Note`
- `VAELoader`
- `Note`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`LoadImage`、`ImageResizeKJv2`、`VHS_LoadVideo`、`ImageResizeKJ`、`VHS_VideoInfo`、`VHS_VideoCombine`、`ModelSamplingSD3`、`CLIPTextEncode`、`TrimVideoLatent`、`VAEDecode`、`ImageConcatMulti`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`easy int`、`RHHiddenNodes`、`WanVaceToVideo`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、TrimVideoLatent、ImageResizeKJ、ImageResizeKJv2、easy cleanGpuUsed
