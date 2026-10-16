---
key: 视频生成/图生视频/视频生成视频_图生视频-动作迁移+人脸迁移-wan2.1_1958334806830551042.json
name: 视频生成视频_图生视频-动作迁移+人脸迁移-wan2.1_1958334806830551042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958334806830551042.json
hash: 7110f14ffd586b22
coverage: 0.878788
learned_at: 2026-10-15 22:31:21
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, FaceProcessorLoader, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoSetLoRAs, Anything Everywhere, Anything Everywhere, VHS_VideoCombine, WanVideoLoraSelect, WanVideoVACEEncode, WanVideoSampler, WanVideoDecode, ApplyFaceProcessor, VHS_VideoCombine, ImageResizeKJv2, AIO_Preprocessor, PreviewImage, WanVideoEncode, WanVideoAddStandInLatent, WanVideoVAELoader, Anything Everywhere, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTextEncode, CR Text, VHS_LoadVideo, MathExpression|pysssss, Int, LoadImage, INTConstant, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/视频生成视频_图生视频-动作迁移+人脸迁移-wan2.1_1958334806830551042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958334806830551042.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `FaceProcessorLoader`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `Anything Everywhere`
- `Anything Everywhere`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ApplyFaceProcessor`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `AIO_Preprocessor`
- `PreviewImage`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `CR Text`
- `VHS_LoadVideo`
- `MathExpression|pysssss`
- `Int`
- `LoadImage`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`FaceProcessorLoader`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoDecode`、`ApplyFaceProcessor`、`ImageResizeKJv2`、`AIO_Preprocessor`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`CR Text`、`VHS_LoadVideo`、`MathExpression|pysssss`、`Int`、`LoadImage`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoAddStandInLatent
