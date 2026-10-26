---
name: unknown_workflow_lora_sampler_clip_113
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8088
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/游戏_动漫角色设计（画风参考文生图）二次元可用_2055120295245172737.json, 图片生成/文生图/图1给姿势，图2给脸｜Flux Klein 双图融合工作流【全节点注释】_2070728938242011138.json, 数字人/数字人/Klein9B姿态姿势变换_2071404584735698945.json, 数字人/数字人/Klein9B深度+线稿+法线+硬边缘控制图片编辑_2071404639500722177.json, 数字人/数字人/发型替换  - Klein_2083890877629558785.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/游戏_动漫角色设计（画风参考文生图）二次元可用_2055120295245172737.json、图片生成/文生图/图1给姿势，图2给脸｜Flux Klein 双图融合工作流【全节点注释】_2070728938242011138.json、数字人/数字人/Klein9B姿态姿势变换_2071404584735698945.json、数字人/数字人/Klein9B深度+线稿+法线+硬边缘控制图片编辑_2071404639500722177.json、数字人/数字人/发型替换  - Klein_2083890877629558785.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `CR Text` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `GetImageSize+` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `llama_cpp_instruct_adv` —— 1/5 个有
- `llama_cpp_model_loader` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
