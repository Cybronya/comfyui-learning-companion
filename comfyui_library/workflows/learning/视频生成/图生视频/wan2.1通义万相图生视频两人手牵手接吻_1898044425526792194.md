---
key: 视频生成/图生视频/wan2.1通义万相图生视频两人手牵手接吻_1898044425526792194.json
name: wan2.1通义万相图生视频两人手牵手接吻_1898044425526792194.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1898044425526792194.json
hash: 302e776532e82618
coverage: 0.933333
learned_at: 2026-10-15 22:29:19
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, ImagePadForOutpaint, MaskToImage, MaskToImage, ImageToMask, LayerUtility: LaMa, WanVideoImageClipEncode, WanVideoBlockSwap, Int, WanVideoEnhanceAVideo, LoadImage, FaceBoundingBox, FaceAnalysisModels, FaceBoundingBox, easy imageConcat, PreviewImage, ImageConcanate, PreviewImage, LoadImage, TextInput_, WanVideoSampler, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1通义万相图生视频两人手牵手接吻_1898044425526792194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1898044425526792194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（30 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `ImagePadForOutpaint`
- `MaskToImage`
- `MaskToImage`
- `ImageToMask`
- `LayerUtility: LaMa`
- `WanVideoImageClipEncode`
- `WanVideoBlockSwap`
- `Int`
- `WanVideoEnhanceAVideo`
- `LoadImage`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `easy imageConcat`
- `PreviewImage`
- `ImageConcanate`
- `PreviewImage`
- `LoadImage`
- `TextInput_`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ImagePadForOutpaint`、`MaskToImage`、`ImageToMask`、`LayerUtility: LaMa`、`WanVideoImageClipEncode`、`WanVideoBlockSwap`、`Int`、`WanVideoEnhanceAVideo`、`LoadImage`、`FaceBoundingBox`、`FaceAnalysisModels`、`easy imageConcat`、`ImageConcanate`、`TextInput_`、`WanVideoSampler`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
