---
name: unknown_workflow_lora_sampler_clip_258
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.913
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/智能模特洗图——提示词反推图生图_1975481867791151105.json, 图片生成/文生图/FLux(nunchaku )基础洗图工作流_1911779747029024769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_258

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/智能模特洗图——提示词反推图生图_1975481867791151105.json、图片生成/文生图/FLux(nunchaku )基础洗图工作流_1911779747029024769.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `JjkShowText` —— 1/2 个有
- `Joy_caption` —— 1/2 个有
- `Joy_caption_load` —— 1/2 个有
- `Joy_caption_two_advanced` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `Joy_extra_options` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1460 | - | 2 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1460，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
