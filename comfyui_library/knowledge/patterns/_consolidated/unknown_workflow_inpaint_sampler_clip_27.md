---
name: unknown_workflow_inpaint_sampler_clip_27
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9754
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/局部重绘 _ OneReward_Fill_1990120170746204161.json, 图片生成/图生图/局部重绘-OneReward-CFUI版_1966417889844768769.json, 图片生成/图生图/局部重绘-字节OneReward-ComfyUI版_1966169381141123074.json, 图片生成/图生图/扩图-字节OneReward-ComfyUI版_1966171018454798338.json, 图片生成/图生图/最新OneReward-局部重绘&扩图工作流_1967045684761333761.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/局部重绘 _ OneReward_Fill_1990120170746204161.json、图片生成/图生图/局部重绘-OneReward-CFUI版_1966417889844768769.json、图片生成/图生图/局部重绘-字节OneReward-ComfyUI版_1966169381141123074.json、图片生成/图生图/扩图-字节OneReward-ComfyUI版_1966171018454798338.json、图片生成/图生图/最新OneReward-局部重绘&扩图工作流_1967045684761333761.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 4/5 个有
- `ImageAndMaskPreview` —— 3/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `MaskPreview` —— 2/5 个有
- `easy imageConcat` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RunningHub OneReward Loader` —— 1/5 个有
- `RunningHub OneReward Sampler` —— 1/5 个有
- `YC_SingleTextNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
