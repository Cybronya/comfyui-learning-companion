---
key: 视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json
name: WAN2.2-AllInOne控制+参考_1963899111291572225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json
hash: f82f0fa900c85044
coverage: 1
learned_at: 2026-10-10 23:05:57
nodes: [WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, VHS_LoadVideo, AIO_Preprocessor, INTConstant, WanVideoVACEEncode, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, ImageResizeKJv2, WanVideoSetLoRAs, WanVideoLoraSelect, INTConstant, LoadImage, WanVideoTextEncode, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json`

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
