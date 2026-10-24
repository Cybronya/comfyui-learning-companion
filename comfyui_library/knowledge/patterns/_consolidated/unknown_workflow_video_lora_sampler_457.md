---
name: unknown_workflow_video_lora_sampler_457
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82575
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DisableNoise, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2局部洗图_1977364859492933633.json, 图片生成/图生图/傻瓜版视频 & 图片高清放大合并版（基于SeedVR2）_1938156714976022530.json, 图片生成/图生图/全能图片V1手动编辑产品融背景_1968675156921077761.json, 图片生成/图生图/全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_457

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Wan2.2局部洗图_1977364859492933633.json、图片生成/图生图/傻瓜版视频 & 图片高清放大合并版（基于SeedVR2）_1938156714976022530.json、图片生成/图生图/全能图片V1手动编辑产品融背景_1968675156921077761.json、图片生成/图生图/全能图片V1指哪打哪万物融图+Wan2.2洗图（手动编辑）_1966034816619679745.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `SeedVR2` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `InpaintCrop` —— 2/4 个有
- `InpaintStitch` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `RH_Nano_Banana_Image2Image` —— 2/4 个有
- `Text` —— 2/4 个有
- `DF_Get_image_size` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `VHS_VideoCombine` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `preview_mask` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
