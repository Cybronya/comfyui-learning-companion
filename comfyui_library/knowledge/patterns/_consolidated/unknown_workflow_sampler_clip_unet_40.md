---
name: unknown_workflow_sampler_clip_unet_40
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.891765
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 商业级人像精修｜超强一致性_2085535726921404417.json, 图片生成/图生图/Flux2 Klein_转精致3D建模风格_2041871546448351234.json, 图片生成/图生图/Flux2 Klein_转精致3D建模风格_2042590574431182849.json, 图片生成/图生图/Flux2 Sun Direction LoRA 精确控制‌图片光影_2087880030058795010.json, 图片生成/图生图/Flux2 klein 单图编辑_2062060544747728897.json, 图片生成/图生图/Flux2 klein 双图编辑_2062063724688658433.json, 图片生成/图生图/Flux2 klein 图生图+高清放大_2062043788545191938.json, 图片生成/图生图/Flux2 klein 多图编辑_2062073276687540225.json, 图片生成/图生图/Flux2+Klein9b全能图像编辑：超强一致性全能图像模型_2031926623477436417.json, 图片生成/图生图/Flux2_Klein_商业级人像精修｜超强一致性_2085908338545614849.json, 图片生成/图生图/Flux2_Klein_商业级人像精修｜超强一致性_2085926483779997698.json, 图片生成/图生图/Flux2_klein_图生图+高清放大_2072851483212734466.json, 图片生成/图生图/flux2洗图+放大_2101535680026464257.json, 图片生成/图生图/klein_SU模型图直接渲染效果图+高清放大_2015800051087450114.json, 图片生成/图生图/klein（黑兽BFS）换脸_2039927828656951298.json, 图片生成/图生图/klein（黑兽BFS）换脸_2052845813335904258.json, 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 商业级人像精修｜超强一致性_2085535726921404417.json、图片生成/图生图/Flux2 Klein_转精致3D建模风格_2041871546448351234.json、图片生成/图生图/Flux2 Klein_转精致3D建模风格_2042590574431182849.json、图片生成/图生图/Flux2 Sun Direction LoRA 精确控制‌图片光影_2087880030058795010.json、图片生成/图生图/Flux2 klein 单图编辑_2062060544747728897.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 17 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 16/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/17 个有
- `EmptyFlux2LatentImage` —— 14/17 个有
- `Image Comparer (rgthree)` —— 12/17 个有
- `SeedVR2LoadDiTModel` —— 12/17 个有
- `SeedVR2LoadVAEModel` —— 12/17 个有
- `SeedVR2VideoUpscaler` —— 12/17 个有
- `GetImageSize` —— 10/17 个有
- `CR Text` —— 9/17 个有
- `ImageScaleToTotalPixels` —— 9/17 个有
- `LoraLoaderModelOnly` —— 9/17 个有
- `easy int` —— 7/17 个有
- `GetImageSize+` —— 6/17 个有
- `Anything Everywhere` —— 5/17 个有
- `easy cleanGpuUsed` —— 4/17 个有
- `Fast Groups Bypasser (rgthree)` —— 3/17 个有
- `Fast Groups Muter (rgthree)` —— 3/17 个有
- `ImageCASharpening+` —— 3/17 个有
- `ImageResize+` —— 3/17 个有
- `ImageScaleBy` —— 3/17 个有
- `Int` —— 3/17 个有
- `PreviewImage` —— 3/17 个有
- `TTP_Image_Assy` —— 3/17 个有
- `TTP_Image_Tile_Batch` —— 3/17 个有
- `TTP_Tile_image_size` —— 3/17 个有
- `easy showAnything` —— 3/17 个有
- `Any Switch (rgthree)` —— 1/17 个有
- `CannyEdgePreprocessor` —— 1/17 个有
- `DWPreprocessor` —— 1/17 个有
- `DepthAnythingV2Preprocessor` —— 1/17 个有
- `GetNode` —— 1/17 个有
- `KSamplerAdvanced` —— 1/17 个有
- `ModelSamplingAuraFlow` —— 1/17 个有
- `PreviewAny` —— 1/17 个有
- `PrimitiveFloat` —— 1/17 个有
- `RunningHub Deepcleaner` —— 1/17 个有
- `SetNode` —— 1/17 个有
- `SphereLightNode` —— 1/17 个有
- `llama_cpp_instruct_adv` —— 1/17 个有
- `llama_cpp_model_loader` —— 1/17 个有
- `llama_cpp_parameters` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | beta57 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
