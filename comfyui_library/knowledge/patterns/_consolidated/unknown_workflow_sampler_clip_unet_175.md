---
name: unknown_workflow_sampler_clip_unet_175
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.941286
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, DualCLIPLoader, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, InFluxModelSamplingPred, Joy_caption_two, Joy_caption_two_load, LoadImage, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/6月最新-宠物油画风转绘 细节一致性超高 FLUX逆采样_1937540216741892097.json, 图片生成/图生图/Flux逆采样_在线生图_1896893612884664322.json, 图片生成/图生图/人物宠物油画风格化转换，细节一致性高，FLUX_2016511200237981698.json, 图片生成/图生图/内衣精修工作流_2018139651474722818.json, 图片生成/图生图/宠物油画风转绘+细节一致性超高+FLUX逆采样_2028654614836420609.json, 图片生成/图生图/最新-宠物油画风转绘 细节一致性超高 FLUX逆采样_2026123070141898753.json, 图片生成/图生图/油画·人物宠物风景风格化转换，细节一致性高，FLUX_2016517105818013697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_175

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/6月最新-宠物油画风转绘 细节一致性超高 FLUX逆采样_1937540216741892097.json、图片生成/图生图/Flux逆采样_在线生图_1896893612884664322.json、图片生成/图生图/人物宠物油画风格化转换，细节一致性高，FLUX_2016511200237981698.json、图片生成/图生图/内衣精修工作流_2018139651474722818.json、图片生成/图生图/宠物油画风转绘+细节一致性超高+FLUX逆采样_2028654614836420609.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `InFluxModelSamplingPred`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `LoadImage`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `LoraLoader` —— 6/7 个有
- `ColorMatch` —— 5/7 个有
- `ConcatText_Zho` —— 5/7 个有
- `GetImageSize+` —— 5/7 个有
- `ImageScale` —— 5/7 个有
- `ImpactInt` —— 5/7 个有
- `Float` —— 1/7 个有
- `Get Image Size` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 1/7 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 6 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，6 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
