---
name: unknown_workflow_video_lora_sampler_410
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8948
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1994305244540715009.json, 视频生成/图生视频/1964201625864818690.json, 视频生成/图生视频/1964640487892242434.json, 视频生成/图生视频/1963945783164850177.json, 视频生成/图生视频/1993311574968434690.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_410

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1994305244540715009.json、视频生成/图生视频/1964201625864818690.json、视频生成/图生视频/1964640487892242434.json、视频生成/图生视频/1963945783164850177.json、视频生成/图生视频/1993311574968434690.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `WanVideoEnhanceAVideo` —— 3/5 个有
- `WanVideoSLG` —— 3/5 个有
- `easy positive` —— 3/5 个有
- `AILab_ImageStitch` —— 2/5 个有
- `GetImageSizeAndCount` —— 2/5 个有
- `ImageFromBatch+` —— 2/5 个有
- `RMBG` —— 2/5 个有
- `Label (rgthree)` —— 1/5 个有
- `RH_Nano_Banana2_Image2Image` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `easy humanSegmentation` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
