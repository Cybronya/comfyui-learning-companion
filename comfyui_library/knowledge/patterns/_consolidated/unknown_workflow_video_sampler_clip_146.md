---
name: unknown_workflow_video_sampler_clip_146
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.986
common_nodes: [AppendImageBatch, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, DrawMaskOnImage, Fast Bypasser (rgthree), ImageBatchMulti, ImageFromBatch+, ImagePadForOutpaint, ImageResizeKJv2, ImpactImageInfo, ImpactInt, KOOK_SaveJPGImage, KSamplerAdvanced, LayerFilter: MotionBlur, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, RIFE VFI, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_DuplicateImages, VHS_VideoCombine, WanFirstLastFrameToVideo, easy anythingIndexSwitch, easy forLoopEnd, easy forLoopStart, easy imageSplitGrid, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/电商带货视频万能版自适应识别类目一键成片工作流 V1.0_2058485731072499714.json, 视频生成/图生视频/电商抖音男装带货 千川暗水印解决_2040348727809937409.json, 视频生成/图生视频/电商抖音男装带货 千川暗水印解决_2049873691374305281.json, 视频生成/图生视频/男装带货万能版自适应识别类目一键成片_2039970357578305537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/电商带货视频万能版自适应识别类目一键成片工作流 V1.0_2058485731072499714.json、视频生成/图生视频/电商抖音男装带货 千川暗水印解决_2040348727809937409.json、视频生成/图生视频/电商抖音男装带货 千川暗水印解决_2049873691374305281.json、视频生成/图生视频/男装带货万能版自适应识别类目一键成片_2039970357578305537.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Image2Image` —— 3/4 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
