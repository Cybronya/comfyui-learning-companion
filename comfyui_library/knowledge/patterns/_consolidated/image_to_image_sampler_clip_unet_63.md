---
name: image_to_image_sampler_clip_unet_63
type: Image To Image
frequency: 8
level: strong
coverage: 0.871625
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX2-LONGCAT图像编辑【教学】工作流_1998921046315126785.json, 图片生成/图生图/FLUX完美消除万物去&水印工作流_1948977032865226753.json, 图片生成/图生图/Flux Kontext本地图片编辑王者_1938601592583344129.json, 图片生成/图生图/Flux Kontext物体替换（输入物体名即可）_1938801690151997441.json, 图片生成/图生图/Kontext [dev] 蒙层移除物体_1938860959920541698.json, 平台全量/Flux Kontext物体移除_1938821071824936961.json, 平台全量/KONTEXT 【一键】万能移除物品_1948726057604718594.json, 平台全量/万物迁移Flux Kontext完美物体替换细节保留_1938915571540877314.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX2-LONGCAT图像编辑【教学】工作流_1998921046315126785.json、图片生成/图生图/FLUX完美消除万物去&水印工作流_1948977032865226753.json、图片生成/图生图/Flux Kontext本地图片编辑王者_1938601592583344129.json、图片生成/图生图/Flux Kontext物体替换（输入物体名即可）_1938801690151997441.json、图片生成/图生图/Kontext [dev] 蒙层移除物体_1938860959920541698.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
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
- `DualCLIPLoader` —— 7/8 个有
- `FluxKontextImageScale` —— 7/8 个有
- `INPAINT_MaskedFill` —— 6/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `Mask Fill Holes` —— 3/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `ComparingTwoFrames_` —— 2/8 个有
- `PrimitiveString` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `CLIPLoader` —— 1/8 个有
- `LongCatImageEdit` —— 1/8 个有
- `LongCatImageModelLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
