---
key: 视频生成/文生视频/WAN2.2-AllInOne控制+参考_2072999603861233664.json
name: WAN2.2-AllInOne控制+参考_2072999603861233664
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne控制+参考_2072999603861233664.json
hash: c69ed71078952a24
coverage: 1
learned_at: 2026-10-11 20:38:42
nodes: [WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, VHS_LoadVideo, AIO_Preprocessor, INTConstant, WanVideoVACEEncode, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, ImageResizeKJv2, WanVideoSetLoRAs, WanVideoLoraSelect, INTConstant, LoadImage, WanVideoTextEncode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.2-AllInOne控制+参考_2072999603861233664.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne控制+参考_2072999603861233664.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（20 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `AIO_Preprocessor`
- `INTConstant`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `INTConstant`
- `LoadImage`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（20/20）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`AIO_Preprocessor`、`INTConstant`、`WanVideoVACEEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
