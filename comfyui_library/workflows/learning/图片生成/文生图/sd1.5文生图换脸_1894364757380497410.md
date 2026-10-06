---
key: 图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json
name: sd1.5文生图换脸_1894364757380497410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json
hash: 1f8ce82d61a425bf
coverage: 0.769231
learned_at: 2026-10-07 03:18:01
nodes: [UltralyticsDetectorProvider, SAMLoader, IPAdapterUnifiedLoaderFaceID, IPAdapterFaceID, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, PreviewImage, SaveImage, LoadImage, WD14Tagger|pysssss, FaceDetailer]
patterns: []
missing: [WD14Tagger|pysssss, IPAdapterUnifiedLoaderFaceID]
parameters: {"checkpoint": "majicmixRealistic_v7.safetensors"}
discoveries: [次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `IPAdapterUnifiedLoaderFaceID` 仅有 IPAdapter 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json

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

覆盖率 **77%**（10/13）

**有卡**：`UltralyticsDetectorProvider`、`SAMLoader`、`IPAdapterFaceID`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`ColorMatch`、`SaveImage`、`LoadImage`、`FaceDetailer`

**缺卡**（2）：`WD14Tagger|pysssss`、`IPAdapterUnifiedLoaderFaceID`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、IPAdapterFaceID、SaveImage、FaceDetailer、SAMLoader、UltralyticsDetectorProvider

## 学习发现

- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `IPAdapterUnifiedLoaderFaceID` 仅有 IPAdapter 的通用知识，没有该节点自己的说明
