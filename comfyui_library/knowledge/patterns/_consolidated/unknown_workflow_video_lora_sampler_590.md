---
name: unknown_workflow_video_lora_sampler_590
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.513333
common_nodes: [AILab_Preview, BiRefNetRMBG, CLIPLoader, CLIPVisionLoader, FloatConstant, GetImageSize, GetNode, INTConstant, ImageScaleToMaxDimension, InvertMask, JWStringMultiline, LoadImage, LoadWanVideoT5TextEncoder, PreviewAny, PreviewImage, SetNode, SomethingToString, TextImageEncodeQwenVL, VHS_VideoCombine, WanVideoAddBindweaveEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageResizeToClosest, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy int, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1990334603498057730.json, 视频生成/图生视频/2028822051032666113.json, 视频生成/图生视频/2005583710823088129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_590

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1990334603498057730.json、视频生成/图生视频/2028822051032666113.json、视频生成/图生视频/2005583710823088129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_Preview`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CLIPVisionLoader`
- `FloatConstant`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageScaleToMaxDimension`
- `InvertMask`
- `JWStringMultiline`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewAny`
- `PreviewImage`
- `SetNode`
- `SomethingToString`
- `TextImageEncodeQwenVL`
- `VHS_VideoCombine`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageResizeToClosest`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Create Grid Image from Batch` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/3 个有
- `GIMMVFI_interpolate` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ImpactMinMax` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SeedVR2LoadDiTModel` —— 2/3 个有
- `SeedVR2LoadVAEModel` —— 2/3 个有
- `SeedVR2VideoUpscaler` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `string_util_StrConcat` —— 2/3 个有
- `ImageFromBatch+` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
