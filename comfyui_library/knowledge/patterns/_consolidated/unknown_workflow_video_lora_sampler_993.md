---
name: unknown_workflow_video_lora_sampler_993
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Trigger, CheckpointLoaderSimple, ComfyMathExpression, DiffusionModelLoaderKJ, Fast Groups Bypasser (rgthree), FrameInterpolate, FrameInterpolationModelLoader, ImageFromBatch, ImageResizeKJv2, ImpactConditionalBranch, KSampler, Label (rgthree), LoadImage, Lora Loader Stack (rgthree), ModelSamplingSD3, PreviewImage, PrimitiveFloat, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SQRScail2ReferenceBatchSplit, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, WanSQRMultiReference, easy imageRemBg]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/傻瓜式操作，SCAIL2 多参考动作迁移｜人物替换，长时间不劣化_2109874432629104642.json, 平台全量/傻瓜式操作，SCAIL2 多参考动作迁移｜人物替换，长时间不劣化_2111743707342000129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_993

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/傻瓜式操作，SCAIL2 多参考动作迁移｜人物替换，长时间不劣化_2109874432629104642.json、平台全量/傻瓜式操作，SCAIL2 多参考动作迁移｜人物替换，长时间不劣化_2111743707342000129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Trigger`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `Fast Groups Bypasser (rgthree)`
- `FrameInterpolate`
- `FrameInterpolationModelLoader`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SQRScail2ReferenceBatchSplit`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `WanSQRMultiReference`
- `easy imageRemBg`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
