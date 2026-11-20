---
name: unknown_workflow_controlnet_inpaint_sampler_10
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.816667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, DualCLIPLoader, GrowMaskWithBlur, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncodeForInpaint, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX模特重绘万物换装_1906304125804400642.json, 图片生成/图生图/最强局部重绘！丰胸+修手+擦除+图生图=艾橘溪_1887034807447113730.json, 平台全量/Flux加载ControlNet换背景写实电商摄影_1973201384512335873.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_10

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX模特重绘万物换装_1906304125804400642.json、图片生成/图生图/最强局部重绘！丰胸+修手+擦除+图生图=艾橘溪_1887034807447113730.json、平台全量/Flux加载ControlNet换背景写实电商摄影_1973201384512335873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `FaceDetailer` —— 1/3 个有
- `LayerMask: MaskInvert` —— 1/3 个有
- `LayerMask: RmBgUltra V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `SAMLoader` —— 1/3 个有
- `UltralyticsDetectorProvider` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
