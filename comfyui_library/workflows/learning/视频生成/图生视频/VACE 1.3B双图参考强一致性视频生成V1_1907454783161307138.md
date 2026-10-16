---
key: 视频生成/图生视频/VACE 1.3B双图参考强一致性视频生成V1_1907454783161307138.json
name: VACE 1.3B双图参考强一致性视频生成V1_1907454783161307138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1907454783161307138.json
hash: dcec0b6abc1f22ec
coverage: 0.710526
learned_at: 2026-10-15 22:29:27
nodes: [LoadWanVideoT5TextEncoder, WanVideoTeaCache, WanVideoVAELoader, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, LayerMask: LoadBiRefNetModelV2, TTP_Expand_And_Mask, ImageConcatMulti, ImageConcatMulti, WanVideoDecode, LoadImage, LayerMask: BiRefNetUltraV2, LoadImage, WanVideoVACEEncode, JWImageResizeByLongerSide, PreviewImage, ImageConcanate, JWInteger, JWInteger, JWInteger, PreviewImage, WanVideoTextEncode, PrimitiveNode, Note Plus (mtb), WanVideoModelLoader, WanVideoBlockSwap, VHS_VideoCombine, VHS_VideoCombine, Note, Note, Note, Note, Note, WanVideoSampler, PrimitiveNode, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/VACE 1.3B双图参考强一致性视频生成V1_1907454783161307138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1907454783161307138.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoTeaCache`
- `WanVideoVAELoader`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `LayerMask: LoadBiRefNetModelV2`
- `TTP_Expand_And_Mask`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoDecode`
- `LoadImage`
- `LayerMask: BiRefNetUltraV2`
- `LoadImage`
- `WanVideoVACEEncode`
- `JWImageResizeByLongerSide`
- `PreviewImage`
- `ImageConcanate`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `PreviewImage`
- `WanVideoTextEncode`
- `PrimitiveNode`
- `Note Plus (mtb)`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `Note`
- `Note`

## 知识

覆盖率 **71%**（27/38）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTeaCache`、`WanVideoVAELoader`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`LayerMask: LoadBiRefNetModelV2`、`TTP_Expand_And_Mask`、`ImageConcatMulti`、`WanVideoDecode`、`LoadImage`、`LayerMask: BiRefNetUltraV2`、`WanVideoVACEEncode`、`JWImageResizeByLongerSide`、`ImageConcanate`、`JWInteger`、`WanVideoTextEncode`、`Note Plus (mtb)`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、JWImageResizeByLongerSide
