---
key: 视频生成/图生视频/Wan2.1 AccVideo vace 双图参考快速模型_1948689505176956929.json
name: Wan2.1 AccVideo vace 双图参考快速模型_1948689505176956929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 AccVideo vace 双图参考快速模型_1948689505176956929.json
hash: f1a3f45dbe7ae0ad
coverage: 0.90625
learned_at: 2026-10-15 22:30:48
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, Note Plus (mtb), Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, PrimitiveFloat, Primitive integer [Crystools], ImageScale, ImageResizeKJ, WanVideoTextEncode, RMBG, ImageResize+, RMBG, ImageCompositeMasked, PreviewImage, WanVideoVACEEncode, WanVideoSampler, WanVideoDecode, ColorMatch, ImageConcanate, VHS_VideoCombine, LoadImageFromUrl, LoadImage, LoadImage, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 AccVideo vace 双图参考快速模型_1948689505176956929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948689505176956929.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（32 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note Plus (mtb)`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `PrimitiveFloat`
- `Primitive integer [Crystools]`
- `ImageScale`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `RMBG`
- `ImageResize+`
- `RMBG`
- `ImageCompositeMasked`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ColorMatch`
- `ImageConcanate`
- `VHS_VideoCombine`
- `LoadImageFromUrl`
- `LoadImage`
- `LoadImage`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Note`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Note Plus (mtb)`、`Primitive integer [Crystools]`、`Text Multiline`、`ImageScale`、`ImageResizeKJ`、`WanVideoTextEncode`、`RMBG`、`ImageResize+`、`ImageCompositeMasked`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoDecode`、`ColorMatch`、`ImageConcanate`、`VHS_VideoCombine`、`LoadImageFromUrl`、`LoadImage`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
