---
name: unknown_workflow_inpaint_sampler_vae_2
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94025
common_nodes: [AddMask, BasicGuider, BasicScheduler, DualCLIPLoader, GrowMaskWithBlur, ImageAndMaskPreview, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, KSamplerSelect, LayerUtility: ImageRemoveAlpha, LoadImage, PreviewBridge, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI人物坏手修复工作流_1926876388463382529.json, 图片生成/图生图/FLUX 30s快速一键修脚 修脸 修脚_1936960642509099010.json, 图片生成/图生图/手部修复工作流_1932087023857729538.json, 平台全量/FLUX高精度手指修复 手部美化_1910218196605988865.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_vae_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI人物坏手修复工作流_1926876388463382529.json、图片生成/图生图/FLUX 30s快速一键修脚 修脸 修脚_1936960642509099010.json、图片生成/图生图/手部修复工作流_1932087023857729538.json、平台全量/FLUX高精度手指修复 手部美化_1910218196605988865.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `AddMask`
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `KSamplerSelect`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `PreviewBridge`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CLIPTextEncodeFlux` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
