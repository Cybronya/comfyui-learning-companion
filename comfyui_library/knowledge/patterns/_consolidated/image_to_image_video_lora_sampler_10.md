---
name: image_to_image_video_lora_sampler_10
type: Image To Image
frequency: 3
level: strong
coverage: 0.879667
common_nodes: [AILab_ColorInput, CFGNorm, CLIPLoader, CreateCFGScheduleFloatList, CutAndDragOnPath, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, ImageToMask, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask To Image (mtb), ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PreviewImage, RMBG, RunningHub Deepcleaner, SplineEditor, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoAddTTMLatents, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1991323289348059137.json, 视频生成/图生视频/1991106081629798401.json, 视频生成/图生视频/1990629553938849794.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1991323289348059137.json、视频生成/图生视频/1991106081629798401.json、视频生成/图生视频/1990629553938849794.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_ColorInput`
- `CFGNorm`
- `CLIPLoader`
- `CreateCFGScheduleFloatList`
- `CutAndDragOnPath`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageToMask`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask To Image (mtb)`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `RMBG`
- `RunningHub Deepcleaner`
- `SplineEditor`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoAddTTMLatents`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
