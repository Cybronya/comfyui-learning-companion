---
name: unknown_workflow_inpaint_clip_unet_8
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.925333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, LoadImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模特人物一键换装工作流_1944302344660193282.json, 平台全量/Production of Non Person IP Dataset_1864962757723639809.json, 平台全量/电商模特换装工作流-精简版-mazh_1996115638399746049.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/模特人物一键换装工作流_1944302344660193282.json、平台全量/Production of Non Person IP Dataset_1864962757723639809.json、平台全量/电商模特换装工作流-精简版-mazh_1996115638399746049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `LoadImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImageToMask` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 30 | 3 | 0% |
| 采样算法 | 1 | - | 3 | 33% |
| 调度器 | euler | - | 3 | 33% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 30，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 1，3 个样本，一致性 33%
- 调度器 最常用 euler，3 个样本，一致性 33%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
