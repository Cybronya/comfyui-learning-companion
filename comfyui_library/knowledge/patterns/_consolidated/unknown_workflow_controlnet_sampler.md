---
name: unknown_workflow_controlnet_sampler
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.920571
common_nodes: [AIO_Preprocessor, Control Net Stacker, ControlNetLoader, Eff. Loader SDXL, KSampler SDXL (Eff.), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/SDXL3D+阿尔贝・格莱兹风格加速_1933788680001904641.json, 图片生成/图生图/SDXL图生图3D风格加速_1933770260917215234.json, 图片生成/图生图/SDXL图生图主宰者风格_1933760355674054657.json, 图片生成/图生图/SDXL图生图主宰者风格加速_1933767347314282497.json, 图片生成/图生图/SDXL图生图阿尔贝・格莱兹风格加速_1933784974070079489.json, 图片生成/图生图/SDXL模拟电影+艾德里安・布什加速_1934107099591041026.json, 图片生成/图生图/高保真 3D _ 照片级写实主义_1934115670101811201.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SDXL3D+阿尔贝・格莱兹风格加速_1933788680001904641.json、图片生成/图生图/SDXL图生图3D风格加速_1933770260917215234.json、图片生成/图生图/SDXL图生图主宰者风格_1933760355674054657.json、图片生成/图生图/SDXL图生图主宰者风格加速_1933767347314282497.json、图片生成/图生图/SDXL图生图阿尔贝・格莱兹风格加速_1933784974070079489.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `Control Net Stacker`
- `ControlNetLoader`
- `Eff. Loader SDXL`
- `KSampler SDXL (Eff.)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `easy loraStack` —— 6/7 个有
- `ArtistsImage_Zho` —— 4/7 个有
- `SDXLPromptStyler` —— 4/7 个有
- `StringFunction|pysssss` —— 4/7 个有
- `OneButtonPreset` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 7 | 30% |
| Prompt 约束强度(CFG) | 1.2 | 1 - 8 | 7 | 6% |
| 采样算法 | euler_ancestral | - | 7 | 57% |
| 调度器 | sgm_uniform | - | 7 | 71% |
| 重绘幅度 | 0 | 0 - 0 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，7 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1 - 8，7 个样本，取值分散，一致性仅 6%
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 57%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 71%
- 重绘幅度 中位数 0，观测区间 0 - 0，7 个样本，取值集中（一致性 100%）
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
