---
name: unknown_workflow_upscale_sampler_clip_29
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.494143
common_nodes: [CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner, CheckpointLoaderSimple, DF_Integer, DF_Text_Box, EmptyLatentImage, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [平台全量/发电厂创意海报_1806285393967951874.json, 平台全量/古典插画女神_1808779892321398785.json, 平台全量/地标艺术立体剪纸_1805490718921678849.json, 平台全量/山水亭阁_1804046969835872258.json, 平台全量/抽象现代艺术风格_1793954979199856642.json, 平台全量/服装水彩效果图_1810219725522710530.json, 平台全量/杂志封面摄影_1804066068926291970.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/发电厂创意海报_1806285393967951874.json、平台全量/古典插画女神_1808779892321398785.json、平台全量/地标艺术立体剪纸_1805490718921678849.json、平台全量/山水亭阁_1804046969835872258.json、平台全量/抽象现代艺术风格_1793954979199856642.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncodeSDXL`
- `CLIPTextEncodeSDXLRefiner`
- `CheckpointLoaderSimple`
- `DF_Integer`
- `DF_Text_Box`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/7 个有
- `Image Overlay` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `RH_Prompter` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `TextCombinerTwo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 45 | 6 - 45 | 7 | 65% |
| 采样算法 | 6.5 | 6.5 - 6.5 | 6 | 100% |
| 调度器 | dpmpp_3m_sde_gpu | - | 7 | 86% |
| 重绘幅度 | karras | - | 7 | 86% |
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 45，观测区间 6 - 45，7 个样本
- 采样算法 中位数 6.5，观测区间 6.5 - 6.5，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_3m_sde_gpu，7 个样本，一致性 86%
- 重绘幅度 最常用 karras，7 个样本，一致性 86%
- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 45，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
