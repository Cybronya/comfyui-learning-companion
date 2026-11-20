---
name: image_to_image_sampler_clip_unet_42
type: Image To Image
frequency: 11
level: strong
coverage: 0.942273
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/千府AI建筑鸟瞰图一键工作流_1962384837388668930.json, 图片生成/图生图/最强真实老照片修复_1947226707453497346.json, 图片生成/图生图/老照片修复2.0版本，一键修复，可搭配去除AI感工作流使用_2027976944700104706.json, 图片生成/图生图/老照片修复，一键修复_2029503656806064129.json, 平台全量/Kontext一键卸妆反美颜_2009453940424839169.json, 平台全量/Kontext万物消除简易使用版_1953830790683611138.json, 平台全量/Kontext老照片修复_1929897844097060865.json, 平台全量/kontext一键卸妆_1949536036652752898.json, 平台全量/【真实还原老照片】Kontext老照片修复 保持一致性 老照片上色_1973907222155669505.json, 平台全量/真实人物照片转3D动漫风格_1948327719957344257.json, 平台全量/老旧底片修复为高清照片_1944447156797493249.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_42

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/千府AI建筑鸟瞰图一键工作流_1962384837388668930.json、图片生成/图生图/最强真实老照片修复_1947226707453497346.json、图片生成/图生图/老照片修复2.0版本，一键修复，可搭配去除AI感工作流使用_2027976944700104706.json、图片生成/图生图/老照片修复，一键修复_2029503656806064129.json、平台全量/Kontext一键卸妆反美颜_2009453940424839169.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 10/11 个有
- `LoraLoaderModelOnly` —— 10/11 个有
- `RH_Translator` —— 10/11 个有
- `CR Text` —— 9/11 个有
- `FilmGrain` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `LayerColor: Brightness & Contrast` —— 6/11 个有
- `Image Comparer (rgthree)` —— 3/11 个有
- `ShowText|pysssss` —— 2/11 个有
- `DF_Image_scale_by_ratio` —— 1/11 个有
- `ImageInvert` —— 1/11 个有
- `KontextArchPresetMain` —— 1/11 个有
- `NunchakuFluxDiTLoader` —— 1/11 个有
- `NunchakuTextEncoderLoaderV2` —— 1/11 个有
- `PrimitiveFloat` —— 1/11 个有
- `Text` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 11 | 100% |
| Prompt 约束强度(CFG) | 0.8 | 0.8 - 1 | 11 | 89% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 0.95 | 0.5 - 1 | 11 | 85% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.8，观测区间 0.8 - 1，11 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 0.95，观测区间 0.5 - 1，11 个样本，取值集中（一致性 85%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
