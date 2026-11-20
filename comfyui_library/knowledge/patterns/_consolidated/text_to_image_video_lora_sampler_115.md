---
name: text_to_image_video_lora_sampler_115
type: Text To Image
frequency: 6
level: strong
coverage: 0.562167
common_nodes: [Any Switch (rgthree), BatchCount+, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageAndMaskPreview, ImageFromBatch, ImageResizeKJv2, ImpactConditionalBranch, InvertMask, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ModelPreviewOverrideKJ, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, PrimitiveBoolean, RepeatImageBatch, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, Seed (rgthree), SetNode, SimpleMath+, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy imageRemBg, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Scail-2 动作迁移角色替换｜v1版本一键套用参考动作_2097526220098465793.json, 图片生成/图生图/Scail-2动作迁移v1版｜视频角色一键替换保持动作神态｜AI换人神器_2099098215567155201.json, 图片生成/图生图/Scail-2动作迁移复刻工作流｜多图参考角色替换视频生成_2097394963263868930.json, 图片生成/图生图/Scail-2动作迁移角色替换 多图参考上下文支持_2098816230126870529.json, 图片生成/图生图/Scail-2动作迁移角色替换图生视频处理生成工具_2102155199908507650.json, 图片生成/图生图/动作迁移角色替换｜Scail-2 v1视频生成直出_2090930164845862914.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_115

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Scail-2 动作迁移角色替换｜v1版本一键套用参考动作_2097526220098465793.json、图片生成/图生图/Scail-2动作迁移v1版｜视频角色一键替换保持动作神态｜AI换人神器_2099098215567155201.json、图片生成/图生图/Scail-2动作迁移复刻工作流｜多图参考角色替换视频生成_2097394963263868930.json、图片生成/图生图/Scail-2动作迁移角色替换 多图参考上下文支持_2098816230126870529.json、图片生成/图生图/Scail-2动作迁移角色替换图生视频处理生成工具_2102155199908507650.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BatchCount+`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageAndMaskPreview`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `InvertMask`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPreviewOverrideKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveBoolean`
- `RepeatImageBatch`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `Seed (rgthree)`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy imageRemBg`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
