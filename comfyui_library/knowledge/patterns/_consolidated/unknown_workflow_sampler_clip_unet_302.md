---
name: unknown_workflow_sampler_clip_unet_302
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.764
common_nodes: [CLIPTextEncode, ColorMatch, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImpactSwitch, KSampler, LoadAndResizeImage, PreviewImage, Primitive integer [Crystools], RH_Captioner, RH_Translator, ReferenceLatent, SaveImage, ShowText|pysssss, TTP_text_mix, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext-dev-溶图-打光-扩图_1939259159177248769.json, 图片生成/图生图/kontext-dev-溶图-打光-扩图_1949707668918804482.json, 图片生成/图生图/kontext本地版-溶图-打光-自动版_2095333006037831682.json, 图片生成/图生图/kontext本地版-溶图-打光-自动版_2095455623986106370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_302

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontext-dev-溶图-打光-扩图_1939259159177248769.json、图片生成/图生图/kontext-dev-溶图-打光-扩图_1949707668918804482.json、图片生成/图生图/kontext本地版-溶图-打光-自动版_2095333006037831682.json、图片生成/图生图/kontext本地版-溶图-打光-自动版_2095455623986106370.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImpactSwitch`
- `KSampler`
- `LoadAndResizeImage`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_text_mix`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `Int` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
