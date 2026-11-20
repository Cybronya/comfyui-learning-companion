---
name: unknown_workflow_controlnet_lora_sampler_29
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [ApplyInstantID, Automatic CFG, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, ImageScaleToTotalPixels, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LoadImage, LoraLoader, SaveImage, Text Concatenate]
problems: []
missing: []
members: [图片生成/图生图/一键生成人物二次元贴纸_1914522619549548545.json, 图片生成/图生图/只属于你的即时贴纸_1898612595497357313.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键生成人物二次元贴纸_1914522619549548545.json、图片生成/图生图/只属于你的即时贴纸_1898612595497357313.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `Automatic CFG`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler (Efficient)`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `Text Concatenate`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1016 | - | 2 | 100% |
| 高度 | 1016 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1016，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1016，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
