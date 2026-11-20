---
name: unknown_workflow_inpaint_lora_sampler_23
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5474
common_nodes: [Anything Everywhere, CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetNode, ImageCrop, InpaintModelConditioning, KSampler, LayerMask: MaskPreview, LoadImage, LoraLoaderModelOnly, PreviewImage, RMBG, SaveImage, SetNode, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/学习必看  Ace++三大基础用法_1921120259213033473.json, 图片生成/图生图/指定模特极速换装   AcePlus+反推提示词+拼接参考图+Nunchaku_1920119001022660609.json, 图片生成/图生图/极速生成 产品随机模特图  Nunchaku+Fill+AcePlus_1919779970900492289.json, 图片生成/图生图/模特换装  极速生图   Fill+AcePlus+自动遮罩+Nunchaku_1919784465940283393.json, 图片生成/图生图/随机模特产品展示 AcePlus+Fill_1919735645743284225.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/学习必看  Ace++三大基础用法_1921120259213033473.json、图片生成/图生图/指定模特极速换装   AcePlus+反推提示词+拼接参考图+Nunchaku_1920119001022660609.json、图片生成/图生图/极速生成 产品随机模特图  Nunchaku+Fill+AcePlus_1919779970900492289.json、图片生成/图生图/模特换装  极速生图   Fill+AcePlus+自动遮罩+Nunchaku_1919784465940283393.json、图片生成/图生图/随机模特产品展示 AcePlus+Fill_1919735645743284225.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskPreview`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 3/5 个有
- `ImpactImageInfo` —— 3/5 个有
- `NunchakuFluxDiTLoader` —— 3/5 个有
- `LayerMask: PersonMaskUltra V2` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `easy makeImageForICLora` —— 2/5 个有
- `ACEPlusLoraProcessor` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
