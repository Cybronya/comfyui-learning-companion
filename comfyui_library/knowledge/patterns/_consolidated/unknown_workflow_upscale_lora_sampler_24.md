---
name: unknown_workflow_upscale_lora_sampler_24
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.829375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, INTConstant, ImageResize+, ImageScaleBy, KOOK_SaveJPGImage, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingAuraFlow, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KQ12Z真实美感：自动参考图生成新的图（自动图生图）_2035932710065152001.json, 图片生成/图生图/参考生图 · 日系胶片情绪电影叙事造像师_图生图_人像写真_2053742124792860673.json, 图片生成/图生图/超绝美感：自动参考图生成新的图（自动图生图）KQ12Z_2013988779903688705.json, 图片生成/文生图/(真实细节版-贞贞)Qwen2512+Zimage_KOOK真实人像文生图V1_2009156010946076674.json, 图片生成/文生图/2512+Zimage_2016749564656623617.json, 图片生成/文生图/2512+Zimage_真实人像_2009119378654105601.json, 图片生成/文生图/2512+Zimage双采+反推洗图   抖音网红质感_2011725642034847745.json, 图片生成/文生图/Qwen+Zimage 亚洲人像批量出图（全自动撰写提示词）_2047656415975710722.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/KQ12Z真实美感：自动参考图生成新的图（自动图生图）_2035932710065152001.json、图片生成/图生图/参考生图 · 日系胶片情绪电影叙事造像师_图生图_人像写真_2053742124792860673.json、图片生成/图生图/超绝美感：自动参考图生成新的图（自动图生图）KQ12Z_2013988779903688705.json、图片生成/文生图/(真实细节版-贞贞)Qwen2512+Zimage_KOOK真实人像文生图V1_2009156010946076674.json、图片生成/文生图/2512+Zimage_2016749564656623617.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `INTConstant`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_SaveJPGImage`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
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
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `ImageCASharpening+` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `RunningHub Deepcleaner` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `CR Text Concatenate` —— 3/8 个有
- `LatentFrequencyEnhancer_lrzjason` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `CR Text Replace` —— 2/8 个有
- `Int` —— 2/8 个有
- `JDCN_StringToList` —— 2/8 个有
- `ProcessString` —— 2/8 个有
- `Qwen3VL_Chat` —— 2/8 个有
- `RH_LLMAPI_Pro_Node` —— 2/8 个有
- `TTResolutionSelector` —— 2/8 个有
- `Text Concatenate` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/8 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/8 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 88% |
| Prompt 约束强度(CFG) | 8 | 8 - 15 | 8 | 76% |
| 采样算法 | 1 | 1 - 1.1 | 8 | 97% |
| 调度器 | res_2m | - | 8 | 62% |
| 重绘幅度 | sgm_uniform | - | 8 | 62% |
| 宽度 | 1024 | 1024 - 1080 | 8 | 97% |
| 高度 | 1536 | 1536 - 1920 | 8 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 15，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1.1，8 个样本，取值集中（一致性 97%）
- 调度器 最常用 res_2m，8 个样本，一致性 62%
- 重绘幅度 最常用 sgm_uniform，8 个样本，一致性 62%
- 宽度 中位数 1024，观测区间 1024 - 1080，8 个样本，取值集中（一致性 97%）
- 高度 中位数 1536，观测区间 1536 - 1920，8 个样本，取值集中（一致性 89%）
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
