---
name: unknown_workflow_video_upscale_lora_22
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.77
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DrawViTPose, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSizeAndCount, GetNode, ImageFromBatch, ImageFromBatch+, ImageResize+, ImageResizeKJv2, ImageUpscaleWithModelBatched, KSampler, KepStringLiteral, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PixelPerfectResolution, PoseAndFaceDetection, RHHiddenNodes, RIFE VFI, SetNode, SimpleMath+, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimateToVideo, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUniAnimatePoseInput, WanVideoVAELoader, easy int, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/跳舞动作迁移+表情复刻 跳舞动作模仿_2056620090044534785.json, 视频生成/图生视频/跳舞动作迁移+表情复刻 跳舞动作模仿_2106004931005210625.json, 视频生成/图生视频/跳舞动作迁移+表情复刻 跳舞动作模仿_2106010414332080129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/跳舞动作迁移+表情复刻 跳舞动作模仿_2056620090044534785.json、视频生成/图生视频/跳舞动作迁移+表情复刻 跳舞动作模仿_2106004931005210625.json、视频生成/图生视频/跳舞动作迁移+表情复刻 跳舞动作模仿_2106010414332080129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawViTPose`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageUpscaleWithModelBatched`
- `KSampler`
- `KepStringLiteral`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `RHHiddenNodes`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimateToVideo`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUniAnimatePoseInput`
- `WanVideoVAELoader`
- `easy int`
- `easy showAnything`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 3 | 3 - 3 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | linear_quadratic | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 3，观测区间 3 - 3，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
