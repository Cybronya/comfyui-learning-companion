---
name: unknown_workflow_video_lora_sampler_987
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.616
common_nodes: [Anything Everywhere, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, DWPreprocessor, Fast Groups Bypasser (rgthree), GetImageSizeAndCount, GetNode, ImageConcanate, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, ImpactConditionalBranch, Int, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PainterVRAM, PoseAndFaceDetection, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy compare]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/wan-Animate动作迁移_2037413866488995841.json, 视频生成/图生视频/wan123首针重绘动作迁移_2047166439689297922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_987

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/wan-Animate动作迁移_2037413866488995841.json、视频生成/图生视频/wan123首针重绘动作迁移_2047166439689297922.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PainterVRAM`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy compare`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.97 | - | 2 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.97，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
