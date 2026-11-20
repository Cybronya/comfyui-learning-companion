---
name: text_to_image_upscale_sampler_clip_19
type: Text To Image
frequency: 5
level: strong
coverage: 0.8746
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, RandomNoise, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/001.Z-image生图巅峰018.拆解图像二次元特征提取_2033756843536814082.json, 图片生成/图生图/🦁Z-image化调度器+真实人像=高清8K出图【文生图】_2004141014912802818.json, 图片生成/文生图/Z-image+Flowmatch新版调度器人像更细腻_2004470762981523457.json, 图片生成/文生图/炮自用ZT8K出图（优化词）自选lora_2036421978042667009.json, 图片生成/文生图/🦁Z-image 二次元拆解专属lora+提取人物特征_2004085200088932353.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/001.Z-image生图巅峰018.拆解图像二次元特征提取_2033756843536814082.json、图片生成/图生图/🦁Z-image化调度器+真实人像=高清8K出图【文生图】_2004141014912802818.json、图片生成/文生图/Z-image+Flowmatch新版调度器人像更细腻_2004470762981523457.json、图片生成/文生图/炮自用ZT8K出图（优化词）自选lora_2036421978042667009.json、图片生成/文生图/🦁Z-image 二次元拆解专属lora+提取人物特征_2004085200088932353.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `RandomNoise`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `KOOK_ImageCompression` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `RH_LLMAPI_NODE` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `Note Plus (mtb)` —— 3/5 个有
- `LoadImage` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `DapaoGeminiInstructionZhenzhenNode` —— 1/5 个有
- `DapaoImageAspectRatioResizeNode` —— 1/5 个有
- `DapaoImageCompressionNode` —— 1/5 个有
- `DapaoSafeSaveImage` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/5 个有
- `Qwen3VL_Chat` —— 1/5 个有
- `String` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2048 | 2048 - 2048 | 5 | 100% |
| 高度 | 2048 | 2048 - 2048 | 5 | 100% |
| 采样步数 | 9 | 9 - 10 | 5 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 2048，观测区间 2048 - 2048，5 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9，观测区间 9 - 10，5 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
