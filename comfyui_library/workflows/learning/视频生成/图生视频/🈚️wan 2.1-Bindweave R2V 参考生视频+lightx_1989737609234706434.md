---
key: 视频生成/图生视频/🈚️wan 2.1-Bindweave R2V 参考生视频+lightx_1989737609234706434.json
name: 🈚️wan 2.1-Bindweave R2V 参考生视频+lightx_1989737609234706434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/🈚️wan 2.1-Bindweave R2V 参考生视频+lightx_1989737609234706434.json
hash: 317d670e0cede47a
coverage: 0.488889
learned_at: 2026-10-15 22:33:08
nodes: [WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, GetNode, GetNode, WanVideoDecode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, TextImageEncodeQwenVL, SetNode, GetNode, WanVideoImageToVideoEncode, ImageResizeKJv2, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, GetNode, GetNode, WanVideoAddBindweaveEmbeds, CLIPLoader, SetNode, WanVideoEncodeLatentBatch, Int, WanVideoTextEncode, GetNode, GetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, PreviewImage, WanVideoSampler, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoSetLoRAs, LoadImage, WanVideoLoraSelect, easy imageRemBg, WanVideoLoraSelect, GetNode, GetNode, GetNode, GetNode, GetNode, 孤海图像组合批次, GetNode, 孤海图像组合批次, InvertMask, MaskToImage, SetNode, SetNode, MaskToImage, SolidMask, SetNode, InvertMask, SetNode, MaskToImage, GetNode, GetNode, 孤海图像组合批次, GetNode, ImageToMask, LoadImage, GetNode, GetNode, LoadImage, easy imageRemBg, Text, Int, Int, Fast Groups Muter (rgthree), ImageResizeKJv2, WanVideoDecode, SetNode, PreviewImage, GetNode, VHS_VideoCombine, PreviewImage, MaskPreview]
patterns: []
missing: []
---

# 视频生成/图生视频/🈚️wan 2.1-Bindweave R2V 参考生视频+lightx_1989737609234706434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1989737609234706434.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（90 个）：
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `TextImageEncodeQwenVL`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `WanVideoAddBindweaveEmbeds`
- `CLIPLoader`
- `SetNode`
- `WanVideoEncodeLatentBatch`
- `Int`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `LoadImage`
- `WanVideoLoraSelect`
- `easy imageRemBg`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `孤海图像组合批次`
- `GetNode`
- `孤海图像组合批次`
- `InvertMask`
- `MaskToImage`
- `SetNode`
- `SetNode`
- `MaskToImage`
- `SolidMask`
- `SetNode`
- `InvertMask`
- `SetNode`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `孤海图像组合批次`
- `GetNode`
- `ImageToMask`
- `LoadImage`
- `GetNode`
- `GetNode`
- `LoadImage`
- `easy imageRemBg`
- `Text`
- `Int`
- `Int`
- `Fast Groups Muter (rgthree)`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `MaskPreview`

## 知识

覆盖率 **49%**（44/90）

**有卡**：`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`TextImageEncodeQwenVL`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoAddBindweaveEmbeds`、`CLIPLoader`、`WanVideoEncodeLatentBatch`、`Int`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoLoraSelect`、`easy imageRemBg`、`孤海图像组合批次`、`InvertMask`、`MaskToImage`、`SolidMask`、`ImageToMask`、`Text`、`VHS_VideoCombine`、`MaskPreview`

**用到的条目**：CLIPLoader、LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
