---
name: unknown_workflow_sampler_clip_unet_124
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.878444
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext去掉字幕水印_1971848085930504193.json, 图片生成/图生图/Kontext用嘴改图开源模型双图编辑_1938370989979799554.json, 图片生成/图生图/flux_kontext_1991048121285320705.json, 图片生成/图生图/flux_kontext_双图融合_1950736481751093249.json, 图片生成/图生图/【老金驿站】Kontext清除图像模糊高清工作流_1947912385995649026.json, 图片生成/图生图/【老金驿站】满血Kontext中文输入单图工作流_1939313503348113410.json, 图片生成/图生图/【老金驿站】满血Kontext中文输入双图工作流_1939316636765831170.json, 图片生成/图生图/最强开源大模型 FLUX_1938439204835627009.json, 图片生成/文生图/Flux_kontext_基础工作流_1942411562571214849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Kontext去掉字幕水印_1971848085930504193.json、图片生成/图生图/Kontext用嘴改图开源模型双图编辑_1938370989979799554.json、图片生成/图生图/flux_kontext_1991048121285320705.json、图片生成/图生图/flux_kontext_双图融合_1950736481751093249.json、图片生成/图生图/【老金驿站】Kontext清除图像模糊高清工作流_1947912385995649026.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 8/9 个有
- `FluxKontextImageScale` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `ModelSamplingFlux` —— 8/9 个有
- `ImageScaleBy` —— 5/9 个有
- `ChinesePrompt_Mix` —— 2/9 个有
- `ImageStitch` —— 2/9 个有
- `LoraLoader` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `RH_Translator` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `AILab_LoadImage` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `Int` —— 1/9 个有
- `PathchSageAttentionKJ` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
