---
name: text_to_image_upscale_lora_sampler_33
type: Text To Image
frequency: 8
level: strong
coverage: 0.905375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FastFilmGrain, GetImageSize+, ImageCASharpening+, ImageResize+, ImageScaleBy, KSampler, LayerColor: BrightnessContrastV2, LoraLoaderModelOnly, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ZB瑶光加密自动优化_2037050547345301505.json, 图片生成/文生图/ZB瑶光加密自动优化极速无扩图_2037071390456680450.json, 图片生成/文生图/ZIMAGE-瑶光文生图_2036262515121856513.json, 图片生成/文生图/Zimage-瑶光文生图工作流_2048264071597789186.json, 图片生成/文生图/Zimage_瑶光-真实人像与海报_2034978396467367938.json, 图片生成/文生图/Zimage_真实人像与海报+qwen3.5 反推 无限制_2035586422165475330.json, 图片生成/文生图/Zimage强化+瑶光+晓玉V3（文生图）_2042119298440765442.json, 图片生成/文生图/（自用）ZB瑶光-自写词-无扩图极速版_2037064604660011009.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/ZB瑶光加密自动优化_2037050547345301505.json、图片生成/文生图/ZB瑶光加密自动优化极速无扩图_2037071390456680450.json、图片生成/文生图/ZIMAGE-瑶光文生图_2036262515121856513.json、图片生成/文生图/Zimage-瑶光文生图工作流_2048264071597789186.json、图片生成/文生图/Zimage_瑶光-真实人像与海报_2034978396467367938.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FastFilmGrain`
- `GetImageSize+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LayerColor: BrightnessContrastV2`
- `LoraLoaderModelOnly`
- `RunningHub Deepcleaner`
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
- `KOOK_SaveJPGImage` —— 6/8 个有
- `CR Text` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `TT_img_enc_v2` —— 3/8 个有
- `ZML_SwitchOutput` —— 3/8 个有
- `DapaoPromptNode` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `llama_cpp_instruct_adv` —— 2/8 个有
- `llama_cpp_model_loader` —— 2/8 个有
- `llama_cpp_parameters` —— 2/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `CR Text Replace` —— 1/8 个有
- `Fast Bypasser (rgthree)` —— 1/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `JDCN_StringToList` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有
- `ProcessString` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 8 | 100% |
| 高度 | 1920 | 1920 - 1920 | 8 | 100% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | res_2s | - | 8 | 100% |
| 调度器 | bong_tangent | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，8 个样本，一致性 100%
- 调度器 最常用 bong_tangent，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
