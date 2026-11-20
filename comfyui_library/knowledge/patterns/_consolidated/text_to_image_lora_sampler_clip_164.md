---
name: text_to_image_lora_sampler_clip_164
type: Text To Image
frequency: 10
level: strong
coverage: 0.82
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/MOSS文生图全节点注释版 反推提示词图生图处理工具_2112993127761006593.json, 图片生成/反推提示词/MOSS文生图全节点注释版｜附反推提示词新手照抄就能跑_2112927305474596865.json, 图片生成/图生图/G image2.5全能系列模型｜单张成本低至7分钱_2098728369797025793.json, 图片生成/图生图/Moss简洁文生图流程，图生图搭配玩法不设限_2112692396340375554.json, 图片生成/文生图/MOSS_BBOX边界框精准布局文生图工作流｜海报排版随心控_2114234330708013057.json, 图片生成/文生图/MOSS文生图基础工作流，简洁易上手快速生成高质量图片素材_2114468798932799490.json, 图片生成/文生图/MOSS文生图基础工作流，简洁易上手快速生成高质量图片素材_2117091241753137154.json, 图片生成/文生图/Moss Image SFT turbo加速文生图 海报字体生成工具_2113736101109264385.json, 图片生成/文生图/Moss Image布局控制工作流 元素位置精准海报工具_2114136772199403521.json, 图片生成/文生图/Moss Image布局控制工作流｜文生图海报制作元素位置精准可控_2113884746953609218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/MOSS文生图全节点注释版 反推提示词图生图处理工具_2112993127761006593.json、图片生成/反推提示词/MOSS文生图全节点注释版｜附反推提示词新手照抄就能跑_2112927305474596865.json、图片生成/图生图/G image2.5全能系列模型｜单张成本低至7分钱_2098728369797025793.json、图片生成/图生图/Moss简洁文生图流程，图生图搭配玩法不设限_2112692396340375554.json、图片生成/文生图/MOSS_BBOX边界框精准布局文生图工作流｜海报排版随心控_2114234330708013057.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SkipLayerGuidanceDiTSimple` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `EmptyFlux2LatentImage` —— 7/10 个有
- `PreviewAny` —— 7/10 个有
- `ResolutionSelector` —— 7/10 个有
- `ComfySwitchNode` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `TextGenerate` —— 6/10 个有
- `CreateBoundingBoxes` —— 4/10 个有
- `MOSSImageLayoutPrompt` —— 4/10 个有
- `PrimitiveBoolean` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `SpectrumMOSSImageAdaptive` —— 2/10 个有
- `VOSR2ModelLoader` —— 2/10 个有
- `VOSR2Upscale` —— 2/10 个有
- `LLGPTImage25Generator` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
