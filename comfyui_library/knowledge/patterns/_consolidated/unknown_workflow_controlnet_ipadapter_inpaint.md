---
name: unknown_workflow_controlnet_ipadapter_inpaint
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8114
common_nodes: [AIO_Preprocessor, BlendInpaint, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, CutForInpaint, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, SetUnionControlNetType, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物一键消除_1925146308896878593.json, 图片生成/图生图/万物涂抹一键消除_1988867755061424130.json, 图片生成/图生图/啊癫 电商万物去水印、文字、消除工作流_1914279574824517634.json, 平台全量/万物消除_1909791576560758785.json, 平台全量/万物消除_2003032677026525186.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/万物一键消除_1925146308896878593.json、图片生成/图生图/万物涂抹一键消除_1988867755061424130.json、图片生成/图生图/啊癫 电商万物去水印、文字、消除工作流_1914279574824517634.json、平台全量/万物消除_1909791576560758785.json、平台全量/万物消除_2003032677026525186.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `BlendInpaint`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `CutForInpaint`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LoadImageMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 5 | 100% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 5 | 100% |
| 采样算法 | dpmpp_sde | - | 5 | 100% |
| 调度器 | karras | - | 5 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，5 个样本，一致性 100%
- 调度器 最常用 karras，5 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
