---
name: unknown_workflow_sampler_clip_unet_354
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.864333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/写实风格图生图_1905140867475378177.json, 图片生成/文生图/FLUX SRPO 文生图 _ Joy 3 反推文生图，腾讯开源新模型！真实性和美学质量提高超3倍！_1966878604049125377.json, 图片生成/文生图/WaveSpeed FLUX工作流加速神器_1879120968877830146.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_354

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/写实风格图生图_1905140867475378177.json、图片生成/文生图/FLUX SRPO 文生图 _ Joy 3 反推文生图，腾讯开源新模型！真实性和美学质量提高超3倍！_1966878604049125377.json、图片生成/文生图/WaveSpeed FLUX工作流加速神器_1879120968877830146.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `EnhancedCompileModel` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `Lora Loader Stack (rgthree)` —— 1/3 个有
- `String Literal` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
