---
name: image_to_image_sampler_clip_unet_87
type: Image To Image
frequency: 5
level: strong
coverage: 0.8832
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-LONGCAT图像编辑【教学】工作流_1998921046315126785.json, 图片生成/图生图/FLUX完美消除万物去&水印工作流_1948977032865226753.json, 图片生成/图生图/Flux Kontext本地图片编辑王者_1938601592583344129.json, 图片生成/图生图/Flux Kontext物体替换（输入物体名即可）_1938801690151997441.json, 图片生成/图生图/Kontext [dev] 蒙层移除物体_1938860959920541698.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_87

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX2-LONGCAT图像编辑【教学】工作流_1998921046315126785.json、图片生成/图生图/FLUX完美消除万物去&水印工作流_1948977032865226753.json、图片生成/图生图/Flux Kontext本地图片编辑王者_1938601592583344129.json、图片生成/图生图/Flux Kontext物体替换（输入物体名即可）_1938801690151997441.json、图片生成/图生图/Kontext [dev] 蒙层移除物体_1938860959920541698.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 4/5 个有
- `FluxKontextImageScale` —— 4/5 个有
- `INPAINT_MaskedFill` —— 3/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CLIPLoader` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ComparingTwoFrames_` —— 1/5 个有
- `LongCatImageEdit` —— 1/5 个有
- `LongCatImageModelLoader` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `RH_Translator` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
