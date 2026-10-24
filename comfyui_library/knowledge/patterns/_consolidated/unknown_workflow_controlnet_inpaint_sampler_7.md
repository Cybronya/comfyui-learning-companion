---
name: unknown_workflow_controlnet_inpaint_sampler_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.863
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, GrowMaskWithBlur, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncodeForInpaint, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX模特重绘万物换装_1906304125804400642.json, 图片生成/图生图/最强局部重绘！丰胸+修手+擦除+图生图=艾橘溪_1887034807447113730.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX模特重绘万物换装_1906304125804400642.json、图片生成/图生图/最强局部重绘！丰胸+修手+擦除+图生图=艾橘溪_1887034807447113730.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeForInpaint`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FaceDetailer` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
