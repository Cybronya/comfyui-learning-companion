---
key: 视频生成/图生视频/BindWeave_single_image_1993600135810711553.json
name: BindWeave_single_image_1993600135810711553.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1993600135810711553.json
hash: 451183cb2dc7a9d9
coverage: 0.481481
learned_at: 2026-10-15 22:33:19
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, GetNode, GetNode, PreviewImage, MaskPreview, InvertMask, SetNode, SetNode, WanVideoModelLoader, SetNode, INTConstant, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, INTConstant, INTConstant, GetNode, LoadImage, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResizeKJv2, RMBG, WanVideoAddBindweaveEmbeds, WanVideoImageToVideoEncode, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, WanVideoEncodeLatentBatch, GetNode, GetNode, PrimitiveNode, TextImageEncodeQwenVL, CLIPLoader, SetNode, GetNode, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/BindWeave_single_image_1993600135810711553.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993600135810711553.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（54 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MaskPreview`
- `InvertMask`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `RMBG`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoImageToVideoEncode`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoEncodeLatentBatch`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `TextImageEncodeQwenVL`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`

## 知识

覆盖率 **48%**（26/54）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`MaskPreview`、`InvertMask`、`WanVideoModelLoader`、`INTConstant`、`LoadImage`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResizeKJv2`、`RMBG`、`WanVideoAddBindweaveEmbeds`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoEncodeLatentBatch`、`TextImageEncodeQwenVL`、`CLIPLoader`、`WanVideoTextEncode`

**用到的条目**：CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
