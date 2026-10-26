---
name: unknown_workflow_upscale_lora_sampler_18
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.9245
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSamplerAdvanced, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen2512+Zimage真实人像文生图_2009222406086336514.json, 图片生成/文生图/VividMuse真实人像摄影V2_2021926025617219585.json, 图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json, 图片生成/文生图/qwen zimage 超真实文生图  文生图 碎片大佬的_2043365150119436290.json, 图片生成/文生图/qwen zimage 超真实文生图  文生图_2037064489794805761.json, 图片生成/文生图/qwen zimage 超真实文生图  文生图_2043544443818610689.json, 图片生成/文生图/【Supermate 优化】Qwen2512与Z-image双剑合璧KOOK_真实人像_2009155316952342529.json, 图片生成/文生图/文生图_2044010745309958145.json, 图片生成/文生图/文生图_2045378237215281153.json, 图片生成/文生图/极致真实人像（qwen2512出图+Zimage细化+seedvr高清放大）_2020462495428775938.json, 图片生成/文生图/浮光掠影 · 日系胶片情绪电影叙事造像师_文生图_人像写真_2053673047776866305.json, 图片生成/文生图/真实冷感视界 • 若离造像局：定格克制且深邃的胶片余韵_文生图_写真_摄影_氛围感_2042762564811104258.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Qwen2512+Zimage真实人像文生图_2009222406086336514.json、图片生成/文生图/VividMuse真实人像摄影V2_2021926025617219585.json、图片生成/文生图/Z-Image + Z-Image-Turbo realistic photography V3_2057641945413017602.json、图片生成/文生图/qwen zimage 超真实文生图  文生图 碎片大佬的_2043365150119436290.json、图片生成/文生图/qwen zimage 超真实文生图  文生图_2037064489794805761.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 11/12 个有
- `CR Text` —— 10/12 个有
- `ImageCASharpening+` —— 10/12 个有
- `KOOK_SaveJPGImage` —— 10/12 个有
- `ModelSamplingAuraFlow` —— 10/12 个有
- `VAEEncode` —— 10/12 个有
- `RunningHub Deepcleaner` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 6/12 个有
- `INTConstant` —— 5/12 个有
- `SimpleMath+` —— 5/12 个有
- `DuckHideNode` —— 3/12 个有
- `ConditioningZeroOut` —— 2/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/12 个有
- `LoadImage` —— 2/12 个有
- `RHLLMChatNode` —— 2/12 个有
- `easy promptList` —— 2/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `DF_Text_Box` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LayerColor: ColorAdapter` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `Seed (rgthree)` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 83% |
| Prompt 约束强度(CFG) | 10 | 8 - 12 | 12 | 86% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | res_2m | - | 12 | 67% |
| 重绘幅度 | sgm_uniform | - | 12 | 67% |
| 宽度 | 1024 | 1024 - 1536 | 12 | 83% |
| 高度 | 1536 | 1536 - 2048 | 12 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 12，12 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_2m，12 个样本，一致性 67%
- 重绘幅度 最常用 sgm_uniform，12 个样本，一致性 67%
- 宽度 中位数 1024，观测区间 1024 - 1536，12 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1536 - 2048，12 个样本，取值集中（一致性 88%）
