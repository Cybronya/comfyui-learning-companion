---
key: 视频生成/文生视频/Wan2.2文生视频KJ版_1950074509607002113.json
name: Wan2.2文生视频KJ版_1950074509607002113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频KJ版_1950074509607002113.json
hash: e03b40da393a09aa
coverage: 0.882353
learned_at: 2026-10-15 22:47:15
nodes: [WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, ShowText|pysssss, Wan_video_prompt_generator, easy cleanGpuUsed, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelect, PrimitiveInt, PrimitiveInt, CR Text, WanVideoTextEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, LoadImage, ImageFromBatch+, INTConstant, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2文生视频KJ版_1950074509607002113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频KJ版_1950074509607002113.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoEmptyEmbeds`
- `WanVideoTorchCompileSettings`
- `ShowText|pysssss`
- `Wan_video_prompt_generator`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `PrimitiveInt`
- `PrimitiveInt`
- `CR Text`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ImageFromBatch+`
- `INTConstant`
- `MarkdownNote`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`WanVideoVAELoader`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`Wan_video_prompt_generator`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`CR Text`、`WanVideoTextEncode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoSampler`、`LoadImage`、`ImageFromBatch+`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
