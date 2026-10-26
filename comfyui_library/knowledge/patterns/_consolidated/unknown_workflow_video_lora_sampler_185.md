---
name: unknown_workflow_video_lora_sampler_185
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.606545
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, InvertMask, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoAddBindweaveEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/03-18-01-WAN2.1-BindWeave单图参考图生视频_1996052544822657026.json, 视频生成/图生视频/03-18-02-WAN2.1-BindWeave-融合多图生成高一致性视频_1996106049994309634.json, 视频生成/图生视频/BindWeave_multi_image_1995416893911707650.json, 视频生成/图生视频/BindWeave_single_image_1993600135810711553.json, 视频生成/图生视频/BindWeave_多图生视频_2029026172620775426.json, 视频生成/图生视频/BindWeave三图参考图生视频V1(FPS24)_1989700619843891202.json, 视频生成/图生视频/图生视频 BindWeave 三图编辑【人+产品+背景组合】_2029575255773159425.json, 视频生成/图生视频/图生视频 BindWeave 三图编辑【人+人+背景组合】_2030497637895507970.json, 视频生成/图生视频/图生视频5.1 BindWeave 视频双图编辑_1990080887029157890.json, 视频生成/图生视频/图生视频5.2 BindWeave 三图编辑【人+产品+背景组合】_1990227277147459585.json, 视频生成/图生视频/图生视频5.3 BindWeave 三图编辑【人+人+背景组合】_1990257275820535809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_185

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/03-18-01-WAN2.1-BindWeave单图参考图生视频_1996052544822657026.json、视频生成/图生视频/03-18-02-WAN2.1-BindWeave-融合多图生成高一致性视频_1996106049994309634.json、视频生成/图生视频/BindWeave_multi_image_1995416893911707650.json、视频生成/图生视频/BindWeave_single_image_1993600135810711553.json、视频生成/图生视频/BindWeave_多图生视频_2029026172620775426.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `InvertMask`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `TextImageEncodeQwenVL` —— 10/11 个有
- `ImageBatchMulti` —— 9/11 个有
- `MaskBatchMulti` —— 9/11 个有
- `WanVideoSetLoRAs` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `MaskPreview+` —— 7/11 个有
- `SolidMask` —— 7/11 个有
- `easy imageRemBg` —— 7/11 个有
- `ImageConcatMulti` —— 6/11 个有
- `JWInteger` —— 6/11 个有
- `INTConstant` —— 5/11 个有
- `JjkText` —— 5/11 个有
- `Primitive integer [Crystools]` —— 5/11 个有
- `SimpleMath+` —— 5/11 个有
- `WanVideoTorchCompileSettings` —— 5/11 个有
- `easy cleanGpuUsed` —— 5/11 个有
- `MaskPreview` —— 4/11 个有
- `RMBG` —— 4/11 个有
- `CR Prompt Text` —— 3/11 个有
- `ImageConcanate` —— 3/11 个有
- `ImagePadForOutpaint` —— 2/11 个有
- `DrawMaskOnImage` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `FloatConstant` —— 1/11 个有
- `GetImageSizeAndCount` —— 1/11 个有
- `LayerUtility: ImageBlendAdvance` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
