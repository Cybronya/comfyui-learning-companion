---
name: unknown_workflow_controlnet_video_upscale
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.579
common_nodes: [Bjornulf_FreeVRAM, Bjornulf_ShowInt, CLIPLoader, CLIPVisionLoader, ConditioningZeroOut, DrawMaskOnImage, DrawViTPose, Fast Groups Muter (rgthree), GetNode, INTConstant, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImageScale, ImageUpscaleWithModelBatched, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, RIFE VFI, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, TT_img_enc, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2064594523124232193.json, 视频生成/图生视频/2065167482889007106.json, 视频生成/图生视频/2063232908294451201.json, 视频生成/图生视频/2053105004701069313.json, 视频生成/图生视频/2066760634758426626.json, 视频生成/图生视频/2068050463907471361.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_upscale

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2064594523124232193.json、视频生成/图生视频/2065167482889007106.json、视频生成/图生视频/2063232908294451201.json、视频生成/图生视频/2053105004701069313.json、视频生成/图生视频/2066760634758426626.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
- `Bjornulf_FreeVRAM`
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageUpscaleWithModelBatched`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `RIFE VFI`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `TT_img_enc`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
