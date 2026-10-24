---
name: image_to_image_sampler_clip_unet_19
type: Image To Image
frequency: 11
level: strong
coverage: 0.870455
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/200斤以上大胖子_1958383043901865986.json, 图片生成/图生图/Flux Kontext Dev双图编辑模式_1941124111307587586.json, 图片生成/图生图/Flux Kontext开源官方流（说话改图）_1938956279115403266.json, 图片生成/图生图/Flux Kontext物体替换（输入物体名即可）_1938801690151997441.json, 图片生成/图生图/Kontext-光影重绘-溶图_1956516186076971010.json, 图片生成/图生图/Kontext高级暗感INS风格_1956315870576431105.json, 图片生成/图生图/kontext一键变胖_1954137979562422273.json, 图片生成/图生图/kontext一键转超写实插画风格_1954500675407364098.json, 图片生成/图生图/kontext线条水彩风格_1957038775403515905.json, 图片生成/图生图/kontext美妆产品精修_1957064408419721218.json, 图片生成/图生图/kontext转彩铅风格_1957036567203123201.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/200斤以上大胖子_1958383043901865986.json、图片生成/图生图/Flux Kontext Dev双图编辑模式_1941124111307587586.json、图片生成/图生图/Flux Kontext开源官方流（说话改图）_1938956279115403266.json、图片生成/图生图/Flux Kontext物体替换（输入物体名即可）_1938801690151997441.json、图片生成/图生图/Kontext-光影重绘-溶图_1956516186076971010.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 10/11 个有
- `ImageScale` —— 9/11 个有
- `PreviewImage` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `CR Text` —— 8/11 个有
- `GetImageSize` —— 8/11 个有
- `Image Comparer (rgthree)` —— 8/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `Primitive float [Crystools]` —— 8/11 个有
- `FastCanvas` —— 1/11 个有
- `FastCanvasTool` —— 1/11 个有
- `INPAINT_MaskedFill` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `LayerMask: RmBgUltra V2` —— 1/11 个有
- `Mask Fill Holes` —— 1/11 个有
- `PrimitiveString` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
