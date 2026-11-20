---
key: 平台全量/lora 换脸 - F.1_1899062120691187714.json
name: lora 换脸 - F.1_1899062120691187714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/lora 换脸 - F.1_1899062120691187714.json
hash: 8b9b2f045ee86e2f
coverage: 1
learned_at: 2026-11-14 01:14:30
nodes: [FaceDetailer, SaveImage, CLIPTextEncode, UltralyticsDetectorProvider, SAMLoader, CLIPTextEncodeFlux, VAELoader, DualCLIPLoader, CR Text, UNETLoader, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/lora 换脸 - F.1_1899062120691187714.json

> 来源文件 `comfyui_library/workflows/平台全量/lora 换脸 - F.1_1899062120691187714.json`

## 结构

**生成流程**：Model → Condition → Output → Other

**节点**（12 个）：
- `FaceDetailer`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `CLIPTextEncodeFlux` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CR Text`
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **100%**（12/12）

**有卡**：`FaceDetailer`、`SaveImage`、`CLIPTextEncode`、`UltralyticsDetectorProvider`、`SAMLoader`、`CLIPTextEncodeFlux`、`VAELoader`、`DualCLIPLoader`、`CR Text`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、DualCLIPLoader、SaveImage
