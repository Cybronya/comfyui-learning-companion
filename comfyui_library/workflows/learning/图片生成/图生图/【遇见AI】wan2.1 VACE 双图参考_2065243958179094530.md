---
key: 图片生成/图生图/【遇见AI】wan2.1 VACE 双图参考_2065243958179094530.json
name: 【遇见AI】wan2.1 VACE 双图参考_2065243958179094530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 VACE 双图参考_2065243958179094530.json
hash: 0a83dc0cb296a726
coverage: 0.882353
learned_at: 2026-10-23 11:52:25
nodes: [WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, WanVideoBlockSwap, LoadImage, MarkdownNote, LoadImage, LayerMask: RmBgUltra V2, ImageScale, PreviewImage, easy makeImageForICLora, LoadImage, LoadImage, LoadImage, MaskPreview+, InvertMask, LoadImage, ImageResizeKJv2, PreviewImage, WanVideoVACEEncode, PreviewImage, Image Overlay, WanVideoLoraSelect, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoVACEModelSelect, WanVideoModelLoader]
patterns: []
missing: []
---

# 图片生成/图生图/【遇见AI】wan2.1 VACE 双图参考_2065243958179094530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】wan2.1 VACE 双图参考_2065243958179094530.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LayerMask: RmBgUltra V2`
- `ImageScale`
- `PreviewImage`
- `easy makeImageForICLora`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MaskPreview+`
- `InvertMask`
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `WanVideoVACEEncode`
- `PreviewImage`
- `Image Overlay`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **88%**（30/34）

**有卡**：`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`LoadImage`、`LayerMask: RmBgUltra V2`、`ImageScale`、`easy makeImageForICLora`、`MaskPreview+`、`InvertMask`、`ImageResizeKJv2`、`WanVideoVACEEncode`、`Image Overlay`、`WanVideoLoraSelect`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
