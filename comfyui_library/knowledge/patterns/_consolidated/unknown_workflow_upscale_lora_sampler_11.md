---
name: unknown_workflow_upscale_lora_sampler_11
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.859929
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSamplerAdvanced, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy getNode, easy setNode, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/图生图/Z-image Base & Turbo 双重采样图生图_2063533951230238722.json, 图片生成/文生图/Z-image Base & Turbo 双重采样文生图_2063288090013298690.json, 图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json, 图片生成/文生图/ZIT情绪高清文生图-AIGC大赏_2059815473482657794.json, 图片生成/文生图/三采样提示词人像_2035173666383732738.json, 图片生成/文生图/三采样提示词人像新_2036363794007461890.json, 图片生成/文生图/去AI感高清人像（3采样+超分放大）_2086099313301737473.json, 图片生成/文生图/提示词自动优化+极致真实V2+亿级像素超分放大_2090073751546318849.json, 图片生成/文生图/最强大模型组合：极致高清人像生成+3次采样+超分放大（去AI感）_2070673952455880706.json, 图片生成/文生图/最强大模型组合：极致高清人像生成+3次采样+超分放大（去AI感）图片反推_2071793609908772865.json, 图片生成/文生图/极致真实V2+亿级像素超分放大-QM_2091885341887254529.json, 图片生成/文生图/极致真实V2+亿级像素超分放大_2059627101044695042.json, 图片生成/文生图/极致真实·三采样自动提示词人像工作流_2034275308475523073.json, 视频生成/图生视频/Z-image Base & Turbo+Klein三重采样图生图_2063550240493498369.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Z-image Base & Turbo 双重采样图生图_2063533951230238722.json、图片生成/文生图/Z-image Base & Turbo 双重采样文生图_2063288090013298690.json、图片生成/文生图/Z-image Base & Turbo+Klein三重采样文生图_2063539477594857474.json、图片生成/文生图/ZIT情绪高清文生图-AIGC大赏_2059815473482657794.json、图片生成/文生图/三采样提示词人像_2035173666383732738.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy setNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 13/14 个有
- `PrimitiveInt` —— 13/14 个有
- `SaveImage` —— 13/14 个有
- `CFGGuider` —— 12/14 个有
- `ConditioningZeroOut` —— 12/14 个有
- `EmptyFlux2LatentImage` —— 12/14 个有
- `Flux2Scheduler` —— 12/14 个有
- `GetImageSize` —— 12/14 个有
- `ImageScaleToTotalPixels` —— 12/14 个有
- `KSamplerSelect` —— 12/14 个有
- `RandomNoise` —— 12/14 个有
- `ReferenceLatent` —— 12/14 个有
- `SamplerCustomAdvanced` —— 12/14 个有
- `VAEEncode` —— 12/14 个有
- `LoadImage` —— 11/14 个有
- `PreviewImage` —— 10/14 个有
- `Any Switch (rgthree)` —— 9/14 个有
- `ImageColorMatch+` —— 7/14 个有
- `ImageResize+` —— 7/14 个有
- `ImageScaleBy` —— 7/14 个有
- `TTP_Image_Assy` —— 7/14 个有
- `TTP_Image_Tile_Batch` —— 7/14 个有
- `TTP_Tile_image_size` —— 7/14 个有
- `easy imageSize` —— 7/14 个有
- `llama_cpp_parameters` —— 7/14 个有
- `ColorMatch` —— 5/14 个有
- `Label (rgthree)` —— 3/14 个有
- `CR Text Concatenate` —— 2/14 个有
- `DuckHideNode` —— 2/14 个有
- `SaveText` —— 2/14 个有
- `CompressImages` —— 1/14 个有
- `JindouyunShowAnything` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 14 | 93% |
| Prompt 约束强度(CFG) | 40 | 8 - 40 | 14 | 70% |
| 采样算法 | 4 | 1 - 6.52 | 14 | 65% |
| 调度器 | res_multistep | - | 14 | 86% |
| 重绘幅度 | sgm_uniform | - | 14 | 57% |
| 宽度 | 864 | 864 - 1536 | 14 | 73% |
| 高度 | 1536 | 864 - 1536 | 14 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，14 个样本，一致性 93%
- Prompt 约束强度(CFG) 中位数 40，观测区间 8 - 40，14 个样本
- 采样算法 中位数 4，观测区间 1 - 6.52，14 个样本
- 调度器 最常用 res_multistep，14 个样本，一致性 86%
- 重绘幅度 最常用 sgm_uniform，14 个样本，一致性 57%
- 宽度 中位数 864，观测区间 864 - 1536，14 个样本
- 高度 中位数 1536，观测区间 864 - 1536，14 个样本，取值集中（一致性 80%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
