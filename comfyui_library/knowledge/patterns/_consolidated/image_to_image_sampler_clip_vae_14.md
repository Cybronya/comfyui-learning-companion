---
name: image_to_image_sampler_clip_vae_14
type: Image To Image
frequency: 15
level: strong
coverage: 0.755267
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext图片去水印_2050191399424933890.json, 图片生成/图生图/Kontext开源版双图融合工作流_1941885913607913473.json, 图片生成/图生图/Kontext绘图-官方工作流（自用）_1938979258507124738.json, 图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939407471486353410.json, 图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939605911574913025.json, 图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_2033743444149014530.json, 图片生成/图生图/flux kontext dev编辑模型开源版本官方示例工作流_1938411062246969346.json, 图片生成/图生图/flux_1_kontext（5连拍生成图片）_1938980661526978561.json, 图片生成/图生图/kontext+nunchaku极速版工作流_1939455859959242754.json, 图片生成/图生图/kontext官方工作流[教学]_1999020387990130690.json, 图片生成/图生图/nunchaku-flux.1-kontext-dev_1939389707900076034.json, 图片生成/图生图/nunchaku加速-flux.1-kontext图片融合修改工作流【好奇漫步】_1970129650544484353.json, 图片生成/图生图/一切都改变了！Kontext Comfyui官方工作流，想干啥干啥_1938325635456761858.json, 图片生成/图生图/一键动漫化_2046111426502201345.json, 图片生成/图生图/想干啥干啥，一切都改变了！Kontext Comfyui官方工作流_2020760788851494913.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Kontext图片去水印_2050191399424933890.json、图片生成/图生图/Kontext开源版双图融合工作流_1941885913607913473.json、图片生成/图生图/Kontext绘图-官方工作流（自用）_1938979258507124738.json、图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939407471486353410.json、图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939605911574913025.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 14/15 个有
- `PreviewImage` —— 14/15 个有
- `SaveImage` —— 14/15 个有
- `EmptySD3LatentImage` —— 12/15 个有
- `LoadImageOutput` —— 11/15 个有
- `UNETLoader` —— 9/15 个有
- `NunchakuFluxDiTLoader` —— 6/15 个有
- `DeepTranslatorTextNode` —— 5/15 个有
- `ImageResizeKJv2` —— 4/15 个有
- `easy imageRemBg` —— 4/15 个有
- `LoraLoaderModelOnly` —— 2/15 个有
- `RH_Translator` —— 2/15 个有
- `Bjornulf_ShowStringText` —— 1/15 个有
- `CompressImages` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 15 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
