---
name: unknown_workflow_sampler_clip_unet_373
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.769
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/节点系列06-Text Random Multiline节点多条随机提示词_2029173085181583362.json, 图片生成/图生图/课程演示——室内设计（全屋）-终版_2075575000530247681.json, 图片生成/文生图/8G 显卡专属｜Flux2 Klein4B 文生图加洗图 43 秒极速生成_2054786195737071617.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_373

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/节点系列06-Text Random Multiline节点多条随机提示词_2029173085181583362.json、图片生成/图生图/课程演示——室内设计（全屋）-终版_2075575000530247681.json、图片生成/文生图/8G 显卡专属｜Flux2 Klein4B 文生图加洗图 43 秒极速生成_2054786195737071617.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `TextRandomMultiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.4 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
