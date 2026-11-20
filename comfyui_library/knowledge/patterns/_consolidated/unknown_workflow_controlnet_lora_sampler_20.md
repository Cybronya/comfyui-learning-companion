---
name: unknown_workflow_controlnet_lora_sampler_20
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9075
common_nodes: [ApplyInstantID, Automatic CFG, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LoadImage, LoraLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键生成人物二次元贴纸_1914522619549548545.json, 图片生成/图生图/只属于你的即时贴纸_1898612595497357313.json, 平台全量/Memoji_1849806645667786754.json, 平台全量/Stickers you ByRui_1834556474726182914.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键生成人物二次元贴纸_1914522619549548545.json、图片生成/图生图/只属于你的即时贴纸_1898612595497357313.json、平台全量/Memoji_1849806645667786754.json、平台全量/Stickers you ByRui_1834556474726182914.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantID`
- `Automatic CFG`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler (Efficient)`
- `LoadImage`
- `LoraLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `BRIA_RMBG_ModelLoader_Zho` —— 3/4 个有
- `BRIA_RMBG_Zho` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `AutoCropFaces` —— 1/4 个有
- `HighRes-Fix Script` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1016 | 1016 - 1016 | 4 | 100% |
| 高度 | 1016 | 1016 - 1016 | 4 | 100% |
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 4 | 3 - 4 | 4 | 88% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 75% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 4 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1016，观测区间 1016 - 1016，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1016，观测区间 1016 - 1016，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 3 - 4，4 个样本，取值集中（一致性 88%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
