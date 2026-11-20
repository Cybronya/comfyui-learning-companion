---
name: unknown_workflow_sampler_clip_unet_442
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.774
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyFlux2LatentImage, KSamplerSelect, PreviewAny, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SkipLayerGuidanceDiTSimple, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Moss｜生图及编辑_2116603170561548290.json, 图片生成/文生图/moss-image-sft_2115982256526413826.json, 平台全量/moss-image-sft｜极致的开源图像大模型！_2117883592650084353.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_442

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Moss｜生图及编辑_2116603170561548290.json、图片生成/文生图/moss-image-sft_2115982256526413826.json、平台全量/moss-image-sft｜极致的开源图像大模型！_2117883592650084353.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/3 个有
- `Ideogram4PromptBuilderKJ` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MOSSImageControl` —— 1/3 个有
- `TextEncodeMOSSImageEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
