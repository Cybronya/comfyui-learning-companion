---
name: unknown_workflow_controlnet_sampler_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9235
common_nodes: [AIO_Preprocessor, Control Net Stacker, ControlNetLoader, Efficient Loader, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/图生图线稿控制游乐场风格_1933746290524082178.json, 图片生成/文生图/canny+depth+双Lora-字体风格转换_1928336738488598530.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图生图线稿控制游乐场风格_1933746290524082178.json、图片生成/文生图/canny+depth+双Lora-字体风格转换_1928336738488598530.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Control Net Stacker`
- `ControlNetLoader`
- `Efficient Loader`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AutoNegativePrompt` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `HighRes-Fix Script` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy loraStack` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6.75 | - | 2 | 96% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 50% |
| 调度器 | exponential | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.75，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 50%
- 调度器 最常用 exponential，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
