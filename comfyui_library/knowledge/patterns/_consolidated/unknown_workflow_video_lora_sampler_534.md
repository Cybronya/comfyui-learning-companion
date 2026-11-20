---
name: unknown_workflow_video_lora_sampler_534
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75025
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177.json, 数字人/数字人/SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665.json, 数字人/数字人/最稳定的本地部署动作迁移 表情很ok_1987421383569420290.json, 视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_534

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/SP503-动作迁移+动态运镜（wan2.2 Animate）_1970122062549426177.json、数字人/数字人/SP503-视频换人+音频同步（wan2.2 Animate）_1969349828675313665.json、数字人/数字人/最稳定的本地部署动作迁移 表情很ok_1987421383569420290.json、视频生成/文生视频/🦖Wan Animate2.2换主体_1970311265270853633.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 3/4 个有
- `DownloadAndLoadSAM2Model` —— 3/4 个有
- `DrawMaskOnImage` —— 3/4 个有
- `GrowMask` —— 3/4 个有
- `Int` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `PointsEditor` —— 3/4 个有
- `Sam2Segmentation` —— 3/4 个有
- `WanVideoEncode` —— 3/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/4 个有
- `WanVideoUni3C_embeds` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageFromBatch` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `easy convertAnything` —— 2/4 个有
- `easy positive` —— 2/4 个有
- `Bjornulf_ShowInt` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Float` —— 1/4 个有
- `ImageGetSize` —— 1/4 个有
- `ImageResize` —— 1/4 个有
- `LayerUtility: GeminiV2` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `ResizeLongestToNode` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
