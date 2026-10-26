---
name: unknown_workflow_inpaint_lora_sampler_16
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.929
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, InpaintModelConditioning, KSamplerSelect, LoadImage, LoraLoader, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】ACE++ local editing 重绘_2049429912020328450.json, 图片生成/图生图/【遇见AI】ACE++ logo标志印刷_2049436152981098497.json, 图片生成/图生图/【遇见AI】ACE++ logo标志展示_2049436131527233537.json, 图片生成/图生图/【遇见AI】ACE++换脸，Fill，Redux_2049433784042393602.json, 图片生成/图生图/【遇见AI】ACE++，Fill，Redux，面部参考_2049431631588495361.json, 图片生成/图生图/【遇见AI】ACE++，Full，Redux，万物迁移，模特换装换衣服_2049438626995507202.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【遇见AI】ACE++ local editing 重绘_2049429912020328450.json、图片生成/图生图/【遇见AI】ACE++ logo标志印刷_2049436152981098497.json、图片生成/图生图/【遇见AI】ACE++ logo标志展示_2049436131527233537.json、图片生成/图生图/【遇见AI】ACE++换脸，Fill，Redux_2049433784042393602.json、图片生成/图生图/【遇见AI】ACE++，Fill，Redux，面部参考_2049431631588495361.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 5/6 个有
- `MaskPreview+` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `ReduxAdvanced` —— 5/6 个有
- `StyleModelLoader` —— 5/6 个有
- `easy makeImageForICLora` —— 5/6 个有
- `EmptyImage` —— 2/6 个有
- `GetImageSizeAndCount` —— 2/6 个有
- `easy humanSegmentation` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
