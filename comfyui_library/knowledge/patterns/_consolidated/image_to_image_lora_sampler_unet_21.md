---
name: image_to_image_lora_sampler_unet_21
type: Image To Image
frequency: 16
level: weak
coverage: 0.652937
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2D转3D丨风格转换丨插画、照片一键转换_1980952858050908162.json, 图片生成/图生图/3-千问edit2511-场景修改_2038605809730461697.json, 图片生成/图生图/34.tonnie-Qwen edit物品迁移工作流_2003212052573429762.json, 图片生成/图生图/Ban_Qwen-动漫转写实真人V2版_1988231591057121281.json, 图片生成/图生图/Ban_Qwen-艺术摄影图片重打光_1988243660754042882.json, 图片生成/图生图/NGS风格转bjd融光_2082671756535492609.json, 图片生成/图生图/NGS风格转bjd融光_2085195450470191106.json, 图片生成/图生图/Qwen 2511 史上最强-动漫转写实真人正式版_2013133142546194434.json, 图片生成/图生图/Qwen-动漫转写实真人_1987456609242779650.json, 图片生成/图生图/Qwen2511-真人转动漫_2014909381707567105.json, 图片生成/图生图/【AI】产品设计及模特上身（学员练习工作流）_2026934710932348930.json, 图片生成/图生图/【AI】图像编辑控制工作流(学员练习)_2011360098072928257.json, 图片生成/图生图/【AI】图像编辑控制工作流)_2085901700283592705.json, 图片生成/图生图/【AI】图像编辑控制工作流)_2085923884175548418.json, 图片生成/图生图/一键证件照生成_2086806567952932866.json, 图片生成/图生图/课程案例演示——图像编辑控制工作流教学_2074004701275840514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/2D转3D丨风格转换丨插画、照片一键转换_1980952858050908162.json、图片生成/图生图/3-千问edit2511-场景修改_2038605809730461697.json、图片生成/图生图/34.tonnie-Qwen edit物品迁移工作流_2003212052573429762.json、图片生成/图生图/Ban_Qwen-动漫转写实真人V2版_1988231591057121281.json、图片生成/图生图/Ban_Qwen-艺术摄影图片重打光_1988243660754042882.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEdit` —— 15/16 个有
- `TextEncodeQwenImageEditPlus` —— 14/16 个有
- `GetNode` —— 13/16 个有
- `SetNode` —— 13/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/16 个有
- `FluxKontextMultiReferenceLatentMethod` —— 10/16 个有
- `Int` —— 7/16 个有
- `PreviewImage` —— 6/16 个有
- `Seed (rgthree)` —— 6/16 个有
- `TextInput_` —— 6/16 个有
- `Image Comparer (rgthree)` —— 5/16 个有
- `ImageConcanate` —— 5/16 个有
- `AIO_Preprocessor` —— 4/16 个有
- `ImageScaleToTotalPixels` —— 4/16 个有
- `Fast Groups Bypasser (rgthree)` —— 3/16 个有
- `FastCanvas` —— 1/16 个有
- `FastCanvasTool` —— 1/16 个有
- `InpaintModelConditioning` —— 1/16 个有
- `InspyrenetRembg` —— 1/16 个有
- `RMBG` —— 1/16 个有
- `SaveGLB` —— 1/16 个有
- `Text` —— 1/16 个有
- `Trellis2LoadModel` —— 1/16 个有
- `Trellis2MeshWithVoxelGenerator` —— 1/16 个有
- `Trellis2PostProcessAndUnWrapAndRasterizer` —— 1/16 个有
- `Trellis2SimplifyMesh` —— 1/16 个有
- `TrimeshToMESH` —— 1/16 个有
- `easy promptLine` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 16 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 16 | 48% |
| 采样算法 | euler | - | 16 | 94% |
| 调度器 | beta | - | 16 | 44% |
| 重绘幅度 | 1 | 0.8 - 1 | 16 | 93% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，16 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，16 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 euler，16 个样本，一致性 94%
- 调度器 最常用 beta，16 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，16 个样本，取值集中（一致性 93%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
