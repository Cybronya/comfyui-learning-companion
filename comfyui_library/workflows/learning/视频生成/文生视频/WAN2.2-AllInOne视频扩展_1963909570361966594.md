---
key: 视频生成/文生视频/WAN2.2-AllInOne视频扩展_1963909570361966594.json
name: WAN2.2-AllInOne视频扩展_1963909570361966594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne视频扩展_1963909570361966594.json
hash: 06a3547543adcf80
coverage: 0.909091
learned_at: 2026-10-10 23:06:00
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoDecode, GetImageSize+, VHS_VideoCombine, VHS_VideoCombine, String Literal, ImagePadKJ, GrowMaskWithBlur, WanVideoVACEEncode, MaskToImage, ImageResizeKJ, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoTextEncode, VHS_LoadVideo, WanVideoBlockSwap, WanVideoModelLoader, VHS_VideoCombine]
patterns: []
missing: [String Literal, GetImageSize+]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/WAN2.2-AllInOne视频扩展_1963909570361966594.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne视频扩展_1963909570361966594.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（22 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `GetImageSize+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `String Literal`
- `ImagePadKJ`
- `GrowMaskWithBlur`
- `WanVideoVACEEncode`
- `MaskToImage`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`ImagePadKJ`、`GrowMaskWithBlur`、`WanVideoVACEEncode`、`MaskToImage`、`ImageResizeKJ`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`WanVideoModelLoader`

**缺卡**（2）：`String Literal`、`GetImageSize+`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
