---
name: unknown_workflow_ipadapter_sampler_vae
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9195
common_nodes: [AlignYourStepsScheduler, Automatic CFG, CR Text, ConcatText_Zho, DisplayText_Zho, IPAdapterStyleComposition, IPAdapterUnifiedLoader, ImageScaleToMegapixels, KSamplerSelect, LoadImage, SamplerCustom, SaveImage, VAEDecode, VAELoader, easy comfyLoader, easy pipeOut]
problems: []
missing: []
members: [平台全量/卡通人像生成器_Cartoon Portrait_1839269086571495426.json, 平台全量/灵魂画手 _ Cartoon Portrait_1864939246162497538.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_sampler_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/卡通人像生成器_Cartoon Portrait_1839269086571495426.json、平台全量/灵魂画手 _ Cartoon Portrait_1864939246162497538.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AlignYourStepsScheduler`
- `Automatic CFG`
- `CR Text`
- `ConcatText_Zho`
- `DisplayText_Zho`
- `IPAdapterStyleComposition`
- `IPAdapterUnifiedLoader`
- `ImageScaleToMegapixels`
- `KSamplerSelect`
- `LoadImage`
- `SamplerCustom`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy comfyLoader`
- `easy pipeOut`

**可变部分**（部分 workflow 才有）：
- `MiniCPM_VQA_Polished` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
