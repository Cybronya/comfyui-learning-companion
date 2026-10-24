---
name: image_to_image_sampler_clip_vae_12
type: Image To Image
frequency: 14
level: strong
coverage: 0.738143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext绘图-官方工作流（自用）_1938979258507124738.json, 图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939407471486353410.json, 图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939605911574913025.json, 图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_2033743444149014530.json, 图片生成/图生图/flux kontext dev编辑模型开源版本官方示例工作流_1938411062246969346.json, 图片生成/图生图/flux kontext 超强图像编辑模型_1938518653468106753.json, 图片生成/图生图/flux kontext双图模式_1938527528707358722.json, 图片生成/图生图/flux_1_kontext_dev_basic工作流(通过中文改变局部属性)_1938495711467995137.json, 图片生成/图生图/flux_1_kontex终于等来了，模型基础效果_1938275066096582657.json, 图片生成/图生图/flux_kontext_dev_单图-提示词更听话_1938613725001605122.json, 图片生成/图生图/kontext参考蒙版涂抹消除增加元素_1940288167415300097.json, 图片生成/图生图/一切都改变了！Kontext Comfyui官方工作流，想干啥干啥_1938325635456761858.json, 图片生成/图生图/一键动漫化_2046111426502201345.json, 图片生成/图生图/想干啥干啥，一切都改变了！Kontext Comfyui官方工作流_2020760788851494913.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_12

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Kontext绘图-官方工作流（自用）_1938979258507124738.json、图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939407471486353410.json、图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_1939605911574913025.json、图片生成/图生图/Nunchaku Kontext官方工作流 10秒采样_2033743444149014530.json、图片生成/图生图/flux kontext dev编辑模型开源版本官方示例工作流_1938411062246969346.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 12/14 个有
- `EmptySD3LatentImage` —— 11/14 个有
- `LoadImageOutput` —— 11/14 个有
- `UNETLoader` —— 11/14 个有
- `ImageResizeKJv2` —— 5/14 个有
- `RH_Translator` —— 5/14 个有
- `DeepTranslatorTextNode` —— 4/14 个有
- `NunchakuFluxDiTLoader` —— 4/14 个有
- `easy imageRemBg` —— 4/14 个有
- `Bjornulf_ShowStringText` —— 1/14 个有
- `ChinesePrompt_Mix` —— 1/14 个有
- `Color` —— 1/14 个有
- `InvertMask` —— 1/14 个有
- `JjkText` —— 1/14 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 14 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，14 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
