---
name: unknown_workflow_inpaint_lora_sampler_69
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.900667
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize_, ImageCrop, ImageResize+, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltra, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, MaskPreview+, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [平台全量/FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313.json, 平台全量/【电商换装】万能换装，可以长袖换成吊带裙_1915368657071833089.json, 平台全量/最新ACE++  Redux 万物迁移 AI模特换装 UP 楚门的AI世界)_1890014204382916609.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/FLUX+fill+ACE电商产品换装2.0FLUX+fill+ACE换装1_1931224249976205313.json、平台全量/【电商换装】万能换装，可以长袖换成吊带裙_1915368657071833089.json、平台全量/最新ACE++  Redux 万物迁移 AI模特换装 UP 楚门的AI世界)_1890014204382916609.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize_`
- `ImageCrop`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: BiRefNetUltra`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `PreviewBridge` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 25 - 28 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 25 - 28，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
