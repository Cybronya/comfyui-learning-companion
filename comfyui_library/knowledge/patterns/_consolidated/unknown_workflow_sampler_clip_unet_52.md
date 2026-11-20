---
name: unknown_workflow_sampler_clip_unet_52
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.785647
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX 3 Image Klein 文生图_2120031107382071298.json, 平台全量/Moss-image Sft文生图_自动词优化版_2117525839586873345.json, 平台全量/Moss-image Sft文生图_自动词优化版_2117900748280393729.json, 平台全量/Moss-image Sft文生图_自动词优化版_2117904157385519105.json, 平台全量/Moss-image Sft文生图_自动词优化版_2117905542550216706.json, 平台全量/Moss-image Sft文生图_自动词优化版_2117907451457658881.json, 平台全量/Moss-image Sft文生图_自动词优化版_2118260696638119937.json, 平台全量/Moss-image Sft文生图_自动词优化版_2118263481702109185.json, 平台全量/Moss-image Sft文生图_自动词优化版_2119055314258583554.json, 平台全量/Moss-image_Sft文生图_自动词优化版_2117781182636183553.json, 平台全量/Moss_文生图高质量版_2119249577248382977.json, 平台全量/Moss_文生图高质量版_2119609749120573441.json, 平台全量/image_moss_image_t2i（道具）API V20261020_2117318099631427585.json, 平台全量/moss_image_t2i_scene_v20261020_2117283368663609346.json, 平台全量/moss_image_t2i【四视图】API V20261020_2117320813128011777.json, 平台全量/moss超写实模型_2120185855489957890.json, 数字人/数字人/MOSS sft Comfyui官方工作流文生图_2112066748353695746.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/FLUX 3 Image Klein 文生图_2120031107382071298.json、平台全量/Moss-image Sft文生图_自动词优化版_2117525839586873345.json、平台全量/Moss-image Sft文生图_自动词优化版_2117900748280393729.json、平台全量/Moss-image Sft文生图_自动词优化版_2117904157385519105.json、平台全量/Moss-image Sft文生图_自动词优化版_2117905542550216706.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 16/17 个有
- `PreviewAny` —— 15/17 个有
- `SkipLayerGuidanceDiTSimple` —— 7/17 个有
- `ComfySwitchNode` —— 4/17 个有
- `CR Prompt Text` —— 3/17 个有
- `MOSSMergePreset` —— 3/17 个有
- `ConcatTextOfUtils` —— 2/17 个有
- `ModelSamplingFlux` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 16 - 50 | 17 | 63% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 17 | 83% |
| 采样算法 | er_sde | - | 17 | 76% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 16 - 50，17 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，17 个样本，取值集中（一致性 83%）
- 采样算法 最常用 er_sde，17 个样本，一致性 76%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
