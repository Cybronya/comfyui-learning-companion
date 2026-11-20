---
name: unknown_workflow_controlnet_upscale_face_detailer_2
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.761667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FaceDetailerPipe, FluxGuidance, FromBasicPipe_v2, ImageScale, KSamplerSelect, LoadImage, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ToBasicPipe, ToDetailerPipe, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/TG_ART _生成人物一致性工作流_1900387590351089666.json, 图片生成/图生图/人物多角度展示｜脸部参考换脸_1935153358376214530.json, 图片生成/图生图/角色一致性+姿态控制+表情调整在线运行版_1923927944048070657.json, 图片生成/文生图/PuLID角色一致性+姿态控制+表情调整在线运行版V2.5s_1906720124529782785.json, 平台全量/NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962.json, 平台全量/角色一致性 & CONSISTENT CHARACTERS from an INPUT IMAGE_1856746778539544578.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_2

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/TG_ART _生成人物一致性工作流_1900387590351089666.json、图片生成/图生图/人物多角度展示｜脸部参考换脸_1935153358376214530.json、图片生成/图生图/角色一致性+姿态控制+表情调整在线运行版_1923927944048070657.json、图片生成/文生图/PuLID角色一致性+姿态控制+表情调整在线运行版V2.5s_1906720124529782785.json、平台全量/NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceDetailerPipe`
- `FluxGuidance`
- `FromBasicPipe_v2`
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
- `ApplyPulidFlux` —— 5/6 个有
- `PulidFluxEvaClipLoader` —— 5/6 个有
- `PulidFluxInsightFaceLoader` —— 5/6 个有
- `PulidFluxModelLoader` —— 5/6 个有
- `SetUnionControlNetType` —— 5/6 个有
- `ExpressionEditor` —— 4/6 个有
- `Fast Groups Muter (rgthree)` —— 4/6 个有
- `ImageCrop` —— 4/6 个有
- `AnyLineArtPreprocessor_aux` —— 3/6 个有
- `Anything Everywhere` —— 3/6 个有
- `CFGGuider` —— 3/6 个有
- `CoreMLDetailerHookProvider` —— 3/6 个有
- `EmptyLatentImage` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `ImageResize+` —— 3/6 个有
- `Int Literal` —— 3/6 个有
- `JoinStrings` —— 3/6 个有
- `LoraLoader` —— 3/6 个有
- `ModelPassThrough` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `Simple String` —— 3/6 个有
- `String Literal` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `GetImage_(Width&Height) _O` —— 2/6 个有
- `OpenposePreprocessor` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `Load Lora` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.63 | 0.63 - 0.66 | 6 | 98% |
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 720 | 720 - 720 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.63，观测区间 0.63 - 0.66，6 个样本，取值集中（一致性 98%）
- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
