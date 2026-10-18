---
key: 视频生成/图生视频/Unianimate Dit+Gpeno人物一致性跳舞+姿势动画加速版V2换脸加速（MPS奖励）_1913792299430572033.json
name: Unianimate Dit+Gpeno人物一致性跳舞+姿势动画加速版V2换脸加速（MPS奖励）_1913792299430572033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Unianimate Dit+Gpeno人物一致性跳舞+姿势动画加速版V2换脸加速（MPS奖励）_1913792299430572033.json
hash: 49b9623df1e8faa8
coverage: 0.98
learned_at: 2026-10-15 22:29:34
nodes: [JWInteger, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, ImageConcanate, ImageConcanate, ImageConcanate, VHS_VideoCombine, VHS_VideoCombine, WanVideoTeaCache, WanVideoBlockSwap, WanVideoDecode, LayerUtility: PurgeVRAM V2, WanVideoTextEncode, CR Prompt Text, VHS_LoadVideo, Load RetinaFace, JWInteger, Crop Face, ImageResizeKJ, WanVideoUniAnimateDWPoseDetector, WanVideoSampler, WanVideoExperimentalArgs, PreviewImage, VHS_VideoCombine, LoadImage, VHS_VideoCombine, ImageListToImageBatch, LoadImage, ImageConcanate, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoUniAnimatePoseInput, ImageResizeKJ, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, ImpactImageBatchToImageList, ImpactImageBatchToImageList, VHS_VideoCombine, ImageConcanate, JWImageResizeByLongerSide, JWImageResizeByLongerSide, Note Plus (mtb), JWInteger, ReActorFaceSwap, GPENO Face Restoration]
patterns: []
missing: []
---

# 视频生成/图生视频/Unianimate Dit+Gpeno人物一致性跳舞+姿势动画加速版V2换脸加速（MPS奖励）_1913792299430572033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1913792299430572033.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `JWInteger`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `Load RetinaFace`
- `JWInteger`
- `Crop Face`
- `ImageResizeKJ`
- `WanVideoUniAnimateDWPoseDetector`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageListToImageBatch`
- `LoadImage`
- `ImageConcanate`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoUniAnimatePoseInput`
- `ImageResizeKJ`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImpactImageBatchToImageList`
- `ImpactImageBatchToImageList`
- `VHS_VideoCombine`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `JWImageResizeByLongerSide`
- `Note Plus (mtb)`
- `JWInteger`
- `ReActorFaceSwap`
- `GPENO Face Restoration`

## 知识

覆盖率 **98%**（49/50）

**有卡**：`JWInteger`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`ImageConcanate`、`VHS_VideoCombine`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncode`、`CR Prompt Text`、`VHS_LoadVideo`、`Load RetinaFace`、`Crop Face`、`ImageResizeKJ`、`WanVideoUniAnimateDWPoseDetector`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`LoadImage`、`ImageListToImageBatch`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`WanVideoUniAnimatePoseInput`、`WanVideoLoraSelect`、`ImpactImageBatchToImageList`、`JWImageResizeByLongerSide`、`Note Plus (mtb)`、`ReActorFaceSwap`、`GPENO Face Restoration`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
