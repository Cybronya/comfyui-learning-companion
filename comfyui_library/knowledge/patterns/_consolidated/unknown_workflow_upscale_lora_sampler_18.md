---
name: unknown_workflow_upscale_lora_sampler_18
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.82225
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, INTConstant, ImageResize+, ImageScaleBy, KOOK_SaveJPGImage, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/(真实细节版-贞贞)Qwen2512+Zimage_KOOK真实人像文生图V1_2009156010946076674.json, 图片生成/文生图/2512+Zimage_2016749564656623617.json, 图片生成/文生图/2512+Zimage_真实人像_2009119378654105601.json, 图片生成/文生图/2512+Zimage双采+反推洗图   抖音网红质感_2011725642034847745.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/(真实细节版-贞贞)Qwen2512+Zimage_KOOK真实人像文生图V1_2009156010946076674.json、图片生成/文生图/2512+Zimage_2016749564656623617.json、图片生成/文生图/2512+Zimage_真实人像_2009119378654105601.json、图片生成/文生图/2512+Zimage双采+反推洗图   抖音网红质感_2011725642034847745.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `INTConstant`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCASharpening+` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `LatentFrequencyEnhancer_lrzjason` —— 2/4 个有
- `RunningHub Deepcleaner` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `CR Text Replace` —— 1/4 个有
- `JDCN_StringToList` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/4 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/4 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `ProcessString` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 9 | 8 - 15 | 4 | 72% |
| 采样算法 | 1 | 1 - 1.1 | 4 | 96% |
| 调度器 | euler | - | 4 | 50% |
| 重绘幅度 | simple | - | 4 | 50% |
| 宽度 | 1024 | 1024 - 1080 | 4 | 98% |
| 高度 | 1536 | 1536 - 1920 | 4 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 9，观测区间 8 - 15，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1.1，4 个样本，取值集中（一致性 96%）
- 调度器 最常用 euler，4 个样本，一致性 50%
- 重绘幅度 最常用 simple，4 个样本，一致性 50%
- 宽度 中位数 1024，观测区间 1024 - 1080，4 个样本，取值集中（一致性 98%）
- 高度 中位数 1536，观测区间 1536 - 1920，4 个样本，取值集中（一致性 90%）
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
