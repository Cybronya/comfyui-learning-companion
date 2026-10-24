---
name: unknown_workflow_controlnet_upscale_face_detailer
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.700833
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, CoreMLDetailerHookProvider, DualCLIPLoader, EmptySD3LatentImage, ExpressionEditor, FaceDetailerPipe, FluxGuidance, FromBasicPipe_v2, ImageCrop, ImageScale, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ToBasicPipe, ToDetailerPipe, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX人物多角度风格一致性+放大修复_1906958724634906625.json, 图片生成/文生图/Flux lora训练（AI视频保持人物一致性）_1922307103535595521.json, 图片生成/文生图/Flux版一键生成角色Lora训练集-Fast_1915383673414156289.json, 图片生成/文生图/Flux版一键生成角色Lora训练集_1912845983032537089.json, 图片生成/文生图/动漫角色LORA_2012500101402464258.json, 图片生成/文生图/动漫角色LORA（一键19图）_2067168189636759553.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/FLUX人物多角度风格一致性+放大修复_1906958724634906625.json、图片生成/文生图/Flux lora训练（AI视频保持人物一致性）_1922307103535595521.json、图片生成/文生图/Flux版一键生成角色Lora训练集-Fast_1915383673414156289.json、图片生成/文生图/Flux版一键生成角色Lora训练集_1912845983032537089.json、图片生成/文生图/动漫角色LORA_2012500101402464258.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `CoreMLDetailerHookProvider`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `ExpressionEditor`
- `FaceDetailerPipe`
- `FluxGuidance`
- `FromBasicPipe_v2`
- `ImageCrop`
- `ImageScale`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ToBasicPipe`
- `ToDetailerPipe`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Simple String` —— 5/6 个有
- `Fast Groups Muter (rgthree)` —— 4/6 个有
- `Anything Everywhere?` —— 3/6 个有
- `ETN_CropImage` —— 3/6 个有
- `ImageBatchMulti` —— 3/6 个有
- `RemBGSession+` —— 3/6 个有
- `Seed Everywhere` —— 3/6 个有
- `easy imageChooser` —— 3/6 个有
- `Image Blank` —— 2/6 个有
- `Image Paste Crop by Location` —— 2/6 个有
- `ImageCrop+` —— 2/6 个有
- `ImagePadForOutpaint` —— 2/6 个有
- `ImageRemoveBackground+` —— 2/6 个有
- `ImageResizeKJ` —— 2/6 个有
- `Images to RGB` —— 2/6 个有
- `ImpactImageBatchToImageList` —— 2/6 个有
- `CR Load LoRA` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.66 | 0.66 - 0.69 | 6 | 98% |
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.66，观测区间 0.66 - 0.69，6 个样本，取值集中（一致性 98%）
