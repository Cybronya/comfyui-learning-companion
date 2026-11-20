---
name: image_to_image_lora_sampler_unet_165
type: Image To Image
frequency: 5
level: strong
coverage: 0.8798
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, Preview3D, SaveGLB, SaveImage, TextEncodeQwenImageEditPlus, Trellis2ExportMesh, Trellis2LoadModel, Trellis2MeshWithVoxelGenerator, Trellis2PostProcessAndUnWrapAndRasterizer, Trellis2SimplifyMesh, TrimeshToMESH, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/用 Blender 灯光图驱动 Qwen 2511：一键把图2打光迁移到图1（AnyLight)_2014246399210164226.json, 平台全量/AI生成个人3D卡通手办模型，支持一键导入3D打印机！_2005555017417453569.json, 平台全量/AI生成个人3D卡通手办模型，支持一键导入3D打印机！_2056924842833825794.json, 平台全量/AI生成个人3D卡通手办模型，支持一键导入3D打印机！_2057285054505766914.json, 平台全量/TRELLIS 可爱Q版模型 人物肖像图片生成3D卡通手办模型 支持一键导入3D打印机_2025453828929232898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_165

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/用 Blender 灯光图驱动 Qwen 2511：一键把图2打光迁移到图1（AnyLight)_2014246399210164226.json、平台全量/AI生成个人3D卡通手办模型，支持一键导入3D打印机！_2005555017417453569.json、平台全量/AI生成个人3D卡通手办模型，支持一键导入3D打印机！_2056924842833825794.json、平台全量/AI生成个人3D卡通手办模型，支持一键导入3D打印机！_2057285054505766914.json、平台全量/TRELLIS 可爱Q版模型 人物肖像图片生成3D卡通手办模型 支持一键导入3D打印机_2025453828929232898.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `Preview3D`
- `SaveGLB`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `Trellis2ExportMesh`
- `Trellis2LoadModel`
- `Trellis2MeshWithVoxelGenerator`
- `Trellis2PostProcessAndUnWrapAndRasterizer`
- `Trellis2SimplifyMesh`
- `TrimeshToMESH`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 4/5 个有
- `Light-Tool: SaveToAliyunOSS` —— 4/5 个有
- `PreviewAny` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `RMBG` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `GetImageSize+` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `String Literal` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
