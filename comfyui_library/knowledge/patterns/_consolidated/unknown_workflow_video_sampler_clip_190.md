---
name: unknown_workflow_video_sampler_clip_190
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.986
common_nodes: [AppendImageBatch, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, DrawMaskOnImage, Fast Bypasser (rgthree), ImageBatchMulti, ImageFromBatch+, ImagePadForOutpaint, ImageResizeKJv2, ImpactImageInfo, ImpactInt, KOOK_SaveJPGImage, KSamplerAdvanced, LayerFilter: MotionBlur, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, RH_Nano_Banana2_Image2Image, RIFE VFI, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_DuplicateImages, VHS_VideoCombine, WanFirstLastFrameToVideo, easy anythingIndexSwitch, easy forLoopEnd, easy forLoopStart, easy imageSplitGrid, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2040348727809937409.json, 视频生成/图生视频/2049873691374305281.json, 视频生成/图生视频/2039970357578305537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2040348727809937409.json、视频生成/图生视频/2049873691374305281.json、视频生成/图生视频/2039970357578305537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `AppendImageBatch`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DrawMaskOnImage`
- `Fast Bypasser (rgthree)`
- `ImageBatchMulti`
- `ImageFromBatch+`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImpactImageInfo`
- `ImpactInt`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `LayerFilter: MotionBlur`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RH_Nano_Banana2_Image2Image`
- `RIFE VFI`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `easy anythingIndexSwitch`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageSplitGrid`
- `wanBlockSwap`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
