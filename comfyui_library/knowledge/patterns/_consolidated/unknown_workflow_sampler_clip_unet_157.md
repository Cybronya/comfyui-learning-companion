---
name: unknown_workflow_sampler_clip_unet_157
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86875
common_nodes: [BasicScheduler, CFGOverride, CLIPLoader, CLIPTextEncode, DualModelGuider, EmptyFlux2LatentImage, ExtendIntermediateSigmas, Ideogram4PromptBuilderKJ, KSamplerSelect, ModelSamplingAuraFlow, PreviewAny, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SigmasPreview, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4 人像Lora测试流_2073324611147751426.json, 图片生成/文生图/Ideogram4 可视化提示词编辑+14步高质量加速流_2073324002667483137.json, 图片生成/文生图/Ideogram4 多人物Lora测试流_2073325009149456386.json, 图片生成/文生图/Ideogram_V4_FP8 边界框精准定义++文生图 工作流_2064688948349333505.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Ideogram4 人像Lora测试流_2073324611147751426.json、图片生成/文生图/Ideogram4 可视化提示词编辑+14步高质量加速流_2073324002667483137.json、图片生成/文生图/Ideogram4 多人物Lora测试流_2073325009149456386.json、图片生成/文生图/Ideogram_V4_FP8 边界框精准定义++文生图 工作流_2064688948349333505.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `ExtendIntermediateSigmas`
- `Ideogram4PromptBuilderKJ`
- `KSamplerSelect`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SigmasPreview`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `Epsilon Scaling` —— 3/4 个有
- `ImpactSwitch` —— 3/4 个有
- `LyingSigmaSampler` —— 3/4 个有
- `MuyeImageBlendingMode` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `ScheduledCFGGuidance` —— 3/4 个有
- `easy float` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
