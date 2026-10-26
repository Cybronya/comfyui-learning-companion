---
name: unknown_workflow_inpaint_lora_sampler_21
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.806
common_nodes: [Anything Everywhere, CLIPTextEncode, CR Latent Batch Size, ConditioningZeroOut, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, ImagePadForOutpaint, ImageResize+, InpaintModelConditioning, KSampler, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, ShowText|pysssss, Text Concatenate (JPS), UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/fill+ACE++ 模特换背景_1912102639885086722.json, 图片生成/图生图/fill+ACE++ 电商换背景_1910533105982107650.json, 图片生成/图生图/fill+ACE电商服装迁移工作流_1913966897199808514.json, 图片生成/图生图/fill+ACE电商服装迁移工作流_1915320207890649089.json, 图片生成/图生图/最新fill+ACE产品换背景（融合效果超级好）_1915320224344903682.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/fill+ACE++ 模特换背景_1912102639885086722.json、图片生成/图生图/fill+ACE++ 电商换背景_1910533105982107650.json、图片生成/图生图/fill+ACE电商服装迁移工作流_1913966897199808514.json、图片生成/图生图/fill+ACE电商服装迁移工作流_1915320207890649089.json、图片生成/图生图/最新fill+ACE产品换背景（融合效果超级好）_1915320224344903682.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `ImagePadForOutpaint`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `Text Concatenate (JPS)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Overlay` —— 4/5 个有
- `LayerUtility: ColorImage V2` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有
- `FeatherMask` —— 1/5 个有
- `InspyrenetRembg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
