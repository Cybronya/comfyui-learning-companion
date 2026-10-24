---
name: image_to_image_sampler_clip_vae_14
type: Image To Image
frequency: 13
level: strong
coverage: 0.942692
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/kontext-gguf版单图编辑（真人转3D，真人转动漫，动漫转真人）_1989474249289158658.json, 图片生成/图生图/kontext单图工作流_1944956155041075201.json, 图片生成/图生图/kontext单图工作流_1971121957414543362.json, 图片生成/图生图/kontext单图转绘-免费-速度快-效果好_1963527482023694337.json, 图片生成/图生图/kontext去水印_1958369496044093441.json, 图片生成/图生图/kontext图片编辑_1943613174111498242.json, 图片生成/图生图/kontext（dev）开源官方版本_1938409745747476482.json, 图片生成/图生图/kontext（dev）开源官方版本（双图）_1938414703502884866.json, 图片生成/图生图/numchaku10倍Flux Kontext多模态一句话改图（单图模式）_1938409164169220098.json, 图片生成/图生图/图像编辑（单图）_1938449619573473282.json, 图片生成/图生图/图像编辑（单图）_2039936993047617537.json, 图片生成/图生图/🦖Flux Kontext Dev一句话修图（单图）_1938427261941121025.json, 图片生成/文生图/Kontext 单图-万能改图_1940687352694206465.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/kontext-gguf版单图编辑（真人转3D，真人转动漫，动漫转真人）_1989474249289158658.json、图片生成/图生图/kontext单图工作流_1944956155041075201.json、图片生成/图生图/kontext单图工作流_1971121957414543362.json、图片生成/图生图/kontext单图转绘-免费-速度快-效果好_1963527482023694337.json、图片生成/图生图/kontext去水印_1958369496044093441.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 12/13 个有
- `UNETLoader` —— 12/13 个有
- `VAELoader` —— 12/13 个有
- `FluxKontextImageScale` —— 10/13 个有
- `RH_Translator` —— 7/13 个有
- `Text Multiline` —— 7/13 个有
- `ImageStitch` —— 6/13 个有
- `ImageConcatMulti` —— 5/13 个有
- `ShowText|pysssss` —— 5/13 个有
- `UnetLoaderGGUF` —— 3/13 个有
- `AV_VAELoader` —— 1/13 个有
- `DualCLIPLoaderGGUF` —— 1/13 个有
- `GoogleTranslateTextNode` —— 1/13 个有
- `ImageScaleToTotalPixels` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `NunchakuFluxDiTLoader` —— 1/13 个有
- `PMRF` —— 1/13 个有
- `workflow>UpSpeed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
