---
name: unknown_workflow_inpaint_sampler_clip_60
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.96975
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, Kontext Inpainting Conditioning, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-inpaint局部重绘_1942857168016052226.json, 平台全量/Y-kontext_inpaint_workflow_1943974335478632449.json, 平台全量/kontext 精准局部标贴设计v1_1957765878588829697.json, 平台全量/kontext 精准局部重绘 指哪打哪 精准定位_1946764876717154306.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext-inpaint局部重绘_1942857168016052226.json、平台全量/Y-kontext_inpaint_workflow_1943974335478632449.json、平台全量/kontext 精准局部标贴设计v1_1957765878588829697.json、平台全量/kontext 精准局部重绘 指哪打哪 精准定位_1946764876717154306.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `Kontext Inpainting Conditioning`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 3/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `MaskBlur+` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `LayerColor: Brightness & Contrast` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.98 - 1 | 4 | 99% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.98 - 1，4 个样本，取值集中（一致性 99%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.98，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
