---
name: unknown_workflow_controlnet_inpaint_lora_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6505
common_nodes: [ACN_AdvancedControlNetApply_v2, Anything Everywhere, Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, DWPreprocessor, DepthAnything_V2, DifferentialDiffusion, DownloadAndLoadDepthAnythingV2Model, FluxGuidance, Image Comparer (rgthree), InpaintCrop, InpaintModelConditioning, InpaintStitch, KSamplerSelect, Lora Loader Stack (rgthree), PreviewBridge, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VHS_LoadVideo]
problems: []
missing: []
members: [图片生成/图生图/flux+lora+controlnet【视频频首帧参考生成】_1919653119842516994.json, 图片生成/图生图/角色替换（自定义角色Lora）图片_视频首帧_1918251304102334465.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux+lora+controlnet【视频频首帧参考生成】_1919653119842516994.json、图片生成/图生图/角色替换（自定义角色Lora）图片_视频首帧_1918251304102334465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply_v2`
- `Anything Everywhere`
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DWPreprocessor`
- `DepthAnything_V2`
- `DifferentialDiffusion`
- `DownloadAndLoadDepthAnythingV2Model`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSamplerSelect`
- `Lora Loader Stack (rgthree)`
- `PreviewBridge`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `CM_NumberToInt` —— 1/2 个有
- `Image Size to Number` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.37 | - | 2 | 27% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.37，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
