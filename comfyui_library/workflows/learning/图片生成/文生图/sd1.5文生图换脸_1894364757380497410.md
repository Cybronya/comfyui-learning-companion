---
key: sd1.5文生图换脸_1894364757380497410.json
name: sd1.5文生图换脸_1894364757380497410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json
hash: 1f8ce82d61a425bf
coverage: 0.846154
learned_at: 2026-10-10 20:59:26
nodes: [UltralyticsDetectorProvider, SAMLoader, IPAdapterUnifiedLoaderFaceID, IPAdapterFaceID, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, PreviewImage, SaveImage, LoadImage, WD14Tagger|pysssss, FaceDetailer]
patterns: []
missing: [WD14Tagger|pysssss]
parameters: {"checkpoint": "majicmixRealistic_v7.safetensors"}
discoveries: [次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识]
---

# sd1.5文生图换脸_1894364757380497410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json`

## 结构

**生成流程**：Model → Condition → Control → Output → Other

**节点**（13 个）：
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `IPAdapterUnifiedLoaderFaceID`
- `IPAdapterFaceID`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ColorMatch`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `WD14Tagger|pysssss`
- `FaceDetailer`

## 关键参数

- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UltralyticsDetectorProvider`、`SAMLoader`、`IPAdapterUnifiedLoaderFaceID`、`IPAdapterFaceID`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`ColorMatch`、`SaveImage`、`LoadImage`、`FaceDetailer`

**缺卡**（1）：`WD14Tagger|pysssss`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、IPAdapterFaceID、IPAdapterUnifiedLoaderFaceID、SaveImage、FaceDetailer、SAMLoader

## 学习发现

- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
